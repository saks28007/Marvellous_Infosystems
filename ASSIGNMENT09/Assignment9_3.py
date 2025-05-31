import multiprocessing
import math

def compute_factorial(n):
    return math.factorial(n)

if __name__ == "__main__":
    numbers = [3, 5, 7, 10, 12]

    # Create a pool of worker processes
    with multiprocessing.Pool() as pool:
        # Map the list of numbers to the compute_factorial function
        results = pool.map(compute_factorial, numbers)

    print("Factorials:", results)
