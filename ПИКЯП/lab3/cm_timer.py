import time
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        print(f"time: {elapsed_time:.1f}")

@contextmanager
def cm_timer_2():
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"time: {elapsed_time:.1f}")


if __name__ == '__main__':
    from time import sleep

    print("Тестирование cm_timer_1 (на основе класса):")
    with cm_timer_1():
        sleep(2.5)

    print("\nТестирование cm_timer_2 (с использованием contextlib):")
    with cm_timer_2():
        sleep(1.8)

    print("\nТестирование с коротким временем выполнения:")
    with cm_timer_1():
        sleep(0.5)

    with cm_timer_2():
        sleep(0.3)
