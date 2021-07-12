import time
from multiprocessing import Process

from homework3.hw3_task02_with_process import slow_calculate


def test_time_spent_calculating_is_less_60_seconds():
    if __name__ == "__main__":
        procs = []
        for i in range(501):
            proc = Process(target=slow_calculate, args=(i,))
            procs.append(proc)
            proc.start()

        result = []
        for proc in procs:
            proc.join()
            result.append(proc.exitcode)
        print(sum(result))

        end_time = time.time()
        assert (end_time - start_time) <= 60
