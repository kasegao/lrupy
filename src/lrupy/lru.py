from abc import ABCMeta, abstractmethod
from typing import Any, Callable, Generic, Optional, OrderedDict, TypeVar


class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        ...


K = TypeVar("K", bound=Comparable)
V = TypeVar("V")


class LRUCache(Generic[K, V]):
    def __init__(self, maxsize: int = 100):
        if maxsize <= 0:
            raise ValueError("maxsize must be positive")

        self._cache: OrderedDict[K, V] = OrderedDict()
        self.maxsize = maxsize

    def __getitem__(self, key: K) -> Optional[V]:
        return self.get(key)

    def __setitem__(self, key: K, val: V):
        self.put(key, val)

    def get(self, key: K, f: Optional[Callable[[K], V]] = None) -> Optional[V]:
        val = self._cache.get(key)
        if val is not None:
            self._cache.move_to_end(key, last=True)
        else:
            if f is None:
                return None
            val = f(key)
            self.put(key, val)
        return val

    def put(self, key: K, val: V):
        if key in self._cache:
            del self._cache[key]
        self._cache[key] = val
        if len(self._cache) > self.maxsize:
            self._remove()

    def _remove(self):
        self._cache.popitem(last=False)
