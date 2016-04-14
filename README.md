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
System: Networked cache and client


###Step 2 List Services and Outcomes
Services:
* SET /k/v: Sets a key-value pair in the cache. Creates entries for new keys and overwrites values for existing keys.
* GET /k: Retrieves at key-value pair from the cache. Returns the value corresponding to the key and the value size if the key exists in the cache, and returns NULL otherwise.
* DELETE /k: Deletes a key-value pair from the cache. No effect on the cache if key does not exist.


###Step 3 Select Metrics
* Sustained throughput, defined as the maximum offered load (in requests per second) at which the mean response time remains under 1 millisecond. 
* Accuracy of GET requests, defined as the maximum number of packets at which average success rate is over 95%. (this may change!)

###Step 4 List Parameters
* Systems:
** Server/Client OS
** Server/Client CPU speed
** Network bandwidth

* Workload:
** Time intervals between request
** Average key/val size
** Packet size

###Step 5 Select Factors to Study


###Step 6 Select Evaluation Technique

###Step 7 Select Workload

###Step 8 Design Experiments

###Step 9 Analyze and Interpret Data

###Step 10 Present Results
