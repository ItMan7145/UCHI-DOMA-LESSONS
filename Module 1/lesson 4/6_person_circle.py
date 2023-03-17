# n = int(input())
# k = int(input())
#
# massive = []
#
# for chel in range(1, n + 1):
#     massive.append(chel)
#
#
# def sorting():
#     global massive
#     for person in massive:
#         if person == k:
#             massive.remove(person)
#             sorting()
#     print(massive)
#
#
# sorting()


n, k = int(input()), int(input())
last = 0
for i in range(1, n + 1):
    last = (last + k) % i

print(last + 1)
