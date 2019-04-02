import magma as m
from mantle import DefineAdd, DefineSub, DefineNegate

__all__ = [ "Add", "Sub", "Negate", "UDiv", "SDiv", "UMod", "SMod", "Mul"]


def Add(n, cin=False, cout=False, T=m.Bits, **kwargs):
    return DefineAdd(n, cin=cin, cout=cout, T=T)(**kwargs)


def Sub(n, cin=False, cout=False, T=m.Bits, **kwargs):
    return DefineSub(n, cin=cin, cout=cout, T=T)(**kwargs)


def Negate(width, **kwargs):
    return DefineNegate(width)(**kwargs)


def Mul(width, T=m.Bits, **kwargs):
    if m.mantle_target != "coreir":
        raise NotImplementedError(
            "Mul not implemented for mantle target {m.mantle_target}")
    # Workaround import error for other targets by delaying import until after
    # if guard
    from mantle import DefineMul
    return DefineMul(width, T=T)(**kwargs)


def UDiv(width, **kwargs):
    if m.mantle_target != "coreir":
        raise NotImplementedError(
            "Division not implemented for mantle target {m.mantle_target}")
    # Workaround import error for other targets by delaying import until after
    # if guard
    from mantle import DefineUDiv
    return DefineUDiv(width)(**kwargs)


def SDiv(width, **kwargs):
    if m.mantle_target != "coreir":
        raise NotImplementedError(
            "Division not implemented for mantle target {m.mantle_target}")
    # Workaround import error for other targets by delaying import until after
    # if guard
    from mantle import DefineSDiv
    return DefineSDiv(width)(**kwargs)


def UMod(width, **kwargs):
    if m.mantle_target != "coreir":
        raise NotImplementedError(
            "Modulo not implemented for mantle target {m.mantle_target}")
    # Workaround import error for other targets by delaying import until after
    # if guard
    from mantle import DefineUMod
    return DefineUMod(width)(**kwargs)


def SMod(width, **kwargs):
    if m.mantle_target != "coreir":
        raise NotImplementedError(
            "Modulo not implemented for mantle target {m.mantle_target}")
    # Workaround import error for other targets by delaying import until after
    # if guard
    from mantle import DefineSMod
    return DefineSMod(width)(**kwargs)
