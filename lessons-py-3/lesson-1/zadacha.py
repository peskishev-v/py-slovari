n = int(input())  # количество элементов в массиве
arr = list(map(int, input().split()))  # ввод массива
x = int(input())  # число, которое нужно найти

count = 0  # переменная для хранения количества вхождений числа x в массив

for i in range(n):
    if arr[i] == x:
        count += 1

print(count)
