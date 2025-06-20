class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        ordered = sorted(counter.values(), reverse=True)

        while k > 0:
            value = ordered[-1]
            if k >= value:
                k -= value
                ordered.pop()
            else:
                break
        
        return len(ordered)
        
# Time Complexity: O(n log n) [Because of sorting algorithm]
# Space Complexity: O(n)