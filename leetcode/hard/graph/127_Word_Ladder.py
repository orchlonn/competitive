class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                graph[pattern].append(word)
        
        queue, visit = deque(), set()
        queue.append((beginWord))
        visit.add((beginWord))
        
        res = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                
                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in graph[pattern]:
                        if nei not in visit:
                            queue.append((nei))
                            visit.add((nei))
            
            res +=1
        
        return 0
                    
                    