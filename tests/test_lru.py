import unittest

from lrupy import LRUCache


class TestLRU(unittest.TestCase):
    def test_get(self):
        cache = LRUCache[int, str](maxsize=2)
        cache.put(0, "0")  # [0]
        cache.put(1, "1")  # [0, 1]
        self.assertEqual(list(cache._cache.keys()), [0, 1])

        self.assertEqual(cache.get(0), "0")
        self.assertEqual(list(cache._cache.keys()), [1, 0])

        self.assertEqual(cache.get(1), "1")
        self.assertEqual(list(cache._cache.keys()), [0, 1])

        self.assertEqual(cache.get(2), None)
        self.assertEqual(list(cache._cache.keys()), [0, 1])

    def test_get_or(self):
        cache = LRUCache[int, str](maxsize=2)
        cache.put(0, "0")  # [0]
        cache.put(1, "1")  # [0, 1]

        self.assertEqual(cache.get(2), None)
        self.assertEqual(list(cache._cache.keys()), [0, 1])

        self.assertEqual(cache.get_or(2, "2"), "2")  # [1, 2]
        self.assertEqual(list(cache._cache.keys()), [1, 2])

        self.assertEqual(cache.get(0), None)
        self.assertEqual(list(cache._cache.keys()), [1, 2])

        self.assertEqual(cache.get_or(1, "3"), "1")
        self.assertEqual(list(cache._cache.keys()), [2, 1])

    def test_get_or_else(self):
        succ = lambda i: str(i + 1)
        self.assertEqual(succ(1), "2")

        cache = LRUCache[int, str](maxsize=2)
        cache.put(0, "0")  # [0]
        cache.put(1, "1")  # [0, 1]

        self.assertEqual(cache.get(2), None)
        self.assertEqual(list(cache._cache.keys()), [0, 1])

        self.assertEqual(cache.get_or_else(2, succ), "3")  # [1, 2]
        self.assertEqual(list(cache._cache.keys()), [1, 2])

        self.assertEqual(cache.get(0), None)
        self.assertEqual(list(cache._cache.keys()), [1, 2])

        self.assertEqual(cache.get_or_else(1, succ), "1")
        self.assertEqual(list(cache._cache.keys()), [2, 1])


if __name__ == "__main__":
    unittest.main()
