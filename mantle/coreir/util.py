import magma as m
from hwtypes import SIntVector, UIntVector

default_port_mapping = {
    "I": "in",
    "I0": "in0",
    "I1": "in1",
    "O": "out",
    "S": "sel",
    "CLK": "clk",
}


def DefineCoreirCircuit(*args, **kwargs):
    return m.DefineCircuit(*args, **kwargs,
                           renamed_ports=default_port_mapping)


def DeclareCoreirCircuit(*args, **kwargs):
    return m.DeclareCircuit(*args, **kwargs,
                            renamed_ports=default_port_mapping)


def get_int_vector_type(signed):
    return SIntVector if signed else UIntVector
