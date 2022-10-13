class XOROperationInAnArray:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for j in range(n):
            result ^= start + 2 * j
        return result


obj = XOROperationInAnArray()

result = obj.xorOperation(5, 3)
print(result)
