class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stackNumbers = []
        self.stackOperators = []
        operators = ['+', '-', '*', '/']
        res = 0 

        for c in tokens:
            if c in operators:
                self.stackOperators.append(c)
            else:
                self.stackNumbers.append(c)

            if res == 0 and self.stackOperators:
                print(self.stackNumbers)
                first = int(self.stackNumbers.pop())
                second = int(self.stackNumbers.pop())
                operator = self.stackOperators.pop()
                # print(first, second)
                if operator == '+':
                    res =  second + first
                elif operator == '-':
                    res =  second - first
                elif operator == '*':
                    res =  second * first
                else:
                    res = int(second / first)
            elif self.stackOperators:
                last = int(self.stackNumbers.pop())
                operator = self.stackOperators.pop()
                if operator == '+':
                    res += last
                elif operator == '-':
                    res -= last
                elif operator == '*':
                    res *= last
                else:
                    res = int(last / res)

        return res