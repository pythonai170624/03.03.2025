import time
import multiprocessing


def count_range(start, end, name, return_dict=None):
    """Count from start to end-1"""
    counter = 0
    for i in range(start, end):
        counter += 1
    print(f"{name} finished. Final count: {counter}")
    if return_dict is not None:
        return_dict[name] = counter


def single_process_count():
    """Count to 10 million in a single process"""
    start_time = time.time()

    count_range(1, 500_000_001, "Single process")

    end_time = time.time()
    elapsed = end_time - start_time
    print(f"Single process time: {elapsed:.4f} seconds")
    return elapsed


def multi_process_count():
    """Count to 10 million using two processes"""
    start_time = time.time()

    # Create a manager to share data between processes
    manager = multiprocessing.Manager()
    return_dict = manager.dict()

    # Create two processes
    process1 = multiprocessing.Process(
        target=count_range,
        args=(1, 250_000_001, "Process 1", return_dict)
    )
    process2 = multiprocessing.Process(
        target=count_range,
        args=(250_000_001, 500_000_001, "Process 2", return_dict)
    )

    # Start both processes
    process1.start()
    process2.start()

    # Wait for both processes to complete
    process1.join()
    process2.join()

    end_time = time.time()
    elapsed = end_time - start_time
    print(f"Two processes time: {elapsed:.4f} seconds")

    # Verify results
    total_count = sum(return_dict.values())
    print(f"Total count from multiprocessing: {total_count}")

    print(return_dict)

    return elapsed


if __name__ == "__main__":
    print("Starting test...")
    print("Running single process test...")
    single_time = single_process_count()

    print("\nRunning two processes test...")
    multi_time = multi_process_count()

    print("\nResults comparison:")
    print(f"Single process: {single_time:.4f} seconds")
    print(f"Two processes: {multi_time:.4f} seconds")

    if multi_time < single_time:
        improvement = (single_time - multi_time) / single_time * 100
        print(f"Two processes were faster by {improvement:.2f}%")
    else:
        slowdown = (multi_time - single_time) / single_time * 100
        print(f"Two processes were slower by {slowdown:.2f}%")


    print("\nExplanation:")
    print("Unlike threading, multiprocessing creates separate Python processes")
    print("each with its own Python interpreter and memory space, bypassing")
    print("the Global Interpreter Lock (GIL). This allows true parallel execution")
    print("for CPU-bound tasks, which usually results in performance improvement")
    print("on multi-core systems.")
    print("\nNote: There is some overhead for process creation and inter-process")
    print("communication, but for significant computational work, multiprocessing")
    print("typically outperforms threading for CPU-bound tasks.")