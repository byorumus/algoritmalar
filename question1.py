def is_greater_than(a, b):
    """
    This function compares two given integers, returning True if first is greater.

    :param a: Integer
    :param b: Integer
    :return: Boolean
    """
    if is_negative(a) and is_negative(b) and a//b==0:
        return True
    elif a // b == 0:
        return False
    elif a == b:
        return False
    elif is_negative(a) and not is_negative(b):
        return False
    else:
        return True


def is_negative(number):
    return number < 0
