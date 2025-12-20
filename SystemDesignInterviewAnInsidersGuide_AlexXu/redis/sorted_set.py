import redis
import time
import json
from typing import List, Tuple, Optional

class FrequencyQueue:
    """
    Frequency-based queue using Redis Sorted Sets.
    Items are ordered by their frequency/priority score.
    """
    
    def __init__(self, redis_client: redis.Redis, queue_name: str):
        self.redis = redis_client
        self.queue_name = queue_name
    
    def add_item(self, item: str, initial_frequency: float = 0) -> bool:
        """Add item to queue with initial frequency"""
        result = self.redis.zadd(
            self.queue_name, 
            {item: initial_frequency},
            nx=True  # Only add if doesn't exist
        )
        return result > 0
    
    # def increment_frequency(self, item: str, amount: float = 1) -> float:
    #     """Increment item's frequency"""
    #     new_score = self.redis.zincrby(self.queue_name, amount, item)
    #     return float(new_score)
    
    # def decrement_frequency(self, item: str, amount: float = 1) -> float:
    #     """Decrement item's frequency"""
    #     new_score = self.redis.zincrby(self.queue_name, -amount, item)
    #     return float(new_score)
    
    def get_frequency(self, item: str) -> Optional[float]:
        """Get current frequency of an item"""
        score = self.redis.zscore(self.queue_name, item)
        return float(score) if score is not None else None
    
    # def pop_most_frequent(self, count: int = 1) -> List[Tuple[str, float]]:
    #     """Remove and return most frequent items"""
    #     return self.redis.zpopmax(self.queue_name, count)
    
    # def pop_least_frequent(self, count: int = 1) -> List[Tuple[str, float]]:
    #     """Remove and return least frequent items"""
    #     return self.redis.zpopmin(self.queue_name, count)
    
    # def peek_most_frequent(self, count: int = 10) -> List[Tuple[str, float]]:
    #     """View most frequent items without removing"""
    #     return self.redis.zrevrange(self.queue_name, 0, count - 1, withscores=True)
    
    # def peek_least_frequent(self, count: int = 10) -> List[Tuple[str, float]]:
    #     """View least frequent items without removing"""
    #     return self.redis.zrange(self.queue_name, 0, count - 1, withscores=True)
    
    # def get_rank(self, item: str, reverse: bool = True) -> Optional[int]:
    #     """Get item's rank (0-based). If reverse=True, highest frequency = rank 0"""
    #     if reverse:
    #         rank = self.redis.zrevrank(self.queue_name, item)
    #     else:
    #         rank = self.redis.zrank(self.queue_name, item)
    #     return rank
    
    # def get_items_in_range(self, min_freq: float, max_freq: float) -> List[Tuple[str, float]]:
    #     """Get items with frequency in specified range"""
    #     return self.redis.zrangebyscore(self.queue_name, min_freq, max_freq, withscores=True)
    
    # def remove_item(self, item: str) -> bool:
    #     """Remove specific item from queue"""
    #     result = self.redis.zrem(self.queue_name, item)
    #     return result > 0
    
    def size(self) -> int:
        """Get total number of items in queue"""
        return self.redis.zcard(self.queue_name)
    
    def clear(self) -> bool:
        """Clear entire queue"""
        return self.redis.delete(self.queue_name) > 0


# ============================================
# Example Usage & Demonstrations
# ============================================

