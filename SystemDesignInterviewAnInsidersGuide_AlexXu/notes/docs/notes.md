## Interview Framework 

- ability to collabrate, work under pressure, resolve ambiguity constructively
- not over-engieer while delight in design purity and ignore tradeoffs
- not get carried away with details without demonstrating your abilities

Good questions to ask

- what specific features to build
- how many users does the product have
- what is the company's technology stack

## Numbers 

### High availability

- most services fall between 99% and 100%
- the more nines, the better. 99.99% = 53 minutes down time per year

### Twitter Example (not real)

- 300 million MAU
- 50% users use twitter daily -> 150 million DAU
- 2 tweets per user per day -> tweet QPS = 150 million * 2 tweets / 24 / 3600 = ~3500 per second
  - This is number of tweets created per second, not QPS
- Peek QPS = 2 * QPS

Real Twitter num:
- 300k QPS
- 5000 tweets per second

RPS by Language server:
- typical 10,000 RPS per server
- FastAPI/Uvicorn (ASGI): 10,000-30,000+ RPS (async capabilities help significantly)
- Go (Gin, Echo, net/http): 50,000-200,000+ RPS (excellent concurrency model)
- Spring Boot with Tomcat: 10,000-50,000+ RPS for simple endpoints on good hardware
- Netty/Vert.x (async/reactive): 100,000-500,000+ RPS possible due to non-blocking I/O


## Relational database vs Non-relational database

- relational database naturally enforce atomicity, good for strong consistency. (ACID)
- no-relational has low latency, easier for replication/sharding, good for strong availability

### Relational databases:

Pros:
- You need structured data with clear relationships
- ACID transactions are important (e.g., financial applications)
- You need to perform complex join operations across tables
- Data model and format are known in advance (having a schema)

Cons:
- They are difficult to scale horizontally due to their relational nature (hard to partition due to all the foreign key references)
- They require up-front design, and changes are harder (requiring data migrations and possibly downtime)
- Not effective for storing and querying unstructured data
- Relational databases do not handle long tail of data well - when indexes grow large, random access is expensive

### CAP Theorem

- Partition Tolerence
  - If you can't handle partitions, your system goes down when (not if) network issues occur
  - The only true "CA" system is a single-node database—no network, no partitions possible

#### Distributed System

The Inevitable Choice:

When a partition happens, you're forced to choose:
[Node A] ----X---- [Node B]
        (partition)

- Write request arrives at Node A
- Read request arrives at Node B

Your only options:
Choose Consistency (CP): Block/reject requests until partition heals
- Node B refuses reads: "Service unavailable"
- Sacrifices Availability

Choose Availability (AP): Accept requests on both sides
- Node B returns potentially stale data
- Sacrifices Consistency

### PACELC

```
CAP says: "During partition, choose A or C"
PACELC says: "During partition, choose A or C; 
              during normal operation, choose L or C"
```

- EL: Prioritize Low Latency over Consistency
  - Replicate asynchronously
  - Reads might see slightly stale data
  - Fast responses


- EC: Prioritize Consistency over Latency
  - Replicate synchronously
  - Wait for acknowledgments from multiple nodes
  - Slower responses but guaranteed consistency

### ACID

- Atomic: updates all or nothing
- Consistency: going from 1 valid state to another valid state
- Isolation: concurrent transaction do not interfere with each other (when no conflict)
- Durability: once commited, permanently saved (even power failure)
  
- Relational database, mongoDb, redis transaction, Apache Kafka (You can write to multiple topics atomically)

### BASE:

- Basically Available: System appears to work most of the time (tolerates partial failures)
- Soft State: Data state may change over time without new input (due to eventual consistency)
- Eventual Consistency: Given enough time with no updates, all replicas will converge to the same value

### NoSQL:

Pros:
- easy horizontal scaling and low latency to access
- Flexible schema that enables faster development
- Better suited for massive amounts of data
  
Cons:
- Join operations are generally not supported
- only eventual consistency achieved
- Larger data storage footprint due to more data duplication from lack of normalization (not good for mobile app)


## Sharding

- large database into smaller parts (part of user data by userId)
- share same schema
- hard to perform join operations, common workaround is to de-normalize so queries can be performed in a single table


Celebrity problem:

- allocate a shard for each celebrity
- each shard might even require further partition
