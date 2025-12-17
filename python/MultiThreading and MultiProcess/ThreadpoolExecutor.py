from concurrent.futures import ThreadPoolExecutor
import time

def func(seconds):
    print("Start Here", seconds)
    time.sleep(seconds)
    print("End Here", seconds)

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(func, 4)
    executor.submit(func, 1)
    executor.submit(func, 2)
