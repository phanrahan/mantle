try:
    from functools import lru_cache
except ImportError:
    from backports.functools_lru_cache import lru_cache
