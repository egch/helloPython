# https://codeforces.com/contest/1335/problem/A
count = int(input())
while count > 0:
    n = int(input())
    s1 = pow(2, n)
    s2 = 0
    for x in range(1, n // 2):
        s1 += pow(2, x)
    for x in range(n // 2, n):
        s2 += pow(2, x)
    print(s1 - s2)

    count = count - 1
