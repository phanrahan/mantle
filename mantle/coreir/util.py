import magma as m

default_port_mapping = {
    "I": "in",
    "I0": "in0",
    "I1": "in1",
    "O": "out",
    "S": "sel",
}


def DefineCoreirCircuit(*args, **kwargs):
    return m.DefineCircuit(*args, **kwargs,
                           renamed_ports=default_port_mapping)


def DeclareCoreirCircuit(*args, **kwargs):
    return m.DeclareCircuit(*args, **kwargs,
                            renamed_ports=default_port_mapping)
