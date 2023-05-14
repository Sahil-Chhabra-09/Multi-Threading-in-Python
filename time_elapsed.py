import threading
import time
import random as r

def thread_task(name):
    print(f"Thread {name} started")
    t = r.randint(3,8)
    time.sleep(t)
    print(f"Thread {name} ended after {t} seconds")


threads = []
start = time.time()
for i in range(5):
    t = threading.Thread(target = thread_task, args = (i, ))
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()
    
end = time.time()
    
print(f"All threads have finished, time elapsed : {end-start:.2f}")