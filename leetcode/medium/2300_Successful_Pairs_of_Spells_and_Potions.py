class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binary_search(arr, target):
            l, r = 0, len(arr) - 1

            while l <= r:
                mid = (l + r) // 2
                if arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return l
        
        potions.sort()
        ans = []
        potionsLength = len(potions)

        for spell in spells:
            n = binary_search(potions, success / spell)
            ans.append(potionsLength - n)

        return ans