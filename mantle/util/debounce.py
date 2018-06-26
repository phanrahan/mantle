import magma as m
from mantle import FF, And

#
# debounce 
#  a - input signal
#  slow sets the delay
#
def debounce(a, slow):
    ffa = FF(has_ce=True)
    ffa(a, ce=slow)

    ffb = FF(has_ce=True)
    ffb(ffa.O, ce=slow)

    # return the value of a if it is stable for slow duration
    return And(2)(ffa.O, ffb.O)
