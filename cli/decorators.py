# python imports
from functools import wraps


def keyboard_interruptible(f):
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        try:
            f(self, *args, **kwargs)
        except KeyboardInterrupt:
            self.router.exit()
    return wrapper