class Solution:
    def isValid(self, s: str) -> bool:
        stack: List[str] = []
    
        for chunk in s:
            if chunk in ("(", "{", "["):
                stack.append(chunk)
                continue

            if len(stack) == 0:
                return False

            if (
                (chunk == ")" and stack[-1] == "(")
                or (chunk == "}" and stack[-1] == "{")
                or (chunk == "]" and stack[-1] == "[")
            ):
                stack.pop()
            else:
                return False
    
        return len(stack) == 0