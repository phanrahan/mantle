import magma as m


def wrap(circ):
    _IO = []
    for key, value in circ.IO.items():
        _IO += [key, value]

    class Wrapper(m.Circuit):
        name = f"{circ.name}_wrapped"
        IO = _IO

        @classmethod
        def definition(io):
            inst = circ()
            for name in circ.IO:
                m.wire(getattr(inst, name), getattr(io, name))

    return Wrapper
