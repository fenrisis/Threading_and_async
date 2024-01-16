import threading

# counter
counter = 0

# mutex
mutex = threading.Lock()


def increment_counter():
    global counter
    for i in range(100):
        with mutex:
            counter += 1


# 3 threads
threads = []
for i in range(3):
    thread = threading.Thread(target=increment_counter())
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

# Result
print(f"Final counter value: {counter}")
