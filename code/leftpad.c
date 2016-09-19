#include <ctype.h>
#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * left_pad_string(char *ip, size_t ip_count, size_t pad_count)
{
  char * ret;
  uint32_t i;
  if (pad_count < ip_count) {
    ret = strndup(ip, ip_count);
  } else {
    ret = (char *)calloc(pad_count+ip_count, sizeof(char));
    for (i=0; i<(pad_count - ip_count); i++) {
      ret[i] = ' ';
    }
    strncat(ret, ip, ip_count);
  }
  return ret;
}

int
main()
{
  char ip[] = "python";
  char *op = left_pad_string(ip, strlen(ip), 25);
  printf("'%s'\n", op);
  free(op);
  return 0;
}
