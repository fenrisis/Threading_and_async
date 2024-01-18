import concurrent.futures
import time


def my_task(name):
    print(f"{name}: Beginning")
    time.sleep(2)  # Imitation
    print(f"{name}: Ending")
    return f"{name}: result"


def main():

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:

        future_to_task = {executor.submit(my_task, name): name for name in ['Task 1', 'Task 2', 'Task 3']}

        for future in concurrent.futures.as_completed(future_to_task):
            task_name = future_to_task[future]
            try:
                result = future.result()
            except Exception as e:
                print(f"{task_name} generated exception: {e}")
            else:
                print(f"{task_name} returned result: {result}")


if __name__ == "__main__":
    main()
