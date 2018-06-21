# content of conftest.py
import sys
import pytest
from magma.circuit import magma_clear_circuit_cache
from magma import clear_cachedFunctions


@pytest.fixture(autouse=True)
def mantle_test():
    """
    Clear the circuit cache before running, allows name reuse across tests
    without collisions
    """
    import magma.config
    magma.config.set_compile_dir('callee_file_dir')
    magma_clear_circuit_cache()
    clear_cachedFunctions()