def main():
    # Connect to Redis
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    
    print("=" * 70)
    print("FREQUENCY-BASED QUEUE EXAMPLES")
    print("=" * 70)
    
    # ============================================
    # Example 1: Word Frequency Counter
    # ============================================
    print("\n📊 Example 1: WORD FREQUENCY COUNTER")
    print("-" * 70)
    
    word_queue = FrequencyQueue(r, 'word:frequency')
    word_queue.clear()  # Clean start
    
    # Simulate processing text and counting words
    text = "python redis redis python python database redis cache cache python"
    words = text.split()
    
    print(f"Processing text: '{text}'")
    print("\nAdding words and updating frequencies...")
    
    for word in words:
        if not word_queue.add_item(word, initial_frequency=0):
            # Word already exists, increment
            word_queue.increment_frequency(word)
        else:
            # First occurrence, set to 1
            word_queue.increment_frequency(word)
    
    # Show most frequent words
    print("\nMost frequent words:")
    top_words = word_queue.peek_most_frequent(5)
    for rank, (word, freq) in enumerate(top_words, 1):
        print(f"  {rank}. '{word}': {int(freq)} occurrences")
    
    # ============================================
    # Example 2: Task Scheduling by Priority
    # ============================================
    print("\n\n⚡ Example 2: TASK SCHEDULING BY PRIORITY")
    print("-" * 70)
    
    task_queue = FrequencyQueue(r, 'tasks:priority')
    task_queue.clear()
    
    # Add tasks with initial priority
    tasks = {
        'send_notifications': 5,
        'backup_database': 2,
        'process_payments': 10,
        'generate_reports': 3,
        'clean_logs': 1
    }
    
    print("Adding tasks with priorities:")
    for task, priority in tasks.items():
        task_queue.add_item(task, priority)
        print(f"  - {task}: priority {priority}")
    
    # Process high priority tasks
    print("\n🔥 Processing top 3 priority tasks:")
    for i in range(3):
        task_data = task_queue.pop_most_frequent(1)
        if task_data:
            task, priority = task_data[0]
            print(f"  {i+1}. Processing '{task}' (priority: {int(priority)})")
    
    print("\nRemaining tasks:")
    remaining = task_queue.peek_most_frequent(10)
    for task, priority in remaining:
        print(f"  - {task}: priority {int(priority)}")
    
    # ============================================
    # Example 3: API Rate Tracking
    # ============================================
    print("\n\n📡 Example 3: API ENDPOINT USAGE TRACKING")
    print("-" * 70)
    
    api_queue = FrequencyQueue(r, 'api:usage')
    api_queue.clear()
    
    # Simulate API calls
    endpoints = [
        '/api/users', '/api/posts', '/api/users', '/api/comments',
        '/api/users', '/api/posts', '/api/users', '/api/login',
        '/api/users', '/api/posts', '/api/posts', '/api/users'
    ]
    
    print("Tracking API endpoint calls...")
    for endpoint in endpoints:
        if not api_queue.add_item(endpoint, 0):
            api_queue.increment_frequency(endpoint)
        else:
            api_queue.increment_frequency(endpoint)
    
    print("\nMost called endpoints:")
    top_endpoints = api_queue.peek_most_frequent(5)
    for rank, (endpoint, calls) in enumerate(top_endpoints, 1):
        print(f"  {rank}. {endpoint}: {int(calls)} calls")
    
    # Get rank of specific endpoint
    rank = api_queue.get_rank('/api/posts')
    print(f"\n'/api/posts' is ranked #{rank + 1} in usage")
    
    # ============================================
    # Example 4: Product Popularity Tracker
    # ============================================
    print("\n\n🛒 Example 4: PRODUCT POPULARITY TRACKER")
    print("-" * 70)
    
    product_queue = FrequencyQueue(r, 'products:popularity')
    product_queue.clear()
    
    # Add products
    products = ['laptop', 'mouse', 'keyboard', 'monitor', 'webcam']
    for product in products:
        product_queue.add_item(product, 0)
    
    print("Simulating product views and purchases...")
    
    # Simulate user interactions
    interactions = [
        ('laptop', 5),    # 5 views
        ('mouse', 10),    # 10 views
        ('laptop', 3),    # 3 more views
        ('keyboard', 7),
        ('mouse', 5),
        ('monitor', 2),
        ('laptop', 8),
        ('webcam', 1)
    ]
    
    for product, views in interactions:
        product_queue.increment_frequency(product, views)
        current = product_queue.get_frequency(product)
        print(f"  {product}: +{views} views (total: {int(current)})")
    
    print("\n🔥 Trending products:")
    trending = product_queue.peek_most_frequent(5)
    for rank, (product, score) in enumerate(trending, 1):
        print(f"  {rank}. {product}: {int(score)} total interactions")
    
    # Find products with moderate popularity (5-15 interactions)
    print("\nProducts with 5-15 interactions:")
    moderate = product_queue.get_items_in_range(5, 15)
    for product, score in moderate:
        print(f"  - {product}: {int(score)}")
    
    # ============================================
    # Example 5: Dynamic Cache Management
    # ============================================
    print("\n\n💾 Example 5: LFU (Least Frequently Used) CACHE")
    print("-" * 70)
    
    cache_queue = FrequencyQueue(r, 'cache:lfu')
    cache_queue.clear()
    
    # Cache with max size
    MAX_CACHE_SIZE = 5
    
    def access_cache_item(item: str):
        """Access a cache item and update its frequency"""
        if cache_queue.get_frequency(item) is None:
            # Item not in cache
            if cache_queue.size() >= MAX_CACHE_SIZE:
                # Cache full, evict least frequently used
                evicted = cache_queue.pop_least_frequent(1)
                if evicted:
                    print(f"  🗑️  Evicted '{evicted[0][0]}' (frequency: {int(evicted[0][1])})")
            
            cache_queue.add_item(item, 0)
            print(f"  ➕ Added '{item}' to cache")
        
        # Increment access count
        new_freq = cache_queue.increment_frequency(item)
        print(f"  ✓  Accessed '{item}' (frequency: {int(new_freq)})")
    
    # Simulate cache accesses
    print(f"Cache size limit: {MAX_CACHE_SIZE}\n")
    
    access_sequence = [
        'page_home', 'page_about', 'page_home', 'page_products',
        'page_home', 'page_contact', 'page_blog', 'page_home',
        'page_products', 'page_help'  # This will cause evictions
    ]
    
    for item in access_sequence:
        access_cache_item(item)
    
    print("\nFinal cache state (most to least frequent):")
    cache_items = cache_queue.peek_most_frequent(10)
    for rank, (item, freq) in enumerate(cache_items, 1):
        print(f"  {rank}. {item}: {int(freq)} accesses")
    
    # ============================================
    # Example 6: Weighted Job Queue
    # ============================================
    print("\n\n⚙️  Example 6: WEIGHTED JOB QUEUE")
    print("-" * 70)
    
    job_queue = FrequencyQueue(r, 'jobs:weighted')
    job_queue.clear()
    
    # Add jobs with weights (importance scores)
    jobs = {
        'process_payments': 100,
        'send_email': 50,
        'resize_images': 20,
        'cleanup_temp': 10,
        'update_stats': 30
    }
    
    print("Jobs with weights:")
    for job, weight in jobs.items():
        job_queue.add_item(job, weight)
        print(f"  - {job}: weight {weight}")
    
    # Adjust weights based on system conditions
    print("\n⚠️  System alert: Email service delayed, boosting priority...")
    new_weight = job_queue.increment_frequency('send_email', 50)
    print(f"'send_email' weight: {int(new_weight)}")
    
    print("\n✓ Payment processing completed, reducing priority...")
    new_weight = job_queue.decrement_frequency('process_payments', 30)
    print(f"'process_payments' weight: {int(new_weight)}")
    
    print("\nUpdated job priorities:")
    all_jobs = job_queue.peek_most_frequent(10)
    for rank, (job, weight) in enumerate(all_jobs, 1):
        print(f"  {rank}. {job}: weight {int(weight)}")
    
    print("\n" + "=" * 70)
    print("✅ All examples completed!")
    print("=" * 70)


if __name__ == "__main__":
    main()