from collections.abc import Sequence
from magma import *
from ..ice40.PLB import *
from .LUT import LUT2, LUT3
from .logic import Not

__all__   = ['DefineDFF', 'DFF']
__all__  += ['SRFF', 'RSFF', 'JKFF', 'TFF']
__all__  += ['FF']

def DefineDFF(has_ce=False, has_reset=False, edge=True, sync=True):
    # has_set not supported
    has_set = False

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
                    return SB_DFFESR
                elif has_set:
                    return SB_DFFESS
                else:
                    return SB_DFFE
            else:
                if   has_reset:
                    return SB_DFFSR
                elif has_set:
                    return SB_DFFSS
                else:
                    return SB_DFF
        else:
            # asynchronous reset
            if has_ce:
                if   has_reset:
                    return SB_DFFER
                elif has_s:
                    return SB_DFFES
                else:
                    return SB_DFFE
            else:
                if   has_reset:
                    return SB_DFFR
                elif has_set:
                    return SB_DFFS
                else:
                    return SB_DFF
    else:
        # falling edge
        if sync:
            # synchronous reset
            if has_ce:
                if   has_reset:
                    return SB_DFFNESR
                elif has_set:
                    return SB_DFFNESS
                else:
                    return SB_DFFNE
            else:
                if   has_reset:
                    return SB_DFFNSR
                elif has_set:
                    return SB_DFFNSS
                else:
                    return SB_DFFN
        else:
            # asynchronous reset
            if has_ce:
                if   has_reset:
                    return SB_DFFNER
                elif has_set:
                    return SB_DFFNES
                else:
                    return SB_DFFNE
            else:
                if   has_reset:
                    return SB_DFFNR
                elif has_set:
                    return SB_DFFNS
                else:
                    return SB_DFFN

#
# TODO: add async=True, edge=True (also negedge)
#
def DFF(init=0, has_ce=False, has_reset=False, edge=True, sync=True, **kwargs):

    ff = DefineDFF(has_ce, has_reset, edge, sync)(**kwargs)

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
    #if has_set:
    #    args += ['SET', ff.S]

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
        args += ['CE', dff.CE]
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
        args += ['CE', dff.CE]
    args += ["R", lut.I2, "S", lut.I1, 'CLK', dff.CLK, "O", dff.O]

    return AnonymousCircuit(args)


def JKFF(has_ce=False, has_reset=False, edge=True, sync=True, **kwargs):

    """A J-K flip-flop."""

    dff = FF(has_ce=has_ce, has_reset=has_reset, edge=edge, sync=sync, **kwargs)
    lut = LUT3( (~I0&I1)|(I0&~I2), **kwargs )
    dff(lut)

    wire(dff.O, lut.I0)

    args = ["J", lut.I1, "K", lut.I2, "O", dff.O, 'CLK', dff.CLK]
    if has_ce:     args += ['CE', dff.CE]
    if has_reset:  args += ['RESET', dff.R]
    #if has_set:    args += ['SET', dff.S]
    return AnonymousCircuit(*args)


def TFF(has_ce=False, has_reset=False, edge=True, sync=True, **kwargs):

    """A T flip-flop."""

    tff = FF(has_ce=has_ce, has_reset=has_reset, edge=edge, sync=sync, **kwargs)
    lut = LUT2( I0^I1, **kwargs )
    tff(lut)

    wire(tff.O, lut.I0)

    args = ["I", lut.I1, "O", tff.O, "CLK", tff.CLK]
    if has_ce:    args += ['CE', dff.CE]
    if has_reset: args += ['RESET', dff.R]
    #if has_set:   args += ['SET', dff.S]
    return AnonymousCircuit(*args)

