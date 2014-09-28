"""
Python packaging voodoo stolen from
https://github.com/pypa/pip/blob/develop/pip/__main__.py
"""

import sys

if __package__ == '':
    import os
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)

if __name__ == "__main__":
    import babel
    babel.main()