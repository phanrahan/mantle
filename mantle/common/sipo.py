from typing import Optional

import magma as m


def _zero_init_args(T):
    if issubclass(T, m.Tuple):
        return [v(*_zero_init_args(v)) for v in T.types()]
    if issubclass(T, m.Array):
        return [T.T(*_zero_init_args(T.T)) for _ in range(len(T))]
    return [0]


class SIPO(m.Generator2):
    def __init__(self, n: int, T: m.Kind = m.Bit, init=None,
                 has_enable: bool = False,
                 reset_type: Optional[m.AbstractReset] = None):
        if init is None:
            init = [T(*_zero_init_args(T)) for _ in range(n)]
        self.name = f"SIPO{n}"
        self.io = m.IO(
            I=m.In(T),
            O=m.Out(m.Array[n, T] if T is not m.Bit else m.Bits[n])
        )

        # TODO: Add magma helper func for this
        has_async_reset = reset_type == m.AsyncReset
        has_async_resetn = reset_type == m.AsyncResetN
        has_reset = reset_type == m.Reset
        has_resetn = reset_type == m.ResetN
        self.io += m.ClockIO(has_enable=has_enable,
                             has_async_reset=has_async_reset,
                             has_async_resetn=has_async_resetn,
                             has_reset=has_reset, has_resetn=has_resetn)

        regs = (m.Register(T, init=init[i], has_enable=has_enable,
                           reset_type=reset_type)() for i in range(n))
        # TODO: Default clock wiring logic raises warning inside scan
        self.io.O @= m.scan(regs, scanargs={"I": "O"})(self.io.I)
