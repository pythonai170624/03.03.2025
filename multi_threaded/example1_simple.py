import threading

def print_numbers():
    for i in range(5000):
        print(f"Number {i}")

def print_letters():
    for letter in "ABCDE":
        print(f"Letter {letter}")

# Creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Starting threads
thread1.start()
thread2.start()

# Waiting for both to finish
# thread1.join()
# thread2.join()

for i in range(10):
    print('main', i**3)

print("Both threads have finished execution!")
