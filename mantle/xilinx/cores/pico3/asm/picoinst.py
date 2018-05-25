from inst import *

# invb(ra,bitmask)
#   xori(ra, bitmask)
# clrb(ra,bitmask)
#   andi(ra,~bitmask)
# setb(ra,bitmask)
#   ori(ra,bitmask)
#
# clear carry
#   movi(ra,0)
#   cmpi(ra,0)
# set carry
#   movi(ra,0)
#   cmpi(ra,1)


def nop():
    mov(r0, r0)


def _not(a):
    xori(a, 0xff)


def inc(a):
    addi(a, 1)


def dec(a):
    subi(a, 1)
