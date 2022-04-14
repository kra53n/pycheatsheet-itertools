from time import monotonic
from itertools import islice

lst = [*range(100)]

start_time = monotonic()
print('Используем стандартный срез')
print('Список от 0 до 50: ', lst[:50])
print(f'Прошло {monotonic() - start_time} сек.')
print()


start_time = monotonic()
print('Используем itertools.islice')
print('Список от 0 до 50: ', [*islice(lst, 0, 50)])
print(f'Прошло {monotonic() - start_time} сек.')
