# Bottom line: Use enable_auto_commit=False and manual commit() 
# for most cases where you want control over when messages are considered "consumed."

from kafka import KafkaConsumer, TopicPartition
import json

# Disable auto-commit
consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    group_id='my-group',
    enable_auto_commit=False,  # Don't auto-commit offsets
    auto_offset_reset='earliest'
)

def process_message(data):
    """Override this method to implement custom message processing"""
    print(f"Processing: {data['type']} - {data['content']}")

# Read messages without consuming
for i, message in enumerate(consumer):
    print(f"Read message: {message.value}")
    print(f"Offset: {message.offset}")
    
    # Process the message
    result = process_message(message.value)
    
    # Only commit if processing succeeds
    if result == 'success':
        consumer.commit()  # Now the message is "consumed"
        print(f"Message consumed (offset committed)")
    else:
        print(f"Message NOT consumed (offset not committed)")
        # On restart, will re-read this message
        break
    
consumer.close()

# Next time this consumer starts, it will re-read uncommitted messages