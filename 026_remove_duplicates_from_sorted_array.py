from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = []
        duplicate = []
        for i in nums:
            if i in seen:
                duplicate.append(i)
            else:
                seen.append(i)
        for i in duplicate:
            nums.remove(i)
        print(nums)
        return len(nums)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
sol = Solution()
print(sol.removeDuplicates(nums))
