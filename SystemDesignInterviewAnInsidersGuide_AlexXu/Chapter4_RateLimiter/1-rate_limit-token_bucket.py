import time
from threading import Lock

class TokenBucket:
    """
    Token bucket algorithm for rate limiting in application code,
    For distributed token bucket code in API gateway middleware, better to save states in redis cache
    
    Tokens are added at a fixed rate. Each request consumes tokens.
    If insufficient tokens are available, the request is rejected.
    """
    
    def __init__(self, capacity, refill_rate: int):
        """
        Initialize the token bucket.
        
        Args:
            capacity: Maximum number of tokens the bucket can hold
            refill_rate: Number of tokens added per second
        """
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill = time.time()
        self.lock = Lock()
    
    def _refill_if_needed(self):
        """Refill tokens based on time elapsed since last refill."""
        now = time.time()
        elapsed = now - self.last_refill
        tokens_to_add = elapsed * self.refill_rate # accumulative
        self.tokens = min(self.capacity, self.tokens + tokens_to_add)
        self.last_refill = now
    
    def consume(self, tokens=1):
        """
        Attempt to consume tokens from the bucket.
        
        Args:
            tokens: Number of tokens to consume (default: 1)
            
        Returns:
            bool: True if tokens were consumed, False if insufficient tokens
        """
        with self.lock:
            self._refill_if_needed()
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False
    
    def get_tokens(self):
        """Get current number of tokens (for monitoring)."""
        with self.lock:
            self._refill_if_needed()
            return self.tokens


# Example usage
if __name__ == "__main__":
    # Create a bucket with capacity of 4 tokens, refilling at 2 tokens/second
    bucket = TokenBucket(capacity=4, refill_rate=2)
    
    print("Token Bucket Rate Limiter Demo")
    print(f"Capacity: 10 tokens, Refill rate: 2 tokens/second\n")
    
    # Simulate requests
    for i in range(15):
        if bucket.consume(): # called by different threads
            print(f"Request {i+1}: ✓ Allowed (tokens: {bucket.get_tokens():.2f})")
        else:
            print(f"Request {i+1}: ✗ Rejected (tokens: {bucket.get_tokens():.2f})")
        time.sleep(0.2)  # Small delay between requests
    
    print("\nWaiting 3 seconds for bucket to refill...")
    time.sleep(3)
    
    print(f"Tokens after waiting: {bucket.get_tokens():.2f}")
    if bucket.consume():
        print("New request: ✓ Allowed")