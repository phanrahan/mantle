from magma import *
import magma as m


@circuit_generator
def DeclareAdd(N, cin=False, cout=False):
    has_cin = cin
    has_cout = cout
    T = Bits[N]
    IO_ = ['I0', In(T), 'I1', In(T), 'O', Out(T)]
    name_ = "Add{}".format(N)
    if has_cout:
        IO_ += ['COUT', Out(Bit)]
        name_ += "_cout"
    if has_cin:
        IO_ += ['CIN', In(Bit)]
        name_ += "_cin"
    class Add(Circuit):
        # Underscores because there's some weird scoping issue here with Python
        # when trying to capture name and IO
        name = name_
        IO = IO_
    return Add


def add(*args, **kwargs):
    width = get_length(args[0])
    if not all(get_length(arg) == width for arg in args):
        # TODO: Something more specific than a ValueError?
        raise ValueError("Arguments to add should all be the same width")
    if not all(isinstance(arg, BitsType) for arg in args):
        # TODO: Something more specific than a ValueError?
        raise ValueError("Arguments to add should be all Bits"
                " {}".format([(arg, type(arg)) for arg in args]))
    adders = [Add(width, **kwargs) for _ in range(len(args) - 1)]
    curr = adders[0]
    wire(args[0], curr.I0)
    wire(args[1], curr.I1)
    if len(args) > 2:
        next_ = adders[1]
        for i in range(1, len(adders)):
            next_ = adders[i]
            wire(curr.O, next_.I0)
            wire(args[i + 1], next_.I1)
            curr = next_
    return curr.O


@circuit_generator
def DeclareSub(N, cin=False, cout=False, T=m.Bits):
    has_cin = cin
    has_cout = cout
    T = T[N]
    IO_ = ['I0', In(T), 'I1', In(T), 'O', Out(T)]
    name_ = "Sub{}".format(N)
    if has_cout:
        IO_ += ['COUT', Out(Bit)]
        name_ += "_cout"
    if has_cin:
        IO_ += ['CIN', In(Bit)]
        name_ += "_cin"
    class Sub(Circuit):
        # Underscores because there's some weird scoping issue here with Python
        # when trying to capture name and IO
        name = name_
        IO = IO_
    return Sub


def sub(*args, **kwargs):
    width = get_length(args[0])
    if not all(get_length(arg) == width for arg in args):
        # TODO: Something more specific than a ValueError?
        raise ValueError("Arguments to sub should all be the same width")
    if not all(isinstance(arg, BitsType) for arg in args):
        # TODO: Something more specific than a ValueError?
        raise ValueError("Arguments to sub should be all Bits"
                " {}".format([(arg, type(arg)) for arg in args]))
    subbers = [Sub(width, **kwargs) for _ in range(len(args) - 1)]
    curr = subbers[0]
    wire(args[0], curr.I0)
    wire(args[1], curr.I1)
    if len(args) > 2:
        next_ = subbers[1]
        for i in range(1, len(subbers)):
            next_ = subbers[i]
            wire(curr.O, next_.I0)
            wire(args[i + 1], next_.I1)
            curr = next_
    return curr.O

def DeclareNegate(width):
    T = Bits[width]
    class _Negate(Circuit):
        name = 'Negate{}'.format(width)
        IO = ['I', In(T), 'O', Out(T)]
    return _Negate


def DeclareASR(width):
    T = Bits[width]
    class _ASR(Circuit):
        name = 'ASR{}'.format(width)
        IO = ["I0", In(T), "I1", In(T), "O", Out(T)]
    return _ASR
