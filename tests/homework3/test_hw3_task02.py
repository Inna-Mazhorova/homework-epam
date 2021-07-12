import time

from homework3.hw3_task02 import slow_calculate


def test_time_spent_calculating_is_less_4_seconds():
    start_time = time.time()
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
    assert (end_time - start_time) <= 4
