# https://codeforces.com/contest/1335/problem/B
count = int(input())
while count > 0:
    n, a, b = map(int, input().split())
    result = ''
    for x in range(0, n):
        result += chr(ord('a') + x % b)
    print(result)
    count = count - 1
