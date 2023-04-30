from .validates import validate_value, validate_tiny_int
from .error import TinyIntError


def tiny_int(value, call_back=None):
    try:
        if validate_value(value) and validate_tiny_int(value):
            return True
        else:
            raise TinyIntError()
    except TinyIntError as error:
        if call_back is not None:
            call_back()
        else:
            print(error)
