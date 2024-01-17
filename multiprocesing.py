from multiprocessing import Process
import time


def worker(task_id):
    print(f'Beginning {task_id}')
    time.sleep(3)
    print(f'Ending {task_id}')


processes = []

if __name__ == "__main__":
    for i in range(4):
        p = Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

print("All processes have completed.")
