s = ' '
n = int(input("Введите число :"))
while n != 0:
    s = str(n%2) + s
    n //=2
print(s)