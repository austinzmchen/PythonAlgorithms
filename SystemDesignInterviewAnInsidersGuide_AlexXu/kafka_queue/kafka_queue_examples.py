from kafka import KafkaProducer, KafkaConsumer, TopicPartition
import json
import time

# ============ PRODUCER ============
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    key_serializer=lambda k: k.encode('utf-8'),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Send messages with user_id as key
# All messages for user-123 go to the SAME partition
for i in range(10):
    producer.send(
        topic='user-notifications',
        key='user-123',  # KEY determines partition
        value={
            'notification_id': i,
            'message': f'Notification {i} for user-123',
            'timestamp': time.time()
        }
    )

for i in range(10):
    producer.send(
        topic='user-notifications',
        key='user-456',  # Different key = different partition
        value={
            'notification_id': i,
            'message': f'Notification {i} for user-456',
            'timestamp': time.time()
        }
    )

producer.close()

# ============ CONSUMER (Efficient - reads only relevant partition) ============
# Consumer Reading
# Each partition can only be consumed by one consumer within a consumer group at a time. This means:

# If you have 3 partitions and 3 consumers in a group, each consumer gets 1 partition
# If you have 3 partitions and 5 consumers, 2 consumers will be idle
# If you have 3 partitions and 1 consumer, that consumer reads all 3 partitions

class KeyBasedConsumer:
    def __init__(self, user_id, topic, num_partitions=10):
        self.user_id = user_id
        self.topic = topic
        
        # Calculate which partition this user's messages are in
        self.target_partition = abs(hash(user_id)) % num_partitions
        
        # Create consumer and manually assign the specific partition
        self.consumer = KafkaConsumer(
            bootstrap_servers=['localhost:9092'],
            key_deserializer=lambda k: k.decode('utf-8'),
            value_deserializer=lambda v: json.loads(v.decode('utf-8')),
            group_id=f'user-consumer-{user_id}',
            auto_offset_reset='earliest',
            # enable_auto_commit=False,  # Don't auto-commit offsets
        )
        
        # Assign ONLY the partition containing this user's messages
        partition = TopicPartition(topic, self.target_partition)
        self.consumer.assign([partition])
        
        print(f"User {user_id} reading from partition {self.target_partition} ONLY")
    
    def consume(self):
        for message in self.consumer:
            # ALL messages in this partition are for this user
            # No filtering needed!
            print(f"[{self.user_id}] Received: {message.value['message']}")
            print(f"  - Partition: {message.partition}")
            print(f"  - Offset: {message.offset}")
    
    def close(self):
        self.consumer.close()

# Each user only reads their partition
consumer_123 = KeyBasedConsumer('user-123', 'user-notifications')
consumer_123.consume()