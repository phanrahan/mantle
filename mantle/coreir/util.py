import magma as m
from hwtypes import SIntVector, UIntVector


_default_port_mapping = {
    "I": "in",
    "I0": "in0",
    "I1": "in1",
    "O": "out",
    "S": "sel",
    "CLK": "clk",
}


def DeclareCoreirCircuit(*args, **kwargs):
    name_ = args[0]
    decl = args[1:]
    assert isinstance(name_, str)
    assert len(decl) % 2 == 0

    class _Circuit(m.Circuit):
        name = name_
        io = m.IO(**dict(zip(decl[::2], decl[1::2])))
        renamed_ports = _default_port_mapping

    kwargs.setdefault("primitive", True)
    kwargs.setdefault("stateful", False)
    kwargs.setdefault("_is_definition", False)
    for k, v in kwargs.items():
        setattr(_Circuit, k, v)

    return _Circuit


def get_int_vector_type(signed):
    return SIntVector if signed else UIntVector
