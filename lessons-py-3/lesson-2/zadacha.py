n = int(input())  # количество элементов в массиве
arr = list(map(int, input().split()))  # ввод массива
x = int(input())  # число, к которому нужно найти ближайший элемент

min_diff = float('inf')  # переменная для хранения минимальной разницы между числом x и элементами массива
closest_num = None  # переменная для хранения элемента массива, ближайшего к числу x

for i in range(n):
    diff = abs(arr[i] - x)  # вычисляем разницу между числом x и текущим элементом массива
    if diff < min_diff:
        min_diff = diff
        closest_num = arr[i]

print(closest_num)
