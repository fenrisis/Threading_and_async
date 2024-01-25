import time


# Coroutine 1: Just prints text and waits
def coroutine_1():
    for i in range(3):
        print(f'Coroutine 1 {i}')
        yield  # pass
        time.sleep(1)


# Coroutine 2: Just prints text and waits
def coroutine_2():
    for i in range(3):
        print(f'Coroutine 2 {i}')
        yield  # pass
        time.sleep(1)


def event_loop(*coroutines):
    # Initialize iterators for all coroutines
    iterators = [iter(c()) for c in coroutines]

    while iterators:
        for itr in list(iterators):
            try:
                next(itr)  # next step
            except StopIteration:
                # remove from loop
                iterators.remove(itr)


event_loop(coroutine_1, coroutine_2)
