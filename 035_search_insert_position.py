from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0

        for i in nums:
            if i == target:
                return index
            elif i < target:
                index += 1
            else:
                return index

        return index


nums = [1, 3, 5, 6]
target = 5

sol = Solution()
print(sol.searchInsert(nums, target))
