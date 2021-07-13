import time
from multiprocessing import Process

from homework3.hw3_task02 import multiprocessing_calculating, slow_calculate


def test_time_spent_calculating_is_less_60_seconds():
    start_time = time.time()
    print(multiprocessing_calculating())

    end_time = time.time()
    assert (end_time - start_time) <= 60
