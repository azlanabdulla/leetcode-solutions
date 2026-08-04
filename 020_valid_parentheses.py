class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if char == ")" and last != "(":
                    return False
                if char == "]" and last != "[":
                    return False
                if char == "}" and last != "{":
                    return False
        return len(stack) == 0


sol = Solution()
print(sol.isValid("[()]"))
