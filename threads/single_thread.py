import time 

COUNT = 50_000_000

def countdown(n: float):
    while n > 0: 
        n = n-1

start = time.time()
countdown(COUNT)
end = time.time()


print('tempo de execução: ' + str(end - start))

