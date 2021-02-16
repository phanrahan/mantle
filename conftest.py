import pytest
import magma

def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="coreir")

def pytest_configure(config):
    target = config.getoption('--target')
    magma.set_mantle_target(target)

def pytest_collection_modifyitems(items):
    for item in items:
        if   "mantle3" in item.nodeid or "spartan3" in item.nodeid:
            item.add_marker(pytest.mark.spartan3)
        elif "mantle6" in item.nodeid or "spartan6" in item.nodeid:
            item.add_marker(pytest.mark.spartan6)
        elif "mantle40" in item.nodeid or "ice40" in item.nodeid:
            item.add_marker(pytest.mark.ice40)
        elif "verilog" in item.nodeid:
            item.add_marker(pytest.mark.verilog)
        else:
            item.add_marker(pytest.mark.coreir)


@pytest.fixture(autouse=True)
def mantle_test():
    """
    Clear the circuit cache before running, allows name reuse across tests
    without collisions
    """
    import magma.config
    magma.config.set_compile_dir('callee_file_dir')

    from magma import clear_cachedFunctions
    clear_cachedFunctions()

    magma.frontend.coreir_.ResetCoreIR()
    magma.generator.reset_generator_cache()
