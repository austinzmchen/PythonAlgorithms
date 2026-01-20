## Wide rows example

```
CREATE TABLE user_stats (
    user_id text,
    stat_name text,
    stat_value counter,
    PRIMARY KEY (user_id, stat_name)
);

UPDATE user_stats SET stat_value = stat_value + 1 
WHERE user_id = 'user123' AND stat_name = 'page_views';

UPDATE user_stats SET stat_value = stat_value + 1 
WHERE user_id = 'user123' AND stat_name = 'clicks';

UPDATE user_stats SET stat_value = stat_value + 5 
WHERE user_id = 'user123' AND stat_name = 'purchases';
```

`user_id` is the partition key (what Cassandra uses to distribute data), and `stat_name` is clustering columns (they determine sort order within a partition).

Now when you query:

```
SELECT * FROM user_stats WHERE user_id = 'user123';
```

You get one logical row for user123, but it could have thousands of different stat_name columns. Each stat becomes essentially a column in that wide row.


### In a relational database:

```
CREATE TABLE user_stats (
    user_id VARCHAR(50),
    stat_name VARCHAR(50),
    stat_value INT,
    PRIMARY KEY (user_id, stat_name)
);
```

The data would look like:
```
| user_id  | stat_name   | stat_value |
|----------|-------------|------------|
| user123  | page_views  | 150        |
| user123  | clicks      | 75         |
| user123  | purchases   | 5          |
| user123  | downloads   | 20         |
```