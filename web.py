
import time


start = time.time()

for i in range(100):
    for j in range(100):
        for k in range(100):
            print(i, j, k)


end = time.time()

duration = end - start

print(duration)
