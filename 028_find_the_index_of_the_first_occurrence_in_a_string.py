class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return int(haystack.find(needle))


haystack = "sadbutsad"
needle = "sad"
sol = Solution()
print(sol.strStr(haystack, needle))
