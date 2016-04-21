CC = gcc -std=gnu99

# CFLAGS = -Wall -pedantic -Werror

all:
	make server 
	make set_client 
	make get_client
	make delete_client

SERVER_FILES = src/server.c src/cache.c src/lru.c src/tcp.c src/udp.c

server:
	$(CC) $(SERVER_FILES) -o $@

set_client:
	$(CC) set_client.c client.c jsmn/jsmn.c tcp.c udp.c -o $@
 
get_client:
	$(CC) get_client.c client.c jsmn/jsmn.c tcp.c udp.c -o $@

delete_client:
	$(CC) delete_client.c client.c jsmn/jsmn.c tcp.c udp.c -o $@

clean_server:
	rm server

clean_clients:
	rm set_client get_client delete_client

clean:
	rm server set_client get_client delete_client

