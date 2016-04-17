CC = gcc -std=gnu99

CFLAGS = -Wall -pedantic -Werror

SERVER_FILES = src/server.c src/cache.c src/lru.c src/tcp.c src/udp.c

server:
	$(CC) $(SERVER_FILES) -o $@

clean:
	rm server
