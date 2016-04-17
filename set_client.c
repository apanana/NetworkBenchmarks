#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <mach/mach_time.h>
#include "cache.h"

char *hostname;
char *tcpport;
char *udpport;

void test_gets(uint8_t* keys, uint32_t* values, uint64_t numpairs)
{
  cache_t cache = create_cache(numpairs*10);

  char **keystrings = calloc(numpairs,sizeof(char*));
  char **valstrings = calloc(numpairs,sizeof(char*));

  for(int i = 0; i < numpairs; ++i)
    {
      keystrings[i] = calloc(keys[i],1);
      valstrings[i] = calloc(values[i],1);
      memset(keystrings[i],'K',keys[i]);
      memset(valstrings[i],'V',values[i]);
      keystrings[i][keys[i] - 1] = '\0';
      valstrings[i][values[i] - 1] = '\0';
      cache_set(cache,keystrings[i],valstrings[i],values[i]);
      free(valstrings[i]);
    }
  free(valstrings);
}


int main(int argc, char *argv[])
{
  hostname = "134.10.103.234";
  tcpport = "2001";
  udpport = "3001";
  int i = 0,j = 0;
  uint8_t k;
  uint32_t l;
  uint64_t numpairs = atoi(argv[1]);
  uint8_t *keys = calloc(numpairs,sizeof(uint8_t));
  uint32_t *values = calloc(numpairs,sizeof(uint32_t));
  while (scanf("%d",&k) == 1)
    {
      if( i >= numpairs - 1)
        break;

      keys[i++] = k;
    }
  while (scanf("%d",&l) == 1)
    {
      if( j >= numpairs )
        break;

      values[j++] = l;
    }
  test_gets(keys,values,numpairs); //udp test
}
