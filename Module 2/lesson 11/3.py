array = [x for x in range(10000)]

num = 70

maxim = array[-1]
misha = array[0]

cnt = 0

while 1:
    cnt += 1

    mid = (maxim + misha) // 2

    if num < mid:
        maxim = mid
    elif num > mid:
        misha = mid + 1
    else:
        break

print(mid)
print(cnt)
