def sum_odd_index(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    print(f"Сумма равна: {s}")

lst = [9, 1, 5, 5, 3]
sum_odd_index(lst)
lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd_index(lst)
