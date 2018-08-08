from magma import *
from collections import OrderedDict

#Expects data to be "output" or not directional
#Can specifify the name of the data and if you want the data 'flattened' in the tuple
def ReadyValid(data,flatten=False,data_name="data"):
  vals = OrderedDict()
  vals["ready"] = In(Bit)
  vals["valid"] = Out(Bit)
  if flatten:
    assert isinstance(data,TupleKind)
    for k in data.Ks:
      assert k != "ready" and k != "valid"
      vals[k] = Out(data[k])
  else:
    vals[data_name] = Out(data)
  return Tuple(vals)
