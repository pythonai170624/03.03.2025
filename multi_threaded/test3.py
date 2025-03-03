import multiprocessing
import time
from concurrent.futures import ProcessPoolExecutor
import os


def cpu_intensive_task(n):
    """A simple CPU-intensive task: calculate sum of squares"""
    result = 0
    for i in range(n):
        result += i * i
    return result, os.getpid()  # Return result and process ID


def using_multiprocessing_pool():
    """Demo of multiprocessing.Pool"""
    print("\n=== Using multiprocessing.Pool ===")
    start_time = time.time()

    # Create a pool with 4 worker processes
    with multiprocessing.Pool(processes=4) as pool:
        # Process 20 tasks with different input values
        results = pool.map(cpu_intensive_task, [1000000] * 20)

    end_time = time.time()

    # Count unique processes that were used
    process_ids = set(pid for _, pid in results)

    print(f"Time taken: {end_time - start_time:.4f} seconds")
    print(f"Number of different processes used: {len(process_ids)}")
    print(f"Process IDs: {process_ids}")


def using_process_executor():
    """Demo of concurrent.futures.ProcessPoolExecutor"""
    print("\n=== Using concurrent.futures.ProcessPoolExecutor ===")
    start_time = time.time()

    # Create an executor with 4 worker processes
    with ProcessPoolExecutor(max_workers=4) as executor:
        # Submit 20 tasks with different input values
        future_results = [executor.submit(cpu_intensive_task, 1000000) for _ in range(20)]

        # Get results as they complete
        results = [future.result() for future in future_results]

    end_time = time.time()

    # Count unique processes that were used
    process_ids = set(pid for _, pid in results)

    print(f"Time taken: {end_time - start_time:.4f} seconds")
    print(f"Number of different processes used: {len(process_ids)}")
    print(f"Process IDs: {process_ids}")


def sequential_execution():
    """Reference: sequential execution on the main process"""
    print("\n=== Sequential Execution (for comparison) ===")
    start_time = time.time()

    results = []
    for _ in range(20):
        results.append(cpu_intensive_task(1000000))

    end_time = time.time()

    # Should only have one process ID (the main process)
    process_ids = set(pid for _, pid in results)

    print(f"Time taken: {end_time - start_time:.4f} seconds")
    print(f"Number of different processes used: {len(process_ids)}")
    print(f"Process IDs: {process_ids}")


if __name__ == "__main__":
    print(f"Main process ID: {os.getpid()}")
    print(f"Number of CPU cores: {multiprocessing.cpu_count()}")

    # Run the demos
    sequential_execution()
    using_multiprocessing_pool()
    using_process_executor()

    print("\nNote: ProcessPoolExecutor is generally recommended as it offers:")
    print("- A more modern interface consistent with ThreadPoolExecutor")
    print("- Better exception handling")
    print("- Context manager support")
    print("- Future-based interface for more flexibility")