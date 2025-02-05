class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue, visit = deque(), set()
        queue.append((start))

        while queue:
            pos = queue.popleft()

            if arr[pos] == 0:
                return True

            if pos not in visit:
                visit.add((pos))

                if pos + arr[pos] < len(arr):
                    queue.append((pos + arr[pos]))

                if pos - arr[pos] >= 0:
                    queue.append((pos - arr[pos]))

        return False