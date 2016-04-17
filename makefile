CC = gcc

# CFLAGS = -Wall -pedantic -Werror

all:
	make server 
	make set_client 
	make get_client

server:
	$(CC) -std=gnu99 server.c cache.c lru.c tcp.c udp.c -o $@

set_client:
	$(CC) -std=gnu99 set_client.c client.c jsmn/jsmn.c tcp.c udp.c -o $@
 
get_client:
	$(CC) -std=gnu99 get_client.c client.c jsmn/jsmn.c tcp.c udp.c -o $@

clean_server:
	rm server

clean_client:
	rm client

clean:
	rm server set_client get_client

