class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue, visit = deque(), set()
        queue.append((startGene, 0))
        visit.add((startGene))       

        while queue:
            node, turns = queue.popleft()
            if node == endGene:
                return turns
            
            for c in "ACGT":
                for i in range(len(node)):
                    digit = node[:i] + c + node[i+1:]
                    if digit not in visit and digit in bank:
                        queue.append((digit, turns + 1))
                        visit.add((digit))

        return -1