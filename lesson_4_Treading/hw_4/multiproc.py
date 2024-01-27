# Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# � При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения
# вычислений.

from multiprocessing import Process, Pool
import time
from const import *


def sum_elem(arr: [int]) -> int:
    total_sum = 0
    for number in arr:
        total_sum += number
    return total_sum


start_time = time.time()
if __name__ == '__main__':
    print(f'Сумма элементов списка: {sum_elem(list_numbers)}\t')
    pr = Process(target=sum_elem, args=(list_numbers,))
    pr.start()
    pr.join()
    print(f'Время выполнения вычислений - {time.time() - start_time:2f} секунд')
