import magma as m
from magma.backend import verilog
import mantle.coreir


def get_mantle_define_circuit(name):
    return getattr(mantle.coreir, "Define{}".format(name))


def bits_binop_test_factory(name, op):
    def _test():
        circ = get_mantle_define_circuit(name)(1)
        assert verilog.compile(circ) == """
module {name}1 (input  I0, input  I1, output  O);
coreir_{op} #(.WIDTH=1) {name}1(.in0(I0), .in1(I1), .out(O));
endmodule

""".format(name=name, op=op).lstrip()
        circ = get_mantle_define_circuit(name)(2)
        assert verilog.compile(circ) == """
module {name}2 (input [1:0] I0, input [1:0] I1, output [1:0] O);
coreir_{op} #(.WIDTH=2) {name}2(.in0(I0), .in1(I1), .out(O));
endmodule

""".format(name=name, op=op).lstrip()
    return _test


test_and = bits_binop_test_factory("And", "and")
test_or = bits_binop_test_factory("Or", "or")
test_xor = bits_binop_test_factory("Xor", "xor")


def test_invert():
    Invert1 = mantle.coreir.DefineInvert(1)
    assert verilog.compile(Invert1) == """
module Invert1 (input  I, output  O);
coreir_not #(.WIDTH=1) Invert1(.in(I), .out(O));
endmodule

""".lstrip()
    Invert2 = mantle.coreir.DefineInvert(2)
    assert verilog.compile(Invert2) == """
module Invert2 (input [1:0] I, output [1:0] O);
coreir_not #(.WIDTH=2) Invert2(.in(I), .out(O));
endmodule

""".lstrip()


def shift_factory(direction, op, dynamic_op):
    def _test():
        circ = get_mantle_define_circuit("Shift" + direction)(2, 1)
        assert verilog.compile(circ) == """
module Shift{direction}2_1 (input [1:0] I, output [1:0] O);
coreir_{} #(.WIDTH=2, .SHIFTBITS=1) Shift{direction}2_1(.in(I), .out(O));
endmodule

""".format(op, direction=direction).lstrip()
        circ = get_mantle_define_circuit("Shift" + direction)(4, 2)
        assert verilog.compile(circ) == """
module Shift{direction}4_2 (input [3:0] I, output [3:0] O);
coreir_{} #(.WIDTH=4, .SHIFTBITS=2) Shift{direction}4_2(.in(I), .out(O));
endmodule

""".format(op, direction=direction).lstrip()

    def _test_dynamic():
        circ = get_mantle_define_circuit("DynamicShift" + direction)(2)
        assert verilog.compile(circ) == """
module DynamicShift{direction}2 (input [1:0] I0, input [1:0] I1, output [1:0] O);
coreir_{} #(.WIDTH=2) DynamicShift{direction}2(.in0(I0), .in1(I1), .out(O));
endmodule

""".format(dynamic_op, direction=direction).lstrip()  # NOQA

    return _test, _test_dynamic


test_shift_left, test_dynamic_shift_left = shift_factory("Left", "shl", "dshl")
test_shift_right, test_dynamic_shift_right = shift_factory("Right", "shr", "dlshr")  # NOQA


def binop_test_factory(name, op, signed=False):
    def _test():
        circ = get_mantle_define_circuit(name)(1)
        assert verilog.compile(circ) == """
module {name}1 (input [0:0] I0, input [0:0] I1, output [0:0] O);
coreir_{op} #(.WIDTH=1) {name}1(.in0(I0), .in1(I1), .out(O));
endmodule

""".format(name=name, op=op).lstrip()  # NOQA
        circ = get_mantle_define_circuit(name)(2)
        assert verilog.compile(circ) == """
module {name}2 (input [1:0] I0, input [1:0] I1, output [1:0] O);
coreir_{op} #(.WIDTH=2) {name}2(.in0(I0), .in1(I1), .out(O));
endmodule

""".format(name=name, op=op).lstrip()  # NOQA
    return _test


test_unsigned_add = binop_test_factory("UnsignedAdd", "add")
test_unsigned_sub = binop_test_factory("UnsignedSub", "sub")
test_unsigned_mul = binop_test_factory("UnsignedMul", "mul")
test_unsigned_div = binop_test_factory("UnsignedDiv", "div")

# test_signed_add = binop_test_factory("SignedAdd", "+", signed=True)
# test_signed_sub = binop_test_factory("SignedSub", "-", signed=True)
# test_signed_mul = binop_test_factory("SignedMul", "*", signed=True)
# test_signed_div = binop_test_factory("SignedDiv", "/", signed=True)


def comparison_test_factory(name, op, signed=False):
    def _test():
        circ = get_mantle_define_circuit(name)(1)
        assert verilog.compile(circ) == """
module {name}1 (input [0:0] I0, input [0:0] I1, output  O);
coreir_{op} #(.WIDTH=1) {name}1(.in0(I0), .in1(I1), .out(O));
endmodule

""".format(name=name, op=op).lstrip()
        circ = get_mantle_define_circuit(name)(2)
        assert verilog.compile(circ) == """
module {name}2 (input [1:0] I0, input [1:0] I1, output  O);
coreir_{op} #(.WIDTH=2) {name}2(.in0(I0), .in1(I1), .out(O));
endmodule

""".format(name=name, op=op).lstrip()
    return _test


test_unsigned_lt = comparison_test_factory("UnsignedLt", "ult")
test_unsigned_lte = comparison_test_factory("UnsignedLtE", "ule")
test_unsigned_gt = comparison_test_factory("UnsignedGt", "ugt")
test_unsigned_gte = comparison_test_factory("UnsignedGtE", "uge")

# test_signed_lt = comparison_test_factory("SignedLt",   "<",  signed=True)
# test_signed_lte = comparison_test_factory("SignedLtE", "<=", signed=True)
# test_signed_gt = comparison_test_factory("SignedGt",   ">",  signed=True)
# test_signed_gte = comparison_test_factory("SignedGtE", ">=", signed=True)
