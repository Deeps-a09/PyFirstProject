import time


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print(f"Time taken by function {end_time - start_time}")

    return wrapper()


def test_ui_1():
    print("Add a function, time taken by this function")
    time.sleep(2)

# test_ui_1()
