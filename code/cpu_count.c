#include <inttypes.h>
#include <stdio.h>
#include <stdbool.h>

uint32_t cpu_count(bool);

void main() 
{
  uint32_t physical;
  physical = cpu_count(false);
  printf("Physical : %" PRIu32 "\n", physical);
}

