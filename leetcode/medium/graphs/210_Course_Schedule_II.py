class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        visit, cycle = set(), set()
        output = []

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
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return output

# Time complexity: O(P + N) where P is number of prerequisites and N is numCourse

# Solution #2: Topological sort (DFS)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        visited = set()
        visiting = set()
        topSort = []

        def dfs(crs):
            if crs in visited:
                return True
            if crs in visiting:
                return False
            
            visiting.add(crs)
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            
            visiting.remove(crs)
            visited.add(crs)
            topSort.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []

        return topSort

# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
