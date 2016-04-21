CC = gcc -std=gnu99

# CFLAGS = -Wall -pedantic -Werror

all:
	make server 
	make set_client 
	make get_client
	make delete_client

SOURCE_FILES = src/cache.c src/lru.c src/tcp.c src/udp.c

server:
	$(CC) src/server.c $(SOURCE_FILES) -o $@

set_client:
	$(CC) src/set_client.c $(SOURCE_FILES) -o $@
 
get_client:
	$(CC) src/get_client.c $(SOURCE_FILES) -o $@

delete_client:
	$(CC) src/delete_client.c $(SOURCE_FILES) -o $@

clean_server:
	rm server

clean_clients:
	rm set_client get_client delete_client

clean:
	rm server set_client get_client delete_client

