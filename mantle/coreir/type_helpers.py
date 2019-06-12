from magma.frontend.coreir_ import DefineCircuitFromGeneratorWrapper, GetCoreIRBackend
from magma import cache_definition

@cache_definition
def DefineTerm(width: int):
    """
    Take in an array of wires and connect it to nothing so that you don't get an unconnected
    Returns a circuit definition.

    :param cirb: The CoreIR backend currently be used
    :param width: The width of the element to absorb
    :return:
    """
    return DefineCircuitFromGeneratorWrapper(GetCoreIRBackend(), "coreir", "term", "term_w" + str(width), ["global"],
                                               {"width": width})
def Term(width: int):
    """
    Take in an array of wires and connect it to nothing so that you don't get an unconnected
    Returns an instance of a circuit definition.

    :param cirb: The CoreIR backend currently be used
    :param width: The width of the element to absorb
    :return:
    """
    return DefineTerm(width)()
