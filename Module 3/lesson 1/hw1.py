nums = list(map(str, input().split()))

nums.sort(key=lambda x: (-len(str(x)), x))

print(*nums)
