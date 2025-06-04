class Solution:
    def maximum69Number (self, num: int) -> int:
        num_string = str(num)

        return int(num_string.replace('6', '9', 1))