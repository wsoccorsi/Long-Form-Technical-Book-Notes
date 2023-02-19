* System Design Interview Volume 1 - An Insiders Guide by Alex Xu


## Chapter 2 - Back-Of-The Envelope Estimate
* You need to have a good sense of estimating to see how your designs meet design requirements
* An ASCII character uses one byte of memeory (8 bits) 

| Operation Name      | Time |
| -----------         | ----------- |
| LI Cache Reference  | 0.5 ns       |
| Branch mispredict   | 5 ns        |
| L2 cache reference  | 7 ns        |
| Mutex lock/unlock   | 100 ns       |
| Main memory reference  | 100 ns        |
| Compress 1k bytes with Zippy | 10k ns |
| Send 2k Bytes over 1 Gbps network   | 20k ns |
| Read 1 MB sequentially from memory  | 250k ns  |
| Round trip within the same datacenter | 500k ns  |
| Disk seek | 10 ms ns  |
| Read 1 MB sequentially from the network | 10 ms ns  |
| Read 1 MB sequentially from disk | 30 ms |
| Send pack CA => Netherlands -> CA | 150 ms |

* Memory is fast but the disk is slow
* Avoid disk seeks if possible
* Simple compression algos are fast
* Compress data before sending it over the internet if possible
* Data centers are usually in different regions, and it takes time to send data between them


* High Availability is the ability of a system to be continuously operational for a desirably long period of time. 
* HA is measured as a percentage
* SLA - Service Level Agreement and it defines the up time the service will deliver
* 99% = 3.65 days of downtime a year, 99.9999% = 31.56 seconds a year


Example: Estimate Twitter QPS and storage reqs:


Assumptions: 
  
  - 300 million monthly active users
  - 50% of users use Twitter daily
  - Users post 2 tweets per day on average
  - 10% of tweets contain media
  - Data is stored for 5 years
  
Estimations:

  - Daily active users (DAU) = 300 million * 50% = 150 million
  - Tweets QPS = 150 million * 2 tweets / 24 hour / 3600 seconds = ~3500
  - Peak QPS = 2 * QPS = ~7000
 
Media Storage: 

  * Average tweet size:
    * tweet_id: 64 bytes
    * test: 140 bytes
    * media: 1 MB

  - 150 * 2 * 10% * 1 MB = 30TB per day
  - 5-year media storage: 30 TB * 365 * 5 = ~55PB

* Commonly asked back-of-the-envelope estimates: QPS, peak, storage, cache, number of servers, etc..

## Chapter 3 - A Framework for System Design Interviews

* 