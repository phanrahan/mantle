import magma as m
from mantle import DefineRegister


def _make_read_type(data_width, addr_width):
    fields = dict(data=m.Out(m.Bits[data_width]), addr=m.In(m.Bits[addr_width]))
    return m.Product.from_fields("ReadPortT", fields)


def _make_write_type(data_width, addr_width):
    fields = dict(data=m.In(m.Bits[data_width]), addr=m.In(m.Bits[addr_width]))
    return m.Product.from_fields("WritePortT", fields)


class RegFileBuilder(m.CircuitBuilder):
    def __init__(self, name, height: int, width: int):
        super().__init__(name)
        self._data_width = width
        self._height = height
        self._addr_width = m.bitutils.clog2(height)
        self._read_ports = []
        self._write_ports = []
        self._readT = _make_read_type(self._data_width, self._addr_width)
        self._writeT = _make_write_type(self._data_width, self._addr_width)
        clocks = m.ClockInterface(has_async_reset=True)
        for name, typ in zip(clocks[::2], clocks[1::2]):
            self._add_port(name, typ)

    @m.builder_method
    def __getitem__(self, addr):
        """Add a read port"""
        count = len(self._read_ports)
        name = f"read_{count}"
        self._add_port(name, self._readT)
        self._read_ports.append(name)
        port = getattr(self, name)
        m.wire(addr, port.addr)
        return port.data

    @m.builder_method
    def __setitem__(self, addr, data):
        """Add a write port"""
        count = len(self._write_ports)
        name = f"write_{count}"
        self._add_port(name, self._writeT)
        self._write_ports.append(name)
        port = getattr(self, name)
        m.wire(addr, port.addr)
        m.wire(data, port.data)

    @m.builder_method
    def _finalize(self):
        registers = [DefineRegister(self._data_width, has_async_reset=True)()
                     for _ in range(self._height)]
        for name in self._read_ports:
            port = self._port(name)
            mux = m.operators.Mux(self._height, m.Bits[self._data_width])()
            values = [reg.O for reg in registers]
            port.data @= mux(*values, port.addr)
        for name in self._write_ports:
            port = self._port(name)
            for i, reg in enumerate(registers):
                if reg.I.driven():
                    value = reg.I.value()
                    reg.I.unwire(value)
                else:
                    value = reg.O
                mux = m.operators.Mux(2, m.Bits[self._data_width])()
                sel = port.addr == i
                reg.I @= mux(value, port.data, sel)
            for name in self._read_ports:  # forward write
                read_port = self._port(name)
                value = read_port.data.value()
                read_port.data.unwire(value)
                mux = m.operators.Mux(2, m.Bits[self._data_width])()
                sel = port.addr == read_port.addr
                read_port.data @= mux(value, port.data, sel)
