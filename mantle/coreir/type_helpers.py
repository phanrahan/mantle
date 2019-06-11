from magma.frontend.coreir_ import CircuitInstanceFromGeneratorWrapper, GetCoreIRBackend
from magma import cache_definition

@cache_definition
def Term(width: int):
    """
    Take in an array of wires and connect it to nothing so that you don't get an unconnected

    :param cirb: The CoreIR backend currently be used
    :param width: The width of the element to absorb
    :return:
    """
    return CircuitInstanceFromGeneratorWrapper(GetCoreIRBackend(), "coreir", "term", "term_w" + str(width), ["global"],
                                               {"width": width})
