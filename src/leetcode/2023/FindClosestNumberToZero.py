# Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple
# answers, return the number with the largest value.

from typing import List


class FindClosestNumberToZero:
    def findClosestNumber(self, nums: List[int]) -> int:
        result: int = float('inf')
        for element in nums:
            if abs(element) < result:
                result = abs(element)
        if result in nums:
            return result
        # it means the number was negative
        else:
            return -1 * result


check = FindClosestNumberToZero()
array = [1, 4, 3, 5]
result = check.findClosestNumber(array)
print(result)
