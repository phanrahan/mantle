import magma as m
from mantle.coreir import DefineRegister


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
        self._enable_ports = {}
        self._readT = _make_read_type(self._data_width, self._addr_width)
        self._writeT = _make_write_type(self._data_width, self._addr_width)
        clocks = m.ClockIO(has_async_reset=True).decl()
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

    def _add_write_port(self, addr, data):
        """Add a write port"""
        count = len(self._write_ports)
        name = f"write_{count}"
        self._add_port(name, self._writeT)
        self._write_ports.append(name)
        port = getattr(self, name)
        m.wire(addr, port.addr)
        m.wire(data, port.data)
        return name

    @m.builder_method
    def __setitem__(self, addr, data):
        self._add_write_port(addr, data)

    def _add_enable(self, port_name, enable):
        enable_name = f"{port_name}_en"
        self._add_port(enable_name, m.In(m.Enable))
        self._enable_ports[port_name] = enable_name
        port = getattr(self, enable_name)
        m.wire(enable, port)

    @m.builder_method
    def write(self, addr, data, enable=None):
        name = self._add_write_port(addr, data)
        if enable is not None:
            self._add_enable(name, enable)

    @m.builder_method
    def _finalize(self):
        registers = [DefineRegister(self._data_width, has_async_reset=True)()
                     for _ in range(self._height)]
        read_data = {name: None for name in self._read_ports}
        for name in self._read_ports:
            port = self._port(name)
            mux = m.Mux(self._height, m.Bits[self._data_width])()
            values = [reg.O for reg in registers]
            read_data[name] = mux(*values, port.addr)
        reg_data = [reg.O for reg in registers]
        for name in self._write_ports:
            port = self._port(name)
            enable = None
            if name in self._enable_ports:
                enable = m.bit(self._port(self._enable_ports[name]))
            for i, reg in enumerate(registers):
                mux = m.Mux(2, m.Bits[self._data_width])()
                cond = port.addr == i
                if enable is not None:
                    cond &= enable
                reg_data[i] = mux(reg_data[i], port.data, cond)
            for read_name in self._read_ports:  # forward write
                read_port = self._port(read_name)
                mux = m.Mux(2, m.Bits[self._data_width])()
                cond = port.addr == read_port.addr
                if enable is not None:
                    cond &= enable
                read_data[read_name] = mux(read_data[read_name], port.data,
                                           cond)
        # Commit staged reads and writes.
        for i, reg in enumerate(registers):
            reg.I @= reg_data[i]
        for name in self._read_ports:
            port = self._port(name)
            port.data @= read_data[name]
