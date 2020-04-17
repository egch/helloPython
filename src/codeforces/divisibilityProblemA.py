# https://codeforces.com/contest/1328/problem/A
count = int(input())
while count > 0:
    a, b = map(int, input().split())
    if a % b == 0:
        print(0)
    else:
        print((a // b + 1) * b - a)
    count = count - 1
