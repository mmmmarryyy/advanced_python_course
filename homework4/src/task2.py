import math
import concurrent.futures
import logging
import time

def integrate(f, a, b, *, n_jobs=1, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc

def integrate_range(f, a, start, end, step):
    local_acc = 0
    for i in range(start, end):
        local_acc += f(a + i * step) * step
    return local_acc

def integrate_threads(f, a, b, n_jobs=1, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_jobs) as executor:
        futures = []
        for i in range(n_jobs):
            start = i * (n_iter // n_jobs)
            end = (i + 1) * (n_iter // n_jobs) if i != n_jobs - 1 else n_iter
            futures.append(executor.submit(integrate_range, f, a, start, end, step))
        
        for future in futures:
            acc += future.result()
    
    return acc

def integrate_processes(f, a, b, n_jobs=1, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=n_jobs) as executor:
        futures = []
        for i in range(n_jobs):
            start = i * (n_iter // n_jobs)
            end = (i + 1) * (n_iter // n_jobs) if i != n_jobs - 1 else n_iter
            futures.append(executor.submit(integrate_range, f, a, start, end, step))
        
        for future in futures:
            acc += future.result()
    
    return acc

def compare_execution_time(f, a, b, func, n_jobs_list):
    results = {}
    
    for n_jobs in n_jobs_list:
        start_time = time.time()
        func(f, a, b, n_jobs=n_jobs)
        end_time = time.time()
        results[f"n_jobs={n_jobs}"] = end_time - start_time
        
    return results

if __name__ == "__main__":
    logging.basicConfig(filename="../artifacts/4_2.txt", filemode="w", level=logging.INFO, format='%(asctime)s - %(message)s')

    cpu_num = 4
    n_jobs_list = list(range(1, cpu_num*2+1))

    logging.info("Starting ThreadPoolExecutor")
    threadpool_results = compare_execution_time(math.cos, 0, math.pi / 2, integrate_threads, n_jobs_list)
    for key, value in threadpool_results.items():
        logging.info(f"{key}: {value}")

    logging.info("------------------------------------------------------------------")
    logging.info("Starting ProcessPoolExecutor")
    processpool_results = compare_execution_time(math.cos, 0, math.pi / 2, integrate_processes, n_jobs_list)
    for key, value in processpool_results.items():
        logging.info(f"{key}: {value}")