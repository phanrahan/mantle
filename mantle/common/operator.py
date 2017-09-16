from magma import *
from mantle import And

def get_length(value):
    if isinstance(value, (BitType, ClockType, EnableType, ResetType)):
        return None
    elif isinstance(value, ArrayType):
        return len(value)
    else:
        raise NotImplementedError("Cannot get_length of"
                " {}".format(type(value)))


def and_(*args, **kwargs):
    width = get_length(args[0])
    if not all(get_length(x) == width for x in args):
        raise ValueError("All arguments should have the same length")
    return And(len(args), width, **kwargs)(*args)
