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
##### Setup:
We use Python's SciPy library to generate random variables for key and val size according the the distributions given in the paper. We also use a python script to handle setting up our server and clients.

##### Method:
Our python script first sets a specified number of key/val pairs in our cache and then spawns clients. Each client is timed for the amount of time it takes complete all of its requests (we don't care about the error rate of UDP so much, as long as it doesn't look unrealistically high). This is then averaged to find a mean response time for requests.

###Step 9 Analyze and Interpret Data
##### Table of results: 
| SERVICE | GET | SET | DELETE |
| --- | --- | --- | --- |
| Average response time (msec) | 0.283 | 0.685 | 0.5486 |
| Total Load (requests/sec) | 17700 | 7300 | 9110 |
| Failure rate (%) | 4.96 | N/A | N/A |
(All values are 3 sig. figs.)

###Step 10 Present Results
See above.
