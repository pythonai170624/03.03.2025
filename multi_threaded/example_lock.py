import threading
import time

counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:  # Ensuring only one thread modifies counter at a time
        for _ in range(10):
            print(threading.current_thread().name)
            counter += 1

threads = []
for _ in range(50):  # Creating 5 threads
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final counter value: {counter}")
