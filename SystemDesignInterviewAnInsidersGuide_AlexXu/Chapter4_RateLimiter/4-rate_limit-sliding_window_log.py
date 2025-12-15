import time
from threading import Lock
from collections import defaultdict, deque

class SlidingWindowLog:
    """
    Sliding window log algorithm for rate limiting.
    
    Maintains a log of request timestamps and counts requests within
    a sliding time window. Provides precise rate limiting without the
    burst problem of fixed windows.
    """
    
    def __init__(self, max_requests, window_size):
        """
        Initialize the sliding window log.
        
        Args:
            max_requests: Maximum number of requests allowed in the window
            window_size: Size of the sliding window in seconds
        """
        self.max_requests = max_requests
        self.window_size = window_size
        self.request_log = deque()
        # self.user_logs = defaultdict(deque) # for multi user
        self.lock = Lock()
    
    def _remove_old_requests(self):
        """Remove requests outside the current window."""
        now = time.time()
        cutoff = now - self.window_size
        
        # Remove timestamps older than the window
        while self.request_log and self.request_log[0] <= cutoff:
            self.request_log.popleft()
    
    def allow_request(self):
        """
        Check if a request should be allowed.
        
        Returns:
            bool: True if request is allowed, False if limit exceeded
        """
        with self.lock:
            self._remove_old_requests()
            
            if len(self.request_log) < self.max_requests:
                self.request_log.append(time.time())
                return True
            return False
    
    def get_remaining(self):
        """Get remaining requests in current window."""
        with self.lock:
            self._remove_old_requests()
            return max(0, self.max_requests - len(self.request_log))
    
    def get_request_count(self):
        """Get current number of requests in the window."""
        with self.lock:
            self._remove_old_requests()
            return len(self.request_log)
    
    def get_oldest_request_age(self):
        """Get age of oldest request in seconds (None if empty)."""
        with self.lock:
            self._remove_old_requests()
            if not self.request_log:
                return None
            return time.time() - self.request_log[0]


# Example usage
if __name__ == "__main__":
    print("=== Sliding Window Log Demo ===")
    limiter = SlidingWindowLog(max_requests=5, window_size=3)
    
    print(f"Limit: 5 requests per 3-second sliding window")
    print("Note: Unlike fixed window, this prevents burst at boundaries\n")
    
    # Simulate requests
    for i in range(12):
        allowed = limiter.allow_request()
        remaining = limiter.get_remaining()
        count = limiter.get_request_count()
        oldest_age = limiter.get_oldest_request_age()
        
        status = "✓ Allowed" if allowed else "✗ Rejected"
        age_str = f"{oldest_age:.1f}s" if oldest_age else "N/A"
        print(f"Request {i+1}: {status} | In window: {count}/5 | Remaining: {remaining} | Oldest: {age_str}")
        time.sleep(0.5)