import hashlib
import random
import struct
import time
from multiprocessing import Process, Semaphore

# Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
# Calculation time should not take more than a minute. Use functional capabilities of multiprocessing module.
# You are not allowed to modify slow_calculate function.

start_time = time.time()


def slow_calculate(value, sema):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    # sema.acquire()
    data = hashlib.md5(str(value).encode()).digest()
    exit(sum(struct.unpack("<" + "B" * len(data), data)))
    sema.release()


if __name__ == "__main__":
    concurrency = 4
    sema = Semaphore(concurrency)
    procs = []
    for i in range(4):
        sema.acquire()
        proc = Process(target=slow_calculate, args=(i, sema))
        procs.append(proc)
        proc.start()

    result = []
    for proc in procs:
        proc.join()
        result.append(proc.exitcode)
    print(sum(result))

end_time = time.time()

print("--- %s seconds ---" % (end_time - start_time))
