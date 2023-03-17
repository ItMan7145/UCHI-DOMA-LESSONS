list1 = [6, 3, 2, 7, 3, 0, 1, 4]

# for i in range(len(array) - 1):
#     maxim = array[i]
#     maximid = 0
#
#     for j in range(len(array) - i - 1):
#         if maxim < array[j]:
#             maxim = array[j]
#             maximid = j
#
#     array[j], array[maximid] = maxim, array[j]


for i in range(1, len(list1)):
    value = list1[i]
    j = i - 1
    while j >= 0 and value < list1[j]:
        list1[j + 1] = list1[j]
        j -= 1
    list1[j + 1] = value

print(list1)
