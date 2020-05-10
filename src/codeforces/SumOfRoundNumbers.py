count = int(input())
while count > 0:
    n = input()
    size = len(n)
    result = ''
    counter = 0
    for i in range(size):
        if n[i] != '0':
            result += str(int(n[i]) * pow(10, size - i - 1))+" "
            counter += 1
    print(counter)
    print(result)
    count -= 1
