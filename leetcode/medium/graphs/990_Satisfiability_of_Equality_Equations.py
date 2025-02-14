class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parents = [i for i in range(26)]
        
        def ufind(x):
            if parents[x] != x:
                parents[x] = ufind(parents[x])
            return parents[x]
        
        def uunion(a, b):
            ua = ufind(a)
            ub = ufind(b)

            parents[ua] = ub
        
        for equation in equations:
            if equation[1] == '!':
                continue
            
            a = ord(equation[0]) - ord('a')
            b = ord(equation[3]) - ord('a')
            
            uunion(a, b)

        for equation in equations:
            if equation[1] != '!':
                continue
            a = ord(equation[0]) - ord('a')
            b = ord(equation[3]) - ord('a')
            print(a, b)
            
            if ufind(a) == ufind(b):
                return False
            
        return True
        