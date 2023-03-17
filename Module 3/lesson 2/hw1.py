def get_sum():
    summ = 0

    def func(n):
        nonlocal summ
        summ += n
        return summ

    return func


s = get_sum()

nums = map(int, input().split())
for i in nums:
    print(s(i))
