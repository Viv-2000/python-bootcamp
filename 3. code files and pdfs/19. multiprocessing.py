import math
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
import time

def f1(i):
    time.sleep(2)
    print(i)


def f2():
    for i in range(5):
        print(i+10)
        time.sleep(2)

def f3(i):
    time.sleep(2)
    return math.factorial(i)

nums=[1,2,3,4,5,6,7,8,9]

''' ---------------- BASIC MULTIPROCESSING ----------------
 multiprocessing.Process creates completely separate Python processes
 (separate memory space, separate interpreter). Useful for CPU-bound work.

 IMPORTANT BUG:
 target=f1(5) ❌
 This CALLS the function immediately in the main process and passes its
 return value (usually None) as the target, so the new process runs nothing.

 Correct usage:
 target=f1
 args=(5,)

 multiprocessing internally runs: target(*args)
 so args must be iterable → args=(5,) for a single argument.

 start() → launches the new process
 join()  → blocks main program until that process finishes

p3 below shows the correct pattern for passing arguments.'''

if __name__=='__main__':
    p1=multiprocessing.Process(target=f1(5))    # refer to the bottom of file for more info
    p2 = multiprocessing.Process(target=f2)
    p3 = multiprocessing.Process(target=f1, args=(5,))
    t=time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    


'''
 ---------------- PROCESSPOOLEXECUTOR ----------------
 ProcessPoolExecutor is a higher-level API for multiprocessing.
 Instead of manually creating processes, it maintains a pool of
 worker processes and distributes tasks automatically.

 max_workers=3 → at most 3 processes run tasks simultaneously.

 executor.map(function, iterable)
 - sends each element of iterable to a worker
 - equivalent to running f3(i) in parallel for every i in nums

 executor.map returns a lazy iterator of results in input order.
 Converting to list(...) forces execution and collects results.

 This approach is usually cleaner and safer than manually
 managing Process objects for parallel CPU tasks.
'''

## using ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(f3,nums))
        
    print([res for res in results])

    print(time.time()-t)


'''
 multiprocessing.Process usage rules
 target=f(5) ❌ calls the function immediately in main process
 target must be the function reference → target=f
 arguments are passed separately using args

 multiprocessing internally does: target(*args)
 so args must be iterable

 args=5   ❌ int not iterable
 args=(5) ❌ still int
 args=(5,) ✅ correct single-element tuple

 Example:
 multiprocessing.Process(target=f, args=(5,))
'''
