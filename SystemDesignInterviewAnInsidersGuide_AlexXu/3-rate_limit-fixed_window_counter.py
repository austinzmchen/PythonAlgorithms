import time
from threading import Lock

class FixedWindowCounter:
    """
    Fixed window counter algorithm for rate limiting.
    
    Divides time into fixed windows and counts requests in each window.
    When a window expires, the counter resets to zero.
    """
    
    def __init__(self, max_requests, window_size: int):
        """
        Initialize the fixed window counter.
        
        Args:
            max_requests: Maximum number of requests allowed per window
            window_size: seconds
        """
        self.max_requests = max_requests
        self.window_size = window_size
        self.counter = 0
        # self.counters = defaultdict(lambda: {'count': 0, 'window': 0}) # for multi user
        self.window_start = time.time()
        self.lock = Lock()
    
    def _get_current_window(self):
        """Get the current window start time."""
        now = time.time()
        return int(now // self.window_size) * self.window_size # remove fractions by radix of window_size
    
    def _reset_if_new_window(self):
        """Reset counter if we've moved to a new window."""
        current_window = self._get_current_window()
        if current_window > self.window_start:
            self.counter = 0
            self.window_start = current_window
    
    def allow_request(self):
        """
        Check if a request should be allowed.
        
        Returns:
            bool: True if request is allowed, False if limit exceeded
        """
        with self.lock:
            self._reset_if_new_window()
            
            if self.counter < self.max_requests:
                self.counter += 1
                return True
            return False
    
    def get_remaining_reqs(self) -> int:
        """Get remaining requests in current window."""
        with self.lock:
            self._reset_if_new_window()
            return max(0, self.max_requests - self.counter)
    
    def get_reset_time(self) -> int:
        """Get seconds until the window resets."""
        with self.lock:
            current_window = self._get_current_window()
            next_window = current_window + self.window_size
            return next_window - time.time()


# Example usage
if __name__ == "__main__":
    print("=== Fixed Window Counter Demo ===")
    limiter = FixedWindowCounter(max_requests=5, window_size=3)
    
    print(f"Limit: 5 requests per 3-second window\n")
    
    # Simulate requests
    for i in range(10):
        allowed = limiter.allow_request()
        remaining = limiter.get_remaining_reqs()
        reset_time = limiter.get_reset_time()
        
        status = "✓ Allowed" if allowed else "✗ Rejected"
        print(f"Request {i+1}: {status} | Remaining: {remaining} | Reset in: {reset_time:.1f}s")
        time.sleep(0.5)