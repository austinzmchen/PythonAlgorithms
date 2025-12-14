import time

# ============================================================================
# fixed window counter algo
# ============================================================================

class SimpleRateLimiter:
    """
    Basic rate limiter using Redis INCR and EXPIRE.
    
    Uses fixed window counter algorithm:
    - Key format: ratelimit:{user_id}:{window_start}
    - INCR increments the counter atomically
    - EXPIRE sets TTL on first request in window
    """
    
    def __init__(self, redis_client, max_requests=10, window_seconds=60):
        """
        Initialize rate limiter.
        
        Args:
            redis_client: Redis client instance
            max_requests: Maximum requests allowed per window
            window_seconds: Time window in seconds
        """
        self.redis = redis_client
        self.max_requests = max_requests
        self.window_seconds = window_seconds
    
    def is_allowed(self, user_id):
        """
        Check if request is allowed for user.
        
        Args:
            user_id: Unique identifier for the user
            
        Returns:
            tuple: (allowed: bool, remaining: int, reset_time: int)
        """
        # Create key with current window timestamp
        current_window = int(time.time() // self.window_seconds)
        key = f"ratelimit:{user_id}:{current_window}"
        
        # Increment counter
        current_count = self.redis.incr(key)
        
        # Set expiry on first request (when count becomes 1)
        if current_count == 1:
            self.redis.expire(key, self.window_seconds)
        
        # Check if limit exceeded
        allowed = current_count <= self.max_requests
        remaining = max(0, self.max_requests - current_count)
        reset_time = (current_window + 1) * self.window_seconds # unix time
        
        return allowed, remaining, reset_time
    
    def get_info(self, user_id):
        """Get current rate limit info for user."""
        current_window = int(time.time() // self.window_seconds)
        key = f"ratelimit:{user_id}:{current_window}"
        
        count = self.redis.get(key)
        count = int(count) if count else 0
        ttl = self.redis.ttl(key)
        
        return {
            'current_count': count,
            'limit': self.max_requests,
            'remaining': max(0, self.max_requests - count),
            'reset_in_seconds': ttl if ttl > 0 else self.window_seconds
        }

# ============================================================================
# SLIDING WINDOW LOG - More accurate using sorted sets
# ============================================================================

class SlidingWindowRateLimiter:
    """
    Sliding window rate limiter using Redis sorted sets.
    More accurate than fixed window, prevents boundary bursts.
    
    Redis sorted set data structure (ZSET)
    
    ┌─────────────────────┬──────────────────────────────────────────┐
    │ Command             │ What it does                             │
    ├─────────────────────┼──────────────────────────────────────────┤
    │ ZADD                │ Add/update members with scores           │
    │ ZREMRANGEBYSCORE    │ Remove members by score range            │
    │ ZREMRANGEBYRANK     │ Remove members by rank range             │
    │ ZREM                │ Remove specific members                  │
    │ ZCARD               │ Count total members                      │
    │ ZCOUNT              │ Count members in score range             │
    │ ZRANGE              │ Get members by rank (low to high)        │
    │ ZREVRANGE           │ Get members by rank (high to low)        │
    │ ZRANGEBYSCORE       │ Get members by score range               │
    └─────────────────────┴──────────────────────────────────────────┘
    """
    
    def __init__(self, redis_client, max_requests=10, window_seconds=60):
        self.redis = redis_client
        self.max_requests = max_requests
        self.window_seconds = window_seconds
    
    
    def is_allowed(self, user_id):
        key = f"ratelimit:sliding:{user_id}"
        now = time.time()
        window_start = now - self.window_seconds
        
        # Remove old entries outside the window
        self.redis.zremrangebyscore(key, 0, window_start) # z remove range [0, X]
        
        # Count requests in current window
        current_count = self.redis.zcard(key) # z count set members
        
        if current_count < self.max_requests:
            # Add current request with timestamp as score
            self.redis.zadd(key, {str(now): now}) # add to set of a key-value pair, create the set if not exists
            self.redis.expire(key, self.window_seconds)
            allowed = True
            remaining = self.max_requests - current_count - 1
        else:
            allowed = False
            remaining = 0
        
        return allowed, remaining
    

def rate_limit(max_requests=10, window_seconds=60):
    """
    Decorator for rate limiting functions.
    
    Usage:
        @rate_limit(max_requests=5, window_seconds=60)
        def my_api_endpoint(user_id):
            return "Success"
    """
    import redis
    def decorator(func):
        def wrapper(user_id, *args, **kwargs):
            # Note: In real usage, pass redis_client as parameter or use global
            redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)
            limiter = SimpleRateLimiter(redis_client, max_requests, window_seconds)
            # limiter = SlidingWindowRateLimiter(redis_client, max_requests, window_seconds)
            
            allowed, remaining, reset_time = limiter.is_allowed(user_id)
            if not allowed:
                raise Exception(f"Rate limit exceeded. Try again in {reset_time - int(time.time())}s")
            
            return func(user_id, *args, **kwargs)
        return wrapper
    return decorator