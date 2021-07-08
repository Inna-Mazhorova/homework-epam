import hashlib
import os
import random
import struct
import time
from multiprocessing import Pool

# Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
# Calculation time should not take more than a minute. Use functional capabilities of multiprocessing module.
# You are not allowed to modify slow_calculate function.

start_time = time.time()

cores_pc = os.cpu_count()


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    exit(sum(struct.unpack("<" + "B" * len(data), data)))


if __name__ == "__main__":
    pool = Pool(cores_pc)
    result_list = []
    n = 1
    sum_slow_calculate = 0
    for i in range(n):
        result = pool.apply_async(slow_calculate(i))
        result_list.append(result)
    results = [result.get() for i in result_list]
    print(sum(results))


print("--- %s seconds ---" % (time.time() - start_time))
