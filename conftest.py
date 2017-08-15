# content of conftest.py
import sys
import pytest

collect_ignore = ["setup.py"]
if sys.version_info[0] < 3:
    collect_ignore.append("tests/mantle40/test_expressions/test_expressions.py")


@pytest.fixture(autouse=True)
def mantle_test():
    """
    Clear the circuit cache before running, allows name reuse across tests
    without collisions
    """
    import magma.circuit
    magma.circuit.__magma_clear_circuit_cache()
    import magma.config
    magma.config.set_compile_dir('callee_file_dir')
