# чтение входных данных
nums = list(map(int, input().split()))
total = int(input())

# создание множества для хранения уже просмотренных чисел
seen = set()

# перебираем числа в списке
for num in nums:
    # находим разницу между total и текущим числом
    complement = total - num
    # если такая разница уже была в списке, то нашли пару
    if complement in seen:
        # выводим пару чисел и завершаем программу
        print(min(num, complement), max(num, complement))
        break
    # добавляем текущее число в множество просмотренных
    seen.add(num)
else:
    # если прошли по всем числам и не нашли пару, выводим None
    print(None)
