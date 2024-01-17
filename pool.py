from multiprocessing import Pool, Manager
import time


def worker(task_id, queue):
    start_msg = f'Start {task_id}'
    queue.put(start_msg)

    time.sleep(2)

    end_msg = f'End {task_id}'
    queue.put(end_msg)

    return f'Task {task_id} completed'


if __name__ == "__main__":
    with Manager() as manager:
        queue = manager.Queue()
        with Pool(4) as p:
            results = p.starmap(worker, [(i, queue) for i in range(4)])

        while not queue.empty():
            print(queue.get())

    print("\nResults from the worker functions:")
    for result in results:
        print(result)

    print("\nAll tasks in the pool  completed.")
