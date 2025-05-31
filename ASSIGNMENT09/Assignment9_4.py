import time
import threading
import multiprocessing

# Function to sum a range of numbers
def sum_range(start, end):
    return sum(range(start, end))

# Threading target wrapper to store result
def threaded_sum(start, end, result, index):
    result[index] = sum_range(start, end)

# Multiprocessing target wrapper
def multiprocess_sum(start, end):
    return sum_range(start, end)

if __name__ == "__main__":
    start_num = 1
    end_num = 10_000_001
    mid = (start_num + end_num) // 2

    # Normal function
    start_time = time.time()
    total = sum_range(start_num, end_num)
    end_time = time.time()
    print(f"Normal Function Result: {total}, Time: {end_time - start_time:.4f} seconds")

    # Threading
    start_time = time.time()
    result = [0, 0]
    t1 = threading.Thread(target=threaded_sum, args=(start_num, mid, result, 0))
    t2 = threading.Thread(target=threaded_sum, args=(mid, end_num, result, 1))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    total = sum(result)
    end_time = time.time()
    print(f"Threading Result: {total}, Time: {end_time - start_time:.4f} seconds")

    # Multiprocessing
    start_time = time.time()
    with multiprocessing.Pool(processes=2) as pool:
        results = pool.starmap(multiprocess_sum, [(start_num, mid), (mid, end_num)])
    total = sum(results)
    end_time = time.time()
    print(f"Multiprocessing Result: {total}, Time: {end_time - start_time:.4f} seconds")
