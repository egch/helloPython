# https://codeforces.com/contest/1335/problem/A
count = int(input())
while count > 0:
    n = int(input())
    if n <= 2:
        print(0)
    elif n % 2 == 0:
        print(n // 2 - 1)
    else:
        print(n // 2)
    count = count - 1
