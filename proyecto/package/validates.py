def validate_tiny_int(value):
    return value >= 0 and value <= 255


def validate_value(value):
    try:
        return isinstance(int(value), int)
    except ValueError as error:
        return False
