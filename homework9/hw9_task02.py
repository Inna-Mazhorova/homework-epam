"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
"""

from contextlib import contextmanager

"""
1) As a class
"""


class ContextMan_Supressor:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        return True


"""
1) As a generator
"""


@contextmanager
def supressing(*exceptions):
    try:
        yield
    except exceptions:
        pass
