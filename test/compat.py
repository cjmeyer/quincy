# Compatibility layer for unittest(2) depending on Python version used.

__all__ = (
    'unittest'
)

import sys

try:
    import unittest2 as unittest
except:
    if sys.version_info >= (2, 7):
        import unittest
    else:
        raise

