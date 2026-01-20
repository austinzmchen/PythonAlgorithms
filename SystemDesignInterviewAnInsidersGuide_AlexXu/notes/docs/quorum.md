## Quorum:

Pick R, W using (N / 2 + 1), N is the total nodes count

Using an odd number of nodes for quorum is better because it maximizes fault tolerance without wasting resources.

Fault Tolerance is the Same
For quorum-based systems (like Raft, Paxos, or ZooKeeper), you need a majority to make decisions:

- 5 nodes: Need 3 for quorum, can tolerate 2 failures
- 6 nodes: Need 4 for quorum, can tolerate 2 failures (same!)
- 7 nodes: Need 4 for quorum, can tolerate 3 failures
- 8 nodes: Need 5 for quorum, can tolerate 3 failures (same!)

----------

### Problem 1: Quorum Doesn't Guarantee Consistency in All Scenarios

This is the more subtle issue. Even with R + W > N, you can still see inconsistent data in certain edge cases.

```
Scenario 1: Concurrent Writes

Time T1: Client A writes "X" to nodes [1, 2, 3] (W=3)
Time T1: Client B writes "Y" to nodes [2, 3, 4] (W=3)

Both writes succeed concurrently!

Read from [1, 2, 5]:
- Node 1 has "X"
- Node 2 has both "X" and "Y" (conflict!)
- Node 5 has old data

Which value do you return?
```

The quorum guarantees you'll see at least one latest value, but you might see multiple conflicting "latest" values. You need:

Vector clocks or timestamps to detect conflicts
Application-level conflict resolution

**Vector Clock**: If the counters on the first object’s clock are less-than-or-equal to all of the nodes in the second clock,
then the first is an ancestor of the second

-------------

### Problem 2: lower availability

At any time, the system needs to ensure that at least a majority of replicas are up and available, otherwise the operation will fail

#### Coordinator-Based Approaches:

Without a coordinator, you can have concurrent conflicting writes:

```
Time    Client A         Client B         Replica 1    Replica 2    Replica 3
----    --------         --------         ---------    ---------    ---------
t1      Write X=1   →                     X=1          X=1
t2                       Write X=2   →                              X=2
t3                                                     X=2          
t4      Read X      ←                     X=1          X=2          X=2
        (gets X=1 or X=2, inconsistent!)
```

Even with quorum (W=2, R=2), you might read inconsistent values because writes happened concurrently.


How a Coordinator Helps
A coordinator/leader serializes operations for each piece of data:

```
Time    Client A         Client B         Leader       Replica 2    Replica 3
----    --------         --------         ------       ---------    ---------
t1      Write X=1   →    
t2                       Write X=2   →    
t3                                        Process X=1
t4                                        X=1      →   X=1          X=1
t5                                        Process X=2
t6                                        X=2      →   X=2          X=2
t7      Read X      ←                     Returns X=2 (consistent!)
```

Key benefits:

- All writes go through the leader
- Leader decides the sequence: "X=1 happened before X=2"
- All replicas apply changes in the same order
- No conflicting versions to reconcile


### Read Repair and Merkle tree:

Even if we use a coordinator like above, replicas can still be out of sync

1. Replica Temporarily Down During Writes

```
Time    Client A         Leader       Replica 2    Replica 3
----    --------         ------       ---------    ---------
t1      Write X=1   →    
t2                       X=1      →   X=1          💥 (crashed)
t3      Write X=2   →    
t4                       X=2      →   X=2          (still down)
t5                                                 ⚡ (recovers)
t6                                    X=2          X=1 (out of sync!)
```

Result: Replica 3 missed X=2 and is now permanently out of sync until repaired.

2. Network Partition During Replication

```
Time    Client A         Leader       Replica 2    Replica 3
----    --------         ------       ---------    ---------
t1      Write X=1   →    
t2                       X=1      →   X=1          X=1
t3      Write X=2   →    
t4                       X=2      →   X=2          ❌ (network split)
t5                       (commits with 2/3 quorum)
t6      Write X=3   →    
t7                       X=3      →   X=3          ❌ (still partitioned)
t8                                                 🔗 (partition heals)
t9                                    X=3          X=1 (missing X=2, X=3!)
```

Result: Replica 3 is multiple writes behind.