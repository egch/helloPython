count = int(input())
while count > 0:
    n, k = map(int, input().split())
    if k % (n - 1) == 0:
        print(k - 1 + k // (n - 1))
    else:
        print(k + k // (n - 1))
    count = count - 1
