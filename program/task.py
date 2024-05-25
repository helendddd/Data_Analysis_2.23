#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# С использованием многопоточности для
# заданного значения x найти сумму ряда S с
# точностью члена ряда по абсолютному
# значению e=10^-7 и произвести сравнение полученной суммы
# с контрольным значением функции y
# для двух бесконечных рядов.
# Варианты 22 и 23

import math
from threading import Lock, Thread

lock = Lock()


# Пример №22
def sum1(eps, s_dict):
    s = 0
    n = 0
    while True:
        a = 0.5 ** (4 * n + 1)/(4 * n + 1)
        if abs(a) < eps:
            break
        else:
            s += a
            n += 1
    with lock:
        s_dict["sum1"] = s


# Пример №23
def sum2(eps, s_dict):
    s = 0
    n = 1
    while True:
        a = 0.25 ** (n+2) / (n * (n + 1)*(n + 2))
        if abs(a) < eps:
            break
        else:
            s += a
            n += 1
    with lock:
        s_dict["sum2"] = s


def main():
    s = {}

    eps = 1e-7
    # Для примера №22
    y1 = 0.5 * math.log(3) + 0.5 * math.atan(0.5)
    # Для примера №23
    y2 = -5/64 - 9/32 * math.log(0.75)

    thread1 = Thread(target=sum1, args=(eps, s))
    thread2 = Thread(target=sum2, args=(eps, s))

    # Запуск потоков
    thread1.start()
    thread2.start()

    # Ожидание завершения потоков
    thread1.join()
    thread2.join()

    s1 = s["sum1"]
    s2 = s["sum2"]

    print(
        f"Сумма ряда полученная для 22 Варианта: {s1},\n"
        f"Контрольное значение y: {y1}, Разница: {abs(s1 - y1)}"
    )
    print(
        f"Сумма ряда полученная для 23 Варианта: {s2},\n"
        f"Контрольное значение y: {y2}, Разница: {abs(s2 - y2)}"
    )


if __name__ == "__main__":
    main()
