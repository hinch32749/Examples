import time
from threading import Thread
from datetime import datetime


def fn():
    start = datetime.now()
    print(f"start fn() {start}")
    time.sleep(3)
    print("From function with block 3 sec")
    end = datetime.now() - start
    print(f"end fn() {end}")


def task():
    start = datetime.now()
    # print(f"start task() {start}")
    time.sleep(1)
    print('Function task with block 1 sec')
    end = datetime.now() - start
    print(f"end task() {end}")


class CustomThread(Thread):
    def run(self):
        time.sleep(1)
        print('Custom Class')


thread1 = CustomThread()
thread = Thread(target=task)

if __name__ == "__main__":
    print('start __main__')
    thread.start()
    print('between __main__')
    thread1.start()
    thread1.join()

    print('end __main__')
    thread.join()

print(type)