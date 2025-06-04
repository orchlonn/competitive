class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[-1])
        count = 0

        for boxType in boxTypes:
            print(boxType)
            boxCount = min(truckSize, boxType[0])
            count += boxCount * boxType[1]
            truckSize -= boxCount

            if truckSize == 0:
                break
        
        return count 

# Time complexity: O(N logN)
# Space complexity: O(N)