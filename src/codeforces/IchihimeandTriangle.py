# https://codeforces.com/contest/1337/problem/A
count = int(input())
while count > 0:
    a, b, c, d = map(int, input().split())
    msg = "%s %s %s" % (b, c, c)
    print(msg)
    count = count - 1
