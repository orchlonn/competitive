class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = i = 0
        j = len(people) - 1
        people.sort()
        
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            
            ans += 1
            j -= 1
 
        return ans
        
# Time complexity: O(n * log n)
# Space complexity: O(1)