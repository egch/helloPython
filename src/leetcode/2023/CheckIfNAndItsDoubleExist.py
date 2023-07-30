from typing import List


class CheckIfNAndItsDoubleExist:
    def checkIfExist(self, arr: List[int]) -> bool:
        mySet = set()
        for n in arr:
            if (n * 2 in mySet) or (n % 2 == 0 and n / 2 in mySet):
                return True
            mySet.add(n)
        return False


check = CheckIfNAndItsDoubleExist()
array = [1, 4, 3, 5]
result = check.checkIfExist(array)
print(result)
