from typing import List


# A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is
# the same.
# Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression.
# Otherwise, return false.


class CanMakeArithmeticProgressionFromSequence:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        delta: int = arr[1] - arr[0]
        for index, element in enumerate(arr[2:], start=2):
            if arr[index] - arr[index - 1] != delta:
                return False
        return True


instance = CanMakeArithmeticProgressionFromSequence()
array = [1, 4, 3, 5]
result = instance.canMakeArithmeticProgression(array)
print(result)
