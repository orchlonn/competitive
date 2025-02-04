class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = [start]
        visit = set()

        while queue:
            pos = queue.pop()
            jump = arr[pos]

            if jump == 0:
                return True
            
            if pos not in visit:
                visit.add((pos))
                if pos + jump < len(arr):
                    queue.append(pos + jump)
                if pos - jump >= 0:
                    queue.append(pos - jump)
            
        return False