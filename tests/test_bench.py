import time
import unittest

from lrupy import LRUCache


class BenchLRU(unittest.TestCase):
    @staticmethod
    def fib_naive(n: int) -> int:
        if n < 2:
            return n
        return BenchLRU.fib_naive(n - 1) + BenchLRU.fib_naive(n - 2)

    @staticmethod
    def fib_lru(n: int, cache: LRUCache[int, int]) -> int:
        if cache[n] is not None:
            return cache[n]

        if n < 2:
            cache[n] = n
        else:
            cache[n] = BenchLRU.fib_lru(n - 1, cache) + BenchLRU.fib_lru(n - 2, cache)
        return cache[n]

    def test_run(self):
        n = 34

        # naive
        start = time.time()
        self.fib_naive(n)
        end = time.time()
        elp = int((end - start) * 1000)
        dig = len(str(elp))
        print(f"[fib_naive]\t{elp} ms")

        # lru
        cache = LRUCache[int, int](maxsize=n)
        start = time.time()
        self.fib_lru(n, cache)
        end = time.time()
        print(f"[fib_lru]\t{int((end - start)*1000):>{dig}} ms")

        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
