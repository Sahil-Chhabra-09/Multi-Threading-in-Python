import threading

# Shared variable
shared_variable = 0

# Lock for synchronization
lock = threading.Lock()
condition = threading.Condition(lock)

# Function to be executed by the thread
def thread_function():
    global shared_variable  # Access the shared variable
    with condition:
        condition.wait()  # Wait for the condition

        # Access and modify the shared variable
        shared_variable += 1
        print(f"Thread {threading.current_thread().name}: Shared variable updated")

# Create and start multiple threads
threads = []
for i in range(5):
    t = threading.Thread(target=thread_function, name=f"Thread-{i+1}")
    threads.append(t)
    t.start()

# Allow threads to acquire the lock and update the shared variable
with condition:
    condition.notify_all()  # Notify all threads waiting on the condition

# Wait for all threads to finish
for t in threads:
    t.join()

# Print the final value of the shared variable
print("Final value of the shared variable:", shared_variable)
