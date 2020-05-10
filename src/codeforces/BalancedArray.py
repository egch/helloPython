# https://codeforces.com/contest/1335/problem/A
count = int(input())
while count > 0:
    n = int(input())
    if n % 4 != 0:
        print('NO')
    else:
        sEven = 0
        sOdd = 0
        array = [0]*(n+1)
        for x in range(1, (n // 2) + 1):
            array[n // 2 + x] = 2 * x - 1
            array[x] = 2 * x
            sEven += 2 * x
            sOdd += 2 * x - 1

        array[n] += sEven - sOdd
        print('YES')
        for x in range(1, n + 1):
            print(str(array[x]) + ' ')

    count = count - 1
