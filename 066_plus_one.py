from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        for i in digits:
            total = total * 10 + i

        total += 1
        digits = [int(x) for x in str(total)]

        return digits


digits = [9, 9]
sol = Solution()
print(sol.plusOne(digits))
