array = list(map(int, input().split()))
x = int(input())

left = 0
right = len(array) - 1

while left < right:
    mid = (left + right) // 2
    if array[mid] < x:
        left = mid + 1
    elif array[mid] > x:
        right = mid
    else:
        if mid == len(array) - 1 or array[mid + 1] != x:
            print(mid)
            break
        else:
            left = mid + 1
else:
    print(-1)
