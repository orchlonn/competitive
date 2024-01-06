from collections import deque 

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.sum_window = 0
        self.counter = 0
        self.queue = deque()

    def next(self, val: int) -> float:
        self.counter += 1
        self.queue.append(val)
        
        tail = self.queue.popleft() if self.counter > self.size else 0
        
        self.sum_window = self.sum_window - tail + val        

        return self.sum_window / min(self.size, self.counter)