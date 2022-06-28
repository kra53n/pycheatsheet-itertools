import time
from itertools import count


start_time = time.monotonic()


for i in count():
    if i == 200:
        break
    print(i)


print(f"Прошло {time.monotonic() - start_time} секунд")
