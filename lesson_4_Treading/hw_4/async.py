# Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# � При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения
# вычислений.

import asyncio
import time
from const import *


async def sum_elem(arr: [int]) -> int:
    total_sum = 0
    for number in arr:
        total_sum += number
    print(f'Сумма элементов списка: {total_sum}')
    return total_sum


async def main():
    task = asyncio.create_task(sum_elem(list_numbers))
    await task


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(f'Время выполнения вычислений - {time.time() - start_time:2f} секунд')
