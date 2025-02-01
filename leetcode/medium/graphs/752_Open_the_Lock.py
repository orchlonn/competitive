class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1 
            
        def children(locks):
            res = []
            for i in range(4):
                digit = str((int(locks[i]) + 1) % 10)
                res.append(locks[:i] + digit + locks[i+1:])
                digit = str((int(locks[i]) - 1 + 10) % 10)
                res.append(locks[:i] + digit + locks[i+1:])
            
            return res
            
        q = deque([("0000", 0)])
        visit = set((deadends))
        
        while q:
            locks, turns = q.popleft()
            
            if locks == target:
                return turns
            
            for child in children(locks):
                if child not in visit:
                    visit.add((child))
                    q.append((child, turns + 1))
        
        return -1