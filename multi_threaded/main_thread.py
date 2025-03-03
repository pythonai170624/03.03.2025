import threading

import os

print(f"Current Process ID (PID): {os.getpid()}")

# Get the current thread object
current_thread = threading.current_thread()

# Print the thread name
print(f"Current Thread Name: {current_thread.name}")

a = input()
