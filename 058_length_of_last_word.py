class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()
        return len(word[-1])


s = "luffy is still joyboy"
sol = Solution()
print(sol.lengthOfLastWord(s))
