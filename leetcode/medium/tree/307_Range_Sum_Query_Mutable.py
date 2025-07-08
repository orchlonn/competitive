# Solution #1: Brute force
class NumArray:

    def __init__(self, nums: List[int]):
        self.numbers = nums

    def update(self, index: int, val: int) -> None:
        self.numbers[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.numbers[left:right + 1])


# Solution #2: (Segment tree)
class SegmentTree:
    def __init__(self, nums, L, R):
        self.L = L
        self.R = R

        if L == R:
            self.sum = nums[L]
            self.left = self.right = None
        else:
            M = (L + R) // 2
            self.left = SegmentTree(nums, L, M)
            self.right = SegmentTree(nums, M + 1, R)
            self.sum = self.right.sum + self.left.sum

    def update(self, index, val):
        if self.L == self.R:
            self.sum = val
            return
        
        if index <= self.left.R:
            self.left.update(index, val)
        else:
            self.right.update(index, val)
        
        self.sum = self.left.sum + self.right.sum
    
    def query_range(self, L, R):
        if L == self.L and self.R == R:
            return self.sum
        
        M = (self.L + self.R) // 2

        if L > M:
            return self.right.query_range(L, R)
        elif M >= R:
            return self.left.query_range(L, R)
        else:
            return (self.left.query_range(L, M) + self.right.query_range(M + 1, R))
        

class NumArray:

    def __init__(self, nums):
        if nums:
            self.root = SegmentTree(nums, 0, len(nums) - 1)
        else:
            self.root = None

    def update(self, index, val):
        if self.root:
            self.root.update(index, val)

    def sumRange(self, left, right):
        if self.root:
            return self.root.query_range(left, right)