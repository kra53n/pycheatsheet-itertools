import time


start_time = time.monotonic()


i = 0
while True:
    if i == 200:
        break
    print(i)
    i += 1


print(f"Прошло {time.monotonic() - start_time} секунд")
