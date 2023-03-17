n = int(input())
m = int(input())

matrix = [[0] * n for i in range(m)]

dx, dy = 0, 1
x, y = 0, 0

for i in range(1, n * m + 1):
    matrix[x][y] = i

    if x + dx >= m or y + dy >= n or matrix[x + dx][y + dy] != 0:
        dx, dy = dy, -dx
    x += dx
    y += dy

for elem in matrix:
    print(elem)
