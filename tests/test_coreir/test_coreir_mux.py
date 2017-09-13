import os
import pytest
coreir = pytest.importorskip("coreir")
from magma import *
from magma.testing import check_files_equal
from mantle.coreir import DefineMux


def test_coreir_mux_2xNone():
    mux = DefineMux(2, None)
    print(repr(mux))
    compile("build/test_coreir_mux2xNone", mux, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_mux2xNone.json", "gold/test_coreir_mux2xNone.json")


def test_coreir_mux_2x3():
    mux = DefineMux(2, 3)
    print(repr(mux))
    compile("build/test_coreir_mux2x3", mux, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_mux2x3.json", "gold/test_coreir_mux2x3.json")


def test_coreir_mux_4xNone():
    mux = DefineMux(4, None)
    print(repr(mux))
    compile("build/test_coreir_mux4xNone", mux, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_mux4xNone.json", "gold/test_coreir_mux4xNone.json")


def test_coreir_mux_4x3():
    mux = DefineMux(4, 3)
    print(repr(mux))
    compile("build/test_coreir_mux4x3", mux, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_mux4x3.json", "gold/test_coreir_mux4x3.json")
