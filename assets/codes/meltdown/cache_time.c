#define _GNU_SOURCE
#include <stdio.h>
#include "cache_time.h" // get_access_time

static char target_array[1];
#define ESTIMATE_CYCLES 1000000
static void
set_cache_hit_threshold(void)
{
  long cached, uncached, i;

  for (cached = 0, i = 0; i < ESTIMATE_CYCLES; i++)
    cached += get_access_time(target_array);

  for (cached = 0, i = 0; i < ESTIMATE_CYCLES; i++)
    cached += get_access_time(target_array);

  for (uncached = 0, i = 0; i < ESTIMATE_CYCLES; i++) {
    _mm_clflush(target_array);
    uncached += get_access_time(target_array);
  }

  cached /= ESTIMATE_CYCLES;
  uncached /= ESTIMATE_CYCLES;

  printf("cached = %ld, uncached = %ld\n",
         cached, uncached);
}

int main()
{
  set_cache_hit_threshold();
}
