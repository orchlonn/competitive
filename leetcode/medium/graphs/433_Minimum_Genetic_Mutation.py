class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([(startGene, 0)])
        visit = set((startGene))
        
        while queue:
            string, steps = queue.popleft()
            if string == endGene:
                return steps
            
            for c in "ACGT":
                for i in range(len(string)):
                    neighbor = string[:i] + c + string[i + 1:]
                    if neighbor not in visit and neighbor in bank:
                        queue.append((neighbor, steps + 1))
                        visit.add((neighbor))
                        
        return -1
