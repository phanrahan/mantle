import os
import pytest
coreir = pytest.importorskip("coreir")
from magma import *
from magma.testing import check_files_equal
from mantle.coreir import DefineMemory

CHECK_OUTPUT = os.environ.get("MANTLE_CHECK_COREIR_OUTPUT", False)


def test_coreir_rom():
    mem = DefineMemory(4, 16, readonly=False)
    print(repr(mem))
    compile("build/test_coreir_rom", mem, output="coreir")
    if CHECK_OUTPUT:
        assert check_files_equal(__file__,
                "build/test_coreir_rom.json", "gold/test_coreir_rom.json")
