import heapq

class Median:
    def __init__(self):
        self.small, self.large = [], []
    
    def insert(self, num):
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        # Handle uneven size
        if len(self.large) - len(self.small) > 1:
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        elif len(self.small) - len(self.large) > 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)
    
    def getMedian(self):
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0] ) / 2