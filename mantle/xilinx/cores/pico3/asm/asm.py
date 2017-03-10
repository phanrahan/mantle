import sys
from .arch import Arch


def instDump(arch, inst):
    args = inst.args

    syms = [arg['sym'] for arg in args]

    print "def", inst.action, "(", ", ".join(syms), "):"

    for arg in args:
        sym = arg['sym']
        n = arg['length']
        if arg['signed']:
            print '   ', sym, '= checks (', sym, ',', n, ')'
        else:
            print '   ', sym, '= checku (', sym, ',', n, ')'

    s = '    emit( ' + hex(inst.bits)

    for arg in args:
        sym = arg['sym']
        shift = arg['start'] - arg['length']
        s += ' | ' + '(' + sym + '<<' + ("%d" % shift) + ')'

    s += ' )'

    print s


if len(sys.argv) != 2:
    print 'usage: python asm.py proc.arch > proc.mas'
    sys.exit(1)


lines = open(sys.argv[1]).readlines()

arch = Arch(lines)

print "from tiny import *"
print

for inst in arch.instructions:
    # print inst.pattern, inst.bitlength,
    # print "%x" % inst.bits,
    # print "%x" % inst.mask
    # for a in inst.args:
    #    print "  ", a

    instDump(arch, inst)

    print
