class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = bin(int(a, 2) + int(b, 2))[2:]
        return result


a = "11"
b = "1"
sol = Solution()
print(sol.addBinary(a, b))
