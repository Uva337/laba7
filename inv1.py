import sys
#Ввести список А из 10 элементов, найти сумму элементов, меньших по модулю 3 и кратных 9, их количество и вывести результаты на экран.
if __name__ == '__main__':
    A = tuple(map(int, input().split()))
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)
    s = 0
    l = 0
    for item in A:
        if abs(item) < 3 and item % 9 == 0:
            s += item
            l += 1
    print(s, l)
