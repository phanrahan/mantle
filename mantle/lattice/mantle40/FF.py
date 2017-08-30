from collections import Sequence
from magma import *
from ..ice40.PLB import *
from .LUT import LUT2, LUT3
from .logic import Not

__all__   = ['DFF', 'SRFF', 'RSFF', 'JKFF', 'TFF']
__all__  += ['FF']

#
# TODO: add async=True, edge=True (also negedge)
#
def DFF(init=0, has_ce=False, has_reset=False, has_set=False, edge=True, sync=True, **kwargs):

    assert not (has_reset and has_set)

    # By default
    #  not connecting a wire to D defaults to 0
    #  not connecting a wire to C defaults to 0
    #  not connecting a wire to R defaults to 0
    #  not connecting a wire to E defaults to 1
    #   this is better than connecting a 1 to E, 
    #   which causes that signal to be generated
    if edge:
        # rising edge
        if sync:
            # synchronous reset
            if has_ce:
                if   has_reset:
                    ff = SB_DFFESR(**kwargs)
                elif has_set:
                    ff = SB_DFFESS(**kwargs)
                else:
                    ff = SB_DFFE(**kwargs)
            else:
                if   has_reset:
                    ff = SB_DFFSR(**kwargs)
                elif has_set:
                    ff = SB_DFFSS(**kwargs)
                else:
                    ff = SB_DFF(**kwargs)
        else:
            # asynchronous reset
            if has_ce:
                if   has_reset:
                    ff = SB_DFFER(**kwargs)
                elif has_s:
                    ff = SB_DFFES(**kwargs)
                else:
                    ff = SB_DFFE(**kwargs)
            else:
                if   has_reset:
                    ff = SB_DFFR(**kwargs)
                elif has_set:
                    ff = SB_DFFS(**kwargs)
                else:
                    ff = SB_DFF(**kwargs)
    else:
        # falling edge
        if sync:
            # synchronous reset
            if has_ce:
                if   has_reset:
                    ff = SB_DFFNESR(**kwargs)
                elif has_set:
                    ff = SB_DFFNESS(**kwargs)
                else:
                    ff = SB_DFFNE(**kwargs)
            else:
                if   has_reset:
                    ff = SB_DFFNSR(**kwargs)
                elif has_set:
                    ff = SB_DFFNSS(**kwargs)
                else:
                    ff = SB_DFFN(**kwargs)
        else:
            # asynchronous reset
            if has_ce:
                if   has_reset:
                    ff = SB_DFFNER(**kwargs)
                elif has_set:
                    ff = SB_DFFNES(**kwargs)
                else:
                    ff = SB_DFFNE(**kwargs)
            else:
                if   has_reset:
                    ff = SB_DFFNR(**kwargs)
                elif has_set:
                    ff = SB_DFFNS(**kwargs)
                else:
                    ff = SB_DFFN(**kwargs)

    I = ff.D
    O = ff.Q

    # ice40 flip-flops are always initialized to 0
    if init:
        # if init=1, then insert Not before and after the flip-flop
        luti = Not()
        luto = Not()
        wire(luti.O, ff.D)
        wire(ff.Q, luto.I0)
        I = luti.I0
        O = luto.O

    args = ['I', I, 'CLK', ff.C]
    if has_ce:
        args += ['CE', ff.E]
    if has_reset:
        args += ['RESET', ff.R]
    if has_set:
        args += ['SET', ff.S]

    args += ['O', O]

    return AnonymousCircuit(args)

FF = DFF


def SRFF(init=0, has_ce=False, edge=True, sync=True, **kwargs):

    """A S-R flip-flop."""

    dff = FF( init=init, has_ce=has_ce, edge=edge, sync=sync, **kwargs)
    lut = LUT3( (~I1&~I2&I0)|(I1&~I2), **kwargs )
    dff(lut)

    wire(dff.O, lut.I0)

    args = []
    if has_ce:
        args += ['input CE', dff.CE]
    args += ["S", lut.I1, "R", lut.I2, 'CLK', dff.CLK, "O", dff.O]

    return AnonymousCircuit(args)



def RSFF(init=0, has_ce=False, edge=True, sync=True, **kwargs):

    """A R-S flip-flop."""

    dff = FF( init=init, has_ce=has_ce, edge=edge, sync=sync, **kwargs)
    lut = LUT3( (~I1&~I2&I0)|(I1&~I2), **kwargs )
    dff(lut)

    wire(dff.O, lut.I0)

    args = []
    if has_ce:
        args += ['input CE', dff.CE]
    args += ["R", lut.I2, "S", lut.I1, 'CLK', dff.CLK, "O", dff.O]

    return AnonymousCircuit(args)


def JKFF(has_ce=False, has_reset=False, has_set=False, edge=True, sync=True, **kwargs):

    """A J-K flip-flop."""

    dff = FF(has_ce=has_ce, has_reset=has_reset, has_set=has_set, edge=edge, sync=sync, **kwargs)
    lut = LUT3( (~I0&I1)|(I0&~I2), **kwargs )
    dff(lut)

    wire(dff.O, lut.I0)

    args = ["J", lut.I1, "K", lut.I2, "O", dff.O, 'CLK', dff.CLK]
    if has_ce:     args += ['CE', dff.CE]
    if has_reset:  args += ['RESET', dff.R]
    if has_set:    args += ['SET', dff.S]
    return AnonymousCircuit(*args)


def TFF(has_ce=False, has_reset=False, has_set=False, edge=True, sync=True, **kwargs):

    """A T flip-flop."""

    tff = FF(has_ce=has_ce, has_reset=has_reset, has_set=has_set, edge=edge, sync=sync, **kwargs)
    lut = LUT2( I0^I1, **kwargs )
    tff(lut)

    wire(tff.O, lut.I0)

    args = ["I", lut.I1, "O", tff.O, "CLK", tff.CLK]
    if has_ce:    args += ['CE', dff.CE]
    if has_reset: args += ['RESET', dff.R]
    if has_set:   args += ['SET', dff.S]
    return AnonymousCircuit(*args)

