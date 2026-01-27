# System Design Interview Steps



### Step 1: Understand the Problem: (7 mins)

- What are functional requirements
- What are non-functional requirements
  - Availability vs Consistency
    - 99.99% available = 53 minutes down per year
  - Cost ?, Security ?
  - How many users does it support? DAU, MAU 
    - DAU is 40% - 50% of MAU for high egagement application
      - 300 million MAU
      - 50% users use twitter daily -> 150 million DAU
      - 2 tweets per user per day -> tweet QPS = 150 million * 2 tweets / 24 / 3600 = ~3500 per second
      - Peek QPS = 2 * QPS
    - Calculate Request Per Secs, storage size
  - Read heavy or write heavy ?



### Step 2: High Level Design: (12 mins)

- design APIs (Mostly REST, maybe websocket)

- Data Modeling:

  - create simple schema, list most important tables and fields, indexing options

  - read to write ratio ?

  - SQL vs NoSQL implementation

    - **What are the consistency requirements?** Strong → SQL, Eventual → NoSQL
    - **What's the read/write ratio?** Heavy writes at scale → NoSQL
    - **Do we need complex queries or just lookups?** Complex → SQL, Simple → NoSQL
    - **What's the expected scale?** Moderate → SQL, Massive → NoSQL

    Many modern systems use **both**:

    - SQL for transactional data (orders, payments)

    - NoSQL for high-volume data (logs, metrics, user activity)

      

- Draw high level diagram:

  - This might include clients (mobile/web), APIs, web servers, data stores, cache, CDN, message queue, etc.
  - Explain in this diagram how function requirements are achieved, e.g.: how user post, get news feed.



### Step 3: Deep Dive: (20 mins)

- For url shortener, dive into the hash function design that converts a long URL to a short one
- For a chat system, how to reduce latency, and how to support online/offline status
- Do not get carried away with minute details that do not demonstrate my abilities



### Step 4: Improve the Design: (7 mins)

- bottlenecks 
  - single point of failure
  - data replication
  - CDNs
  - high traffic
  - Scalability

- how to monitor metrics and error logs
- how to handle the next scale, support from 1 mil users to 10 mil users

