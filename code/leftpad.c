#include <ctype.h>
#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *
left_pad_string(char *ip, size_t ip_count, size_t pad_count)
{
  char * ret;
  uint32_t i, j;
  ret = (char *)calloc(pad_count, sizeof(char));
  for (i=0; i<(pad_count - ip_count); i++) {
    ret[i] = ' ';
  }
  for (j=0; j<ip_count; j++, i++) {
    ret[i] = ip[j];
  }
  ret[i] = '\0';
  return ret;
}

int
main()
{
  char ip[] = "python";
  char *op = left_pad_string(ip, strlen(ip), 15);
  free(op);
  return 0;
}
