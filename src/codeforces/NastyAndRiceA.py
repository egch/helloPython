count = int(input())
while count > 0:
    n, a, b, c, d = map(int, input().split())
    if c + d < n * (a - b) or c - d > n * (a + b):
        print('no')
    else:
        print('yes')
    count -= 1
