"""
These are imported at the end

This allows targets to override the implementations of generic primitives
(e.g. DefineRAM).
"""
from mantle import DefineRAM, DefineDualRAM

__all__  = ['RAM', 'DualRAM']

def RAM(height, width, **kwargs):
    return DefineRAM(height, width)(**kwargs)

def DualRAM(height, width, **kwargs):
    return DefineDualRAM(height, width)(**kwargs)
