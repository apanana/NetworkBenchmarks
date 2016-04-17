CC = gcc

CFLAGS = -Wall -pedantic -Werror

all:
	make server
	
server:
	$(CC) -std=gnu99 server.c cache.c lru.c tcp.c udp.c -o $@

# client:
# 	$(CC) -std=gnu99 test.c testing.c client.c jsmn/jsmn.c tcp.c udp.c -o $@

# clean_server:
# 	rm server

# clean_client:
# 	rm client

clean:
	rm server
	# rm server client
