import threading
import time

def func(seconds):
    print("Start Here", seconds)
    time.sleep(seconds)
    print("End Here", seconds)

# Serial Way
# func(4)
# func(1)
# func(2)

# Same code using threads
t1 = threading.Thread(target=func, args=(4,))
t2 = threading.Thread(target=func, args=(1,))
t3 = threading.Thread(target=func, args=(2,))

t1.start()
t2.start()
t3.start()
# output - 
    # Start Here 4
    # Start Here 1
    # Start Here 2
    # End Here 1
    # End Here 2
    # End Here 4
    # Here we clearly see they start one after another but end in the order of their sleep time
    # This is because the threads are not blocking each other
t1.join()
t2.join()
t3.join()