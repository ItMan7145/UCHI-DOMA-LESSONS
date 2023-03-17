n = int(input())
array = list(map(int, input().split()))

for i in range(n - 1):
    for j in range(n - 2, i - 1, -1):
        if array[j] < array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
    print(*array)

