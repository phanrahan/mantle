from magma.backend.coreir_ import CoreIRBackend
from magma.frontend.coreir_ import CircuitFromGeneratorWrapper

def Term(cirb: CoreIRBackend, width: int):
    """
    Take in an array of wires and connect it to nothing so that you don't get an unconnected

    :param cirb: The CoreIR backend currently be used
    :param width: The width of the element to absorb
    :return:
    """
    return CircuitFromGeneratorWrapper(cirb, "coreir", "term",
                                       ["global"],
                                       {"width": width})
