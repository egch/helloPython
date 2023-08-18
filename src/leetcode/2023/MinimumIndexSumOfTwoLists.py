# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
#
# A common string is a string that appeared in both list1 and list2.
#
# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then
# i + j should be the minimum value among all the other common strings.
#
# Return all the common strings with the least index sum. Return the answer in any order.
import sys
from typing import List
from typing import Dict


class MinimumIndexSumOfTwoLists:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map: Dict[str, int] = {}
        min: int = sys.maxsize
        result: List[str] = []
        for index, element in enumerate(list1):
            map[element] = index
        for index, element in enumerate(list2):
            if element in map:
                map[element] = map[element] + index
                if map[element] < min:
                    min = map[element]
                    result = [element]
                elif map[element] == min:
                    result.append(element)
        return result
