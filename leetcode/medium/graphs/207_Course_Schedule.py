# Solution 1: Cycle detection (DFS):
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return False
        
        return True


# Topological Sort (DFS):
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        visited = set()
        visiting = set()
        
        def dfs(crs):
            if crs in visited:
                return True
            if crs in visiting:
                return False
            
            visiting.add(crs)

            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            
            visited.add(crs)
            visiting.remove(crs)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

# Time Complexity: O(V + E)
# Space Complexity: O(V + E)


