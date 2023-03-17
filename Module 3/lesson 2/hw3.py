def trib():
    n1, n2, n3 = 0, 0, 1
    while 1:
        yield n1
        n1, n2, n3 = n2, n3, n1 + n2 + n3


n = int(input())
t = trib()
for i in range(n):
    print(next(t), end=' ')
