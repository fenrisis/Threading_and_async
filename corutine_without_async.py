import multiprocessing
import time


def my_task(name):
    print(f"{name}: Beginning")
    time.sleep(2)  # Imitation
    print(f"{name}: Ending")
    return f"{name}: result"


if __name__ == "__main__":
    for i in range(3):
        p = multiprocessing.Process(target=my_task, args=(f'Task{i}',))
        p.start()
        