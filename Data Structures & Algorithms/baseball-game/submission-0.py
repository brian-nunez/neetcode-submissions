from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack: List[int] = []

        for operation in operations:
            match operation:
                case "+":
                    stack.append(stack[-1] + stack[-2])
                case "C":
                    stack.pop()
                case "D":
                    stack.append(stack[-1] * 2)
                case _:
                    stack.append(int(operation))

        return sum(stack)
