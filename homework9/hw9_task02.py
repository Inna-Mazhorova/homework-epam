"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
"""

from contextlib import contextmanager
from types import TracebackType
from typing import Generator, Type

"""
1) As a class
"""


class ContextManSupressor:
    def __init__(self, exception: Type[BaseException]) -> None:
        self.exception = exception

    def __enter__(self) -> None:
        pass

    def __exit__(
        self,
        exc_type: Type[BaseException],
        exc_value: Exception,
        traceback: Type[TracebackType],
    ) -> bool:
        return True


"""
1) As a generator
"""


@contextmanager
def supressing(*exceptions: Type[BaseException]) -> Generator:
    try:
        yield
    except exceptions:
        pass
