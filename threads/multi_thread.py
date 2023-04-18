from threading import Thread
import time 

COUNT = 50_000_000

def countdown(n: float):
    while n > 0: 
        n = n-1

thread_1 = Thread(target=countdown, args=(COUNT))

start = time.time()
countdown(COUNT)
end = time.time()

print('tempo de execução: ' + str(end - start))

