from typing import List
import random
class Balint:

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(0)
        if n == 1 and nums[0] == 1: return 2
        if n == 0: return 1
        counter=0;

        for i in range(1, n + 1):
            counter = 0
            while nums[0] > 0 and nums[0] <= n and nums[nums[0]] != nums[0]:
                counter = counter + 1
                tmp = nums[nums[0]]
                nums[nums[0]] = nums[0]
                nums[0] = tmp
            if nums[i] > 0 and nums[i] <= n and nums[nums[i]] != nums[i]:
                nums[0] = nums[nums[i]]
                nums[nums[i]] = nums[i]
            if counter > 0:
                print(counter)

        i = 1
        while i <= n and nums[i] == i:
            i += 1
        if nums[0] == i:
            i += 1
        print(counter)
        return i

obj = Balint()
nums = [random.randrange(300,1000) for i in range(1_000)]
result = obj.firstMissingPositive( nums)
