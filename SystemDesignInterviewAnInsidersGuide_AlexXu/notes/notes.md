## Interview Framework 

- ability to collabrate, work under pressure, resolve ambiguity constructively
- not over-engieer while delight in design purity and ignore tradeoffs
- not get carried away with details without demonstrating your abilities

Good questions to ask

- what specific features to build
- how many users does the product have
- what is the company's technology stack


## Relational database vs Non-relational database

- relational database naturally enforce atomicity, good for strong consistency.
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


### ACID

- Atomic: updates all or nothing
- Consistency: going from 1 valid state to another valid state
- Isolation: concurrent transaction do not interfere with each other (when no conflict)
- Durability: once commited, permanently saved (even power failure)
  
- Relational database, mongoDb, redis transaction, Apache Kafka (You can write to multiple topics atomically)


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


## Numbers 

### High availability

- most services fall between 99% and 100%
- the more nines, the better. 99.99% = 53 minutes down time per year

### Twitter Example (not real)

- 300 million MAU
- 50% users use twitter daily -> 150 million DAU
- 2 tweets per user per day -> tweet QPS = 150 million * 2 tweets / 24 / 3600 = ~3500
- Peek QPS = 2 * QPS


## Video protocols

- Codec = How you compress the item (vacuum seal, bubble wrap)
  - Reduce file size while maintaining quality

- Container = The box/package format (.mp4, .avi, .mov)
  - Combine video, audio, subtitles, metadata into one file

- Streaming Protocol = The delivery method (FedEx, UPS, postal service)
  - How to deliver video over the network efficiently


## Distributed System

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