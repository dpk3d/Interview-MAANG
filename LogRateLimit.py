# Write a function to reduce noisy log ingestion into actual logging system.
# The rate limit should be based on exact messages occurance, X as a threshold
# in given time window , rolling manner 

from collections import defaultdict , deque 
import time 

class LogRateLimit:
    
    def __init__(self, max_count : int, window:int ):
        self.max_count = max_count
        self.window = window
        self.time = defaultdict(deque)
    

    def should_allow(self, msg : str, timestamp: int) :
        q = self.time[msg]
        while q and q[0] < timestamp - self.window :
            q.popleft()
        
        if len (q) < self.max_count:
            q.append(timestamp)
            return True
        else :
            return False
    


if __name__ == "__main__":
    limiter = LogRateLimit(max_count = 3 ,window = 5)
    
    logs = [    (1, 'DB Error'),
    (2, 'DB Error'),
    (3, 'DB Error'),
    (4, 'DB Error'),
    (500, 'DB Error')
    ]

for k , v in logs:
    result = 'allow' if limiter.should_allow(v,k) else 'deny'
    print(f'{k:>2} | {v: <10} | {result}')


#### Output
# 1 | DB Error   | allow
# 2 | DB Error   | allow
# 3 | DB Error   | allow
# 4 | DB Error   | deny
# 5 | DB Error   | allow

=== Code Execution Successful ===
