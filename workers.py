import concurrent.futures


def worker(task_id):
    print(f"Task with id {task_id} done")


with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:

    futures = [executor.submit(worker, task_id) for task_id in range(4)]

    concurrent.futures.wait(futures)


print("All tasks completed")
