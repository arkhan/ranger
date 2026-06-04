# This file is part of ranger, the console file manager.
# License: GNU GPL version 3, see the file "AUTHORS" for details.

from __future__ import absolute_import

from functools import lru_cache


def cached_function(fnc):
    """Unbounded memoisation decorator backed by functools.lru_cache.

    Equivalent to the previous hand-rolled implementation but uses the
    C-level lru_cache for better performance.  The cache object is exposed
    as ``fnc._cache`` for read-only introspection.
    """
    cached = lru_cache(maxsize=None)(fnc)
    cached._cache = cached  # pylint: disable=protected-access
    return cached
