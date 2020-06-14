import time
import threading


start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping...')



#t1 = threading.Thread(target=do_something) # we do not add () because we do not want to run it. We just gave thread 1 that this function exist
#t2 = threading.Thread(target=do_something)

threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')