# lrupy

Simple LRU cache for Python.

## Install

```bash
pip install "git+https://github.com/kasegao/lrupy#egg=lrupy"
```

## Examples

```python
from lrupy import LRUCache

cache = LRUCache[int, str](maxsize=2)
cache[0] = "0"
cache[1] = "1"

assert cache[0] == "0"
assert cache[1] == "1"
assert cache[2] is None

cache[2] = "2"
assert cache[0] is None
assert cache[1] == "1"
assert cache[2] == "2"

assert cache.get(3) is None
assert cache.get(3, lambda i: str(i)) == "3"
assert cache[1] is None
assert cache[2] == "2"
```

## Developers

```bash
pipenv install -d
pipenv shell
(.venv) python -m unittest
(.venv) tox
```
