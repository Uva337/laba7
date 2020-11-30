#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#В списке, состоящем из вещественных элементов, вычислить:
# 1)количество элементов списка, равных 0;
# 2)произведение элементов списка, расположенных между максимальным и минимальным элементом.
import sys


if __name__ == '__main__':
    a = tuple(map(float, input('Вещественные числа - ').split()))

    if not a:
        print("Cписок пуст")
        exit(1)

    l = 0
    for item in a:
        if item == 0:
            l += 1
    print("1)количество элементов списка равных 0 =", l)

    L = []
    a_min = a_max = a[0]
    i_min = i_max = 0
    b = [abs(i) for i in a]
    for i, item in enumerate(b):
        if item < a_min:
            i_min, a_min = i, item
        if item >= a_max:
            i_max, a_max = i, item
    a_new = a[i_min:i_max + 1]
    cl = 1
    for k in a_new:
        cl *= k
    print("2)Произведение = ", cl)
    a.sort()
    print(f"3) {a} ")
