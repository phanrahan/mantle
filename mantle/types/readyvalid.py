import magma as m

#Expects data to be "output" or not directional
def ReadyValid(data):
  return m.Tuple(
    ready=m.In(m.Bit),
    valid=m.Out(m.Bit),
    data=m.Out(data),
  )
