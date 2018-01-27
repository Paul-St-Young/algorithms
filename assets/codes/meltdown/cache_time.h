#include <x86intrin.h>

static inline int
get_access_time(volatile char *addr)
{
  int time1,time2,junk;
  volatile int j;

  time1 = __rdtscp(&junk);
  j = *addr;
  time2 = __rdtscp(&junk);
  return time2-time1;
}
