# Benchmarking Network Cache
##### Alec Kosik and Alex Pan
<br />
#####Disclaimer:
```

Compiled and tested on Mac/Linux (done by adding -gnu=c99 flag to compile on Linux)
Make file will work on Mac/Linux, no need for any changes if testing on either operating system

./server //will run server side
./client //will run client side
```

To clone this repository:
```git clone --recursive https://github.com/apanana/NetworkBenchmarks.git```

Leaving out the recursive flag will make git ignore the submodule jsmn and stunt client compilation.


<br />
###Step 1 State Goals and Define the System
Goals: To benchmark the performance over various inputs and systems
System: Networked cache and client. We use raw sockets (instead of any networking libraries) and send communcations over UDP and TCP.


###Step 2 List Services and Outcomes
We are using a network cache service over TCP and UDP.
Services:
* SET /k/v: Sets a key-value pair in the cache. Creates entries for new keys and overwrites values for existing keys.
* GET /k: Retrieves at key-value pair from the cache. Returns the value corresponding to the key and the value size if the key exists in the cache, and returns NULL otherwise.
* DELETE /k: Deletes a key-value pair from the cache. No effect on the cache if key does not exist.
(There are some more cache functions and POST requests and HEAD requests to be accounted for. Both POST requests for creating and destroying the cache are only called at the beginning and end of usage. HEAD requests don't really interface with any cache functions so we aren't going to test out performance for that either)


###Step 3 Select Metrics
* Sustained throughput, defined as the maximum offered load (in requests per second) at which the mean response time remains under 1 millisecond. 
* (???Maybe???) Accuracy of GET requests, defined as the maximum number of packets at which average success rate is over 95%.


###Step 4 List Parameters
* Systems:
	* Server/Client OS
	* Server/Client CPU speed
	* Network bandwidth

* Workload:
	* Number of requests
	* Time intervals between request
	* Average key/val size
	* Packet size


###Step 5 Select Factors to Study
#####Dependent Variable:
* Mean response time ("Inter arrival-gap")

#####Independent Variables:
* Requests per second 

#####Constant Variables:
* Number of requests
* Packet size

#####Other Variables:
(These values are modeled on the distributions outlined in the FB Memcache paper.)
* Average key/val size



###Step 6 Select Evaluation Technique
* Simulation:
	We aim to model our throughput on the ETC workload of Facebook's memcache and measure our networked cache's performance against that workload.
(We will not be measuring a real system since we do not have a real system to test)


###Step 7 Select Workload
Our simulation aim's to mimic the workload of FB's memcache while varying the requests per second. 


###Step 8 Design Experiments
We used all of the polytopia computers to test our cache. One computer ran the server while the others acted as clients. We synchronized start times of each client and averaged all mean response times over all clients as well as the calculated number of requests per second. 

In order to simulate the memcache workload we replicated a generalized extreme value distribution (mu = 30.7984, sigma = 8.20449, k = 0.078688) for the keys and a generalized pareto distribution (theta = 0, sigma = 214.476, k = 0.348238) for the values, the same distributions used in the memcache workload analysis paper (Frachtenberg et al.).

Our 

###Step 9 Analyze and Interpret Data
##### Table of results: 
| SERVICE | GET | SET | DELETE | GET* |
| --- | --- | --- | --- | --- |
| Average response time (msec) | 0.283 | 0.685 | 0.5486 | 0.438 |
| Total Load (requests/sec) | 17700 | 7300 | 9110 | 11400 |
| Failure rate (%) | 4.96 | N/A | N/A | 8.41 |
(All values are 3 sig. figs.)

##### Interpretation:
First, we examine just `GET`, `SET`, and `DELETE`. We will discuss `GET` versus `GET*`, which is the rerun of our `GET` tests, next.

We note a marked difference between the speeds of `GET` versus `SET` and `DELETE`. This is to be expected, since `GET` is over UDP while `SET` and `DELETE` are over TCP. We also note that `SET` is slower than `DELETE`, which is what we would expect, since `SET` requires more operations within the cache to complete a request. 

`GET*` refers to us rerunning tests on `GET` while making sure that every single `GET` request is actually something that exists in the cache. We suspect that a portion of the increased time might be due to other clients still sending SET requests after the timed client begins its timing cycle. This would probably be only a negligible amount of increase, but we may make changes to our experimental design later to better maintain independency and contamination like this.

We noticed that `GET*` was slower than `GET`, though still faster than `SET` and `DELETE`. We expected it to be faster than the TCP operations, since it still runs over UDP. We also expect it to run slower than `GET` since there are no longer any requests that should be returning NULL, so the average response size is significantly larger. 

Due to the limited resources of polytopia we were not able to reach our maximum load, in fact, we couldn't even get close.  We were, however, able to approach a millisecond if our server took its good old time to display all of the clients' requests and its responses.

###Step 10 Present Results
See table above.
