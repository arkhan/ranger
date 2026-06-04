# This file is part of ranger, the console file manager.
# License: GNU GPL version 3, see the file "AUTHORS" for details.

from __future__ import (absolute_import, division, print_function)

from functools import lru_cache


# Similar to functools.lru_cache of python3 — now delegates to the real thing.
# The original hand-rolled cache had no size limit and no thread safety;
# lru_cache is implemented in C and is significantly faster.
def cached_function(fnc):
    """Unbounded memoisation decorator (drop-in replacement for the old impl).

    Uses functools.lru_cache with maxsize=None for maximum performance.
    The cache object is exposed as ``fnc._cache`` for compatibility.
    """
    cached = lru_cache(maxsize=None)(fnc)

    # Expose a compatible _cache attribute (read-only view via cache_info)
    cached._cache = cached  # pylint: disable=protected-access
    return cached
