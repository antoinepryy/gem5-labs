import time
from functools import lru_cache
import sys

@lru_cache(maxsize=3)
def test(n):
    """Stupid test function"""
    L = []
    for i in range(1000000000):
        L.append(n)
    return L


start = time.time()
a = test(10000)
end = time.time()
print(end - start)

sys.getsizeof(a)
