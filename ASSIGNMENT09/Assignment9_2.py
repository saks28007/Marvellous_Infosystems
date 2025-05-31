import multiprocessing

def square_number(n, result, index):
    result[index] = n * n

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    n = len(numbers)

    # Shared array to store results
    result = multiprocessing.Array('i', n)

    processes = []

    for i in range(n):
        # Create a process for each number
        p = multiprocessing.Process(target=square_number, args=(numbers[i], result, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Squared numbers:", list(result))
