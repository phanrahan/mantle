import os
import os
import pytest
coreir = pytest.importorskip("coreir")
from magma import *
from magma.testing import check_files_equal
from mantle.coreir import DefineMemory


# def test_coreir_rom():
#     mem = DefineMemory(4, 16, readonly=False)
#     print(repr(mem))
#     compile("build/test_coreir_rom", mem, output="coreir")
#     assert check_files_equal(__file__,
#             "build/test_coreir_rom.json", "gold/test_coreir_rom.json")
