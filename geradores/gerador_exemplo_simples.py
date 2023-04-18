import sys
import time

def gera():
    for n in range(100):
        yield n

start = time.time()
for v in gera():
    print(v)

end = time.time()

print(f"executado em {start - end}")