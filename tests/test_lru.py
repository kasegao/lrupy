import unittest

from lrupy import LRUCache


class TestLRU(unittest.TestCase):
    def test_normal(self):
        cache = LRUCache[int, int](maxsize=2)
        cache.put(0, 0)  # [0]
        cache.put(1, 1)  # [0, 1]
        self.assertEqual(list(cache._cache.keys()), [0, 1])

        self.assertEqual(cache.get(0), 0)
        self.assertEqual(list(cache._cache.keys()), [1, 0])

        self.assertEqual(cache.get(1), 1)
        self.assertEqual(list(cache._cache.keys()), [0, 1])

        self.assertEqual(cache.get(2), None)
        self.assertEqual(list(cache._cache.keys()), [0, 1])

        self.assertEqual(cache.get(2, lambda i: i), 2)  # [1, 2]
        self.assertEqual(list(cache._cache.keys()), [1, 2])

        self.assertEqual(cache.get(0), None)
        self.assertEqual(list(cache._cache.keys()), [1, 2])

        self.assertEqual(cache.get(1), 1)
        self.assertEqual(list(cache._cache.keys()), [2, 1])


if __name__ == "__main__":
    unittest.main()
