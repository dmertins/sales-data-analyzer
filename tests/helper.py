import time
from typing import Callable

MAX_WAIT = 0.5
WAIT = 0.025


def wait_for(func: Callable[[], None]) -> None:
    """Calls the received function catching AssertionError exceptions until
    the time limit is exceeded. Raises AssertionError exception."""
    start_time = time.time()
    while True:
        try:
            return func()
        except AssertionError as e:
            if time.time() - start_time > MAX_WAIT:
                raise e
            time.sleep(WAIT)
