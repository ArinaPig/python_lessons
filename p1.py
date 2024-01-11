with open('p.txt', 'r') as f:
    k = 0
    for i in f:
        s = int(i[-5] + i[-4] + i[-3] + i[-2])
        if s < 1978:
            print(i[-47:-13])
            k += 1
    print(k)

print()

a = int(input('Введите нижний порог диапазона : '))
b = int(input('Введите верхний порог диапазона: '))

with open('p.txt', 'r') as f:
    k = 0
    for i in f:
        s = int(i[-5] + i[-4] + i[-3] + i[-2])
        if (s >= a) and (s <= b):
            print(i)
            k += 1
    print(k)
