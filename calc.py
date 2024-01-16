import concurrent.futures


def add(a, b):
    return f"Addition: {a} + {b} = {a + b}"


def subtract(a, b):
    return f"Subtraction: {a} - {b} = {a - b}"


def divide(a, b):
    return f"Division: {a} / {b} = {a / b}"


def multiply(a, b):
    return f"Multiplication: {a} * {b} = {a * b}"


with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:

    futures = [
        executor.submit(add, 10, 10),
        executor.submit(subtract, 30, 20),
        executor.submit(divide, 100, 10),
        executor.submit(multiply, 5, 5)
    ]

    for future in concurrent.futures.as_completed(futures):
        print(future.result())


print("All tasks are completed.")
