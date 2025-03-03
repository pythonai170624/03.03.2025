import threading
import time

from typing_extensions import override


# Custom Thread class that inherits from threading.Thread
class MyCustomThread(threading.Thread):
    def __init__(self, name, delay, iterations):
        # Always call the parent class's __init__ method
        super().__init__()
        self.name = name
        self.delay = delay
        self.iterations = iterations
        self.counter = 0

    # Override the run method (similar to Java)
    @override
    def run(self):
        print(f"Starting thread {self.name}")
        self.count()
        print(f"Thread {self.name} completed")

    def count(self):
        for i in range(self.iterations):
            time.sleep(self.delay)
            self.counter += 1
            print(f"Thread {self.name} - count: {self.counter}")

    def get_counter(self):
        return self.counter


# Example usage
if __name__ == "__main__":
    print("Creating threads...")

    # Create thread instances
    thread1 = MyCustomThread("Thread-1", 0.5, 15)
    thread2 = MyCustomThread("Thread-2", 1.0, 12)


    # Start threads
    thread1.start()  # This calls the run() method
    thread2.start()

    # Wait for threads to complete
    # thread1.join()
    # thread2.join()

    # Access thread results
    print(f"Final count for {thread1.name}: {thread1.get_counter()}")
    print(f"Final count for {thread2.name}: {thread2.get_counter()}")

    x = 0
    y = 1 / x

    print("All threads completed")
