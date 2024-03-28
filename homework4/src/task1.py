import time
import threading
import multiprocessing

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def run_fibonacci(n):
    start_time = time.time()
    for i in range(10):
        fibonacci(n)
    end_time = time.time()
    return end_time - start_time

def run_with_threading(n):
    start_time = time.time()
    threads = []
    for i in range(10):
        thread = threading.Thread(target=fibonacci, args=(n,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.time()
    return end_time - start_time

def run_with_multiprocessing(n):
    start_time = time.time()
    processes = []
    for i in range(10):
        process = multiprocessing.Process(target=fibonacci, args=(n,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    n = 36
    timers = []
    timers.append(run_fibonacci(n)) # synchronous launch
    timers.append(run_with_threading(n)) # launch using threading
    timers.append(run_with_multiprocessing(n)) # launch using multiprocessing

    with open("../artifacts/4_1.txt", "w") as file:
        file.write(f"synchronous launch: {timers[0]}\n")
        file.write(f"launch using threading: {timers[1]}\n")
        file.write(f"launch using multiprocessing: {timers[2]}\n")