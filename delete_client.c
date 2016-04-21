#include <stdio.h>
#include <stdint.h>
#include <assert.h>
#include <stdlib.h>
#include <mach/mach_time.h>

#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <netdb.h>
#include <unistd.h>
#include <errno.h>
#include "client.h"
char *hostname;
char *tcpport;
char *udpport;

struct cache_obj
{
  char* host;
  char* tcpport;
  char* udpport;
  struct addrinfo *tcpinfo;
  struct addrinfo *udpinfo;
};

cache_t make_cache(uint64_t maxmem)
{
  //create local cache object
  cache_t cache = calloc(1,sizeof(struct cache_obj));
  cache->host = hostname;
  cache->udpport = udpport;
  cache->udpinfo = calloc(1,sizeof(struct addrinfo));

  struct addrinfo hints;
  
  int status;

  memset(&hints, 0, sizeof(hints));
  hints.ai_family = AF_UNSPEC;
  hints.ai_socktype = SOCK_DGRAM;
  if ((status = getaddrinfo(cache->host, "3001", &hints, &cache->udpinfo)) != 0)
    {
      fprintf(stderr, "getaddrinfo for udp: %s\n", gai_strerror(status));
      freeaddrinfo(cache->udpinfo);
      free(cache);
      exit(1);
    }
  return cache;
}

void test_gets(uint8_t* keys, uint64_t numpairs)
{
  cache_t cache = make_cache(0);
  char **keystrings = calloc(numpairs,sizeof(char*));

  for(int i = 0; i < numpairs; ++i)
    {
      keystrings[i] = calloc(keys[i],1);
      memset(keystrings[i],'K',keys[i]);
      keystrings[i][keys[i] - 1] = '\0';
    }

  // Get the timebase info
  // mach_timebase_info_data_t info;
  // mach_timebase_info(&info);

  uint64_t errors = 0;
  const uint64_t requests = numpairs;
  const double nsToSec = 1000000000;
  const uint32_t nsToms = 1000000;
  // uint64_t start = mach_absolute_time();
  struct timespec start, end;
  clock_gettime(CLOCK_MONOTONIC,&start);
  for(int i = 0; i < requests; ++i)
    {
      if( cache_delete(cache,keystrings[i]) == -1) ++errors;
      //if( val_size == 0) ++errors;
      //val_size = 0;
    }
  // uint64_t end = mach_absolute_time();
  clock_gettime(CLOCK_MONOTONIC,&end);
  // uint64_t duration = end - start;
  uint64_t duration = (end.tv_sec * nsToSec + end.tv_nsec) - (start.tv_sec * nsToSec + start.tv_nsec);

  // Convert to nanoseconds
  // duration *= info.numer;
  // duration /= info.denom;

  uint64_t ns = duration;
  double time_elapsed_sec = (double) duration / nsToSec;

  double requests_per_second = (double) requests / time_elapsed_sec;
  double ms = (double) ns / (requests * nsToms);

  printf("Time per Get: %f milliseconds\n",ms);
  printf("Requests per second: %f requests\n",requests_per_second);
  printf("Percent of Requests that failed: %f,%d,%d\n",((double)errors/requests),errors,requests);
}

int main(int argc, char *argv[])
{
  hostname = "134.10.103.229";
  tcpport = "2001";
  udpport = "3001";

  int i = 0,j = 0;
  uint8_t k;
  uint32_t v;
  uint64_t numpairs = atoi(argv[1]);
  uint8_t *keys = calloc(numpairs,sizeof(uint8_t));
  uint32_t *values = calloc(numpairs,sizeof(uint32_t));
  while (scanf("%"PRIu8,&k) == 1)
  {
    keys[i++] = k;
    if( i >= numpairs )
      break;     
  }

  while (scanf("%"PRIu32,&v) == 1)
    {
      values[j++] = v;
      if( j >= numpairs )
        break;
    }

  test_gets(keys,numpairs); //udp test
}