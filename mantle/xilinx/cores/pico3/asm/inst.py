from .tiny import *


def movi(a, i):
    a = checku(a, 4)
    i = checks(i, 8)
    emit(0x2000 | (a << 8) | (i << 0))


def mov(a, b):
    a = checku(a, 4)
    b = checku(b, 4)
    emit(0x3000 | (a << 8) | (b << 4))


def ori(a, i):
    a = checku(a, 4)
    i = checks(i, 8)
    emit(0x6000 | (a << 8) | (i << 0))


def or_(a, b):
    a = checku(a, 4)
    b = checku(b, 4)
    emit(0x7000 | (a << 8) | (b << 4))


def andi(a, i):
    a = checku(a, 4)
    i = checks(i, 8)
    emit(0xa000 | (a << 8) | (i << 0))


def and_(a, b):
    a = checku(a, 4)
    b = checku(b, 4)
    emit(0xb000 | (a << 8) | (b << 4))


def xori(a, i):
    a = checku(a, 4)
    i = checks(i, 8)
    emit(0xe000 | (a << 8) | (i << 0))


def xor(a, b):
    a = checku(a, 4)
    b = checku(b, 4)
    emit(0xf000 | (a << 8) | (b << 4))


def tsti(a, i):
    a = checku(a, 4)
    i = checks(i, 8)
    emit(0x8000 | (a << 8) | (i << 0))


def tst(a, b):
    a = checku(a, 4)
    b = checku(b, 4)
    emit(0x9000 | (a << 8) | (b << 4))


def addi(a, i):
    a = checku(a, 4)
    i = checks(i, 8)
    emit(0x12000 | (a << 8) | (i << 0))


def add(a, b):
    a = checku(a, 4)
    b = checku(b, 4)
    emit(0x13000 | (a << 8) | (b << 4))


def adci(a, i):
    a = checku(a, 4)
    i = checks(i, 8)
    emit(0x16000 | (a << 8) | (i << 0))


def adc(a, b):
    a = checku(a, 4)
    b = checku(b, 4)
    emit(0x17000 | (a << 8) | (b << 4))


def subi(a, i):
    a = checku(a, 4)
    i = checks(i, 8)
    emit(0x1a000 | (a << 8) | (i << 0))


def sub(a, b):
    a = checku(a, 4)
    b = checku(b, 4)
    emit(0x1b000 | (a << 8) | (b << 4))


def sbci(a, i):
    a = checku(a, 4)
    i = checks(i, 8)
    emit(0x1e000 | (a << 8) | (i << 0))


def sbc(a, b):
    a = checku(a, 4)
    b = checku(b, 4)
    emit(0x1f000 | (a << 8) | (b << 4))


def cmpi(a, i):
    a = checku(a, 4)
    i = checks(i, 8)
    emit(0x18000 | (a << 8) | (i << 0))


def cmp(a, b):
    a = checku(a, 4)
    b = checku(b, 4)
    emit(0x19000 | (a << 8) | (b << 4))


def ini(a, i):
    a = checku(a, 4)
    i = checks(i, 8)
    emit(0x20000 | (a << 8) | (i << 0))


def _in(a, b):
    a = checku(a, 4)
    b = checku(b, 4)
    emit(0x21000 | (a << 8) | (b << 4))


def outi(a, i):
    a = checku(a, 4)
    i = checks(i, 8)
    emit(0x22000 | (a << 8) | (i << 0))


def out(a, b):
    a = checku(a, 4)
    b = checku(b, 4)
    emit(0x23000 | (a << 8) | (b << 4))

C  = 1 << 10
Z  = 0 << 10
N  = 1 << 11
CC = 1 << 13

JMP = 0x38000
JMPCC = JMP | CC


def jmp(a):
    a = checku(a, 10)
    emit(JMP | a)


def jnz(a):
    a = checku(a, 10)
    emit(JMPCC | N | Z | a)


def jz(a):
    a = checku(a, 10)
    emit(JMPCC | Z | a)


def jnc(a):
    a = checku(a, 10)
    emit(JMPCC | N | C | a)


def jc(a):
    a = checku(a, 10)
    emit(JMPCC | C | a)

CALL = 0x3C000
CALLCC = CALL | CC


def call(a):
    a = checku(a, 10)
    emit(CALL | a)


def callnz(a):
    a = checku(a, 10)
    emit(CALLCC | N | Z | a)


def callz(a):
    a = checku(a, 10)
    emit(CALLCC | Z | a)


def callnc(a):
    a = checku(a, 10)
    emit(CALLCC | N | C | a)


def callc(a):
    a = checku(a, 10)
    emit(CALLC | C | a)

RET = 0x34000
RETCC = RET | CC


def ret():
    emit(RET)


def retnz():
    emit(RET | N | Z)


def retz():
    emit(RETCC | Z)


def retnc():
    emit(RETCC | N | C)


def retc():
    emit(RETCC | C)
