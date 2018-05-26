from magma import *

BUFG = DeclareCircuit('BUFG', "I", In(Bit), "O", Out(Bit))

BUFGCE = DeclareCircuit('BUFGCE', "CE", In(Enable), "I", In(Bit), "O", Out(Bit))

