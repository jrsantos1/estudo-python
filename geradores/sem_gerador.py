import sys
import time

def gera():
    r = []
    for n in range(100):
        r.append(n)
    return r

start = time.time()
for v in gera():
    print(v)

end = time.time()

print(f"executado em {start - end}")