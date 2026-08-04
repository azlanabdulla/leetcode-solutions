from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        return k


# Example
nums = [3, 2, 2, 3]
val = 3

sol = Solution()
k = sol.removeElement(nums, val)
print(k)
print(nums[:k])
