import time
from threading import Lock
from collections import deque

class LeakyBucket:
    """
    Leaky bucket algorithm for rate limiting.
    
    Requests are added to a bucket with fixed capacity. The bucket "leaks"
    at a constant rate. If the bucket is full, new requests are rejected.
    """
    
    def __init__(self, capacity, leak_rate):
        """
        Initialize the leaky bucket.
        
        Args:
            capacity: Maximum number of requests the bucket can hold
            leak_rate: Number of requests that leak out per second
        """
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.queue = deque()
        self.last_leak = time.time()
        self.lock = Lock()
    
    def _leak(self):
        """Remove (leak) requests based on time elapsed since last leak."""
        now = time.time()
        elapsed = now - self.last_leak
        leaks = int(elapsed * self.leak_rate)
        
        # Remove leaked requests
        for _ in range(min(leaks, len(self.queue))):
            self.queue.popleft()
        self.last_leak = now
    
    def add_request(self):
        """
        Attempt to add a request to the bucket.
        
        Returns:
            bool: True if request was accepted, False if bucket is full
        """
        with self.lock:
            self._leak()
            
            if len(self.queue) < self.capacity:
                self.queue.append(time.time())
                return True
            return False
    
    def get_size(self):
        """Get current number of requests in the bucket."""
        with self.lock:
            self._leak()
            return len(self.queue)


# Example usage
if __name__ == "__main__":
    print("=== Leaky Bucket Demo (Rejection Mode) ===")
    bucket = LeakyBucket(capacity=5, leak_rate=2)
    
    print(f"Capacity: 5 requests, Leak rate: 2 requests/second\n")
    
    # Simulate burst of requests
    for i in range(8):
        if bucket.add_request():
            print(f"Request {i+1}: ✓ Accepted (bucket size: {bucket.get_size()})")
        else:
            print(f"Request {i+1}: ✗ Rejected (bucket full: {bucket.get_size()})")
        time.sleep(0.2)
    
    print(f"\nWaiting 2 seconds for bucket to leak...")
    time.sleep(2)
    print(f"Bucket size after waiting: {bucket.get_size()}")