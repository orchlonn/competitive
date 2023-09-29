class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        max_counter = Counter()
        low_counter = Counter()

        if len(s) >= len(t):
            max_counter = Counter(s)
            low_counter = Counter(t)

        if len(s) <= len(t):
            max_counter = Counter(t)
            low_counter = Counter(s)
        
        cntr = 0
        for i in max_counter:
            if i in low_counter and max_counter[i] == low_counter[i]:
                cntr += 1

        return True if cntr == len(max_counter) else False