import time

init = time.time_ns()
while True:
    if time.time_ns() != init:
        end = time.time_ns()
        break



print(end - init)