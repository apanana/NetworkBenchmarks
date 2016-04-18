import socket, sys, concurrent.futures
from distribution import *
from time import perf_counter as pc

def cache_setup(keys,vals):

        host = "134.10.103.234"
        port = 2001

        # set all keys in cache, won't recv whole messages--doesn't matter
        for key,val in zip(keys,vals):
                try:
                        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                except socket.error:
                        print('Failed to create socket')
                        sys.exit()

                msg = bytes('PUT /{}/{}\0'.format('K'*key,'V'*val),'utf-8')

                s.connect((host, port))
                s.send(msg)

                d = s.recv(1024)
                s.close()

def cache_get(key,s):

        host = "134.10.103.234"
        port = 3001

        msg = bytes('GET /{}\0'.format(key),'utf-8')

        try:
                s.sendto(msg, (host,port))
                d = s.recvfrom(1024)
        except socket.error:
                print('Error Code')
                sys.exit()

def start_client(keys):
        # make socket
        try:
                s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        except socket.error:
                print('Failed to create socket')
                sys.exit()

        # start timer, get all keys, stop, divide, return
        start = pc()
        for key in keys:
                cache_get(key,s)
        elapsed = pc() - start
        elapsed /= len(keys)
        return elapsed

def test_gets(getsPerSec):

        # controversial number, this assumes each client will make a request every 2 ms
        # right now the mean response time is around 3ms so this needs to be changed/rethought
        clients = getsPerSec//500

        # gen keys and values
        keys = gen_keys(1000)
        vals = gen_vals(1000)

        cache_setup(keys,vals)

        # setup keys as an array of strings to save time in gets
        keys = ['K'*key for key in keys]

        # init final result
        m_request_time = 0

        # weird fucking python code that secretly runs the world in what, 10 or so lines?
        with concurrent.futures.ThreadPoolExecutor(max_workers=clients) as executor:

                # Start the load operations and mark each "future" with its client id
                future_to_client = {executor.submit(start_client, keys): client for client in range(0,clients)}

                # as clients finish, collect mean_request times
                # 'future' is an object returned by each job that holds the result
                for future in concurrent.futures.as_completed(future_to_client):

                        # find client id
                        client = future_to_client[future]

                        # get return value from each client
                        try:
                                mean_request_time = future.result()
                        except Exception as exc:
                                print('%r generated an exception: %s' % (client, exc))
                        else:
                                print('Mean Request Time: %f' % mean_request_time)
                                m_request_time += mean_request_time

        m_request_time /= clients
        print("Total Mean Request Time: %f" % m_request_time)


if __name__ == '__main__':
        test_gets(int(sys.argv[1]))
