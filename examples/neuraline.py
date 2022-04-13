import itertools

import time
start_time = time.monotonic()

#lst = ["some", "elements", 4, False, True, {"my value": "your key"}]
##for i in itertools.cycle(lst):
##    print(i)
#
#elemidx = 0
#while True:
#    print(lst[elemidx % len(lst)])
#    elemidx += 1

i = 0
while True:
    if i == 200:
        break
    print(i)
    i += 1

for i in itertools.count(0):
    if i == 200:
        break
    print(i)


print(f"Прошло {time.monotonic() - start_time} с")
