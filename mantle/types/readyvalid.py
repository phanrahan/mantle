import magma as m
from collections import OrderedDict

#Expects data to be "output" or not directional
#Can specifify the name of the data and if you want the data 'flattened' in the tuple
def ReadyValid(data,flatten=False,data_name="data"):
  vals = OrderedDict()
  vals["ready"] = m.In(m.Bit),
  vals["valid"] = m.Out(m.Bit),
  if flatten:
    assert isinstance(a,m.TupleKind)
    for k in data.Ks:
      assert k != "ready" and k != "valid"
      vals[k] = data[k]
  else:
    vals[data_name] = m.Out(data)
  return m.Tuple(vals)
