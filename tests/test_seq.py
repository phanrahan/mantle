import magma as m

def compile_and_check(output_file, circuit_definition, target):
    m.compile(f"build/{output_file}", circuit_definition, output=target)
    if target in ["verilog", "coreir-verilog"]:
        suffix = "v"
    elif target == "coreir":
        suffix = "json"
    else:
        raise NotImplementedError()
    assert check_files_equal(__file__, f"build/{output_file}.{suffix}",
                             f"gold/{output_file}.{suffix}")

def pytest_generate_tests(metafunc):
    if 'target' in metafunc.fixturenames:
        metafunc.parametrize("target", ["coreir", "coreir-verilog"])
    if 'async_reset' in metafunc.fixturenames:
        metafunc.parametrize("async_reset", [True, False])

def test_bug(target):
    def gen_register(T,  init : "T"):
        @m.circuit.sequential(async_reset=True)
        class Register:
            def __init__(self):
                self.value: T = T(init)

            def __call__(self, value: T, en: m.Bit) -> T:
                retvalue = self.value
                if en:
                    self.value = value
                else:
                    self.value = self.value
                return retvalue
        return Register

    Data = m.Bits[16]
    Reg = gen_register(Data, 0)

    @m.circuit.sequential(async_reset=True)
    class Accum:
        def __init__(self):
            self.reg: Reg = Reg()

        def __call__(self, in_ : Data, sel : m.Bit) -> Data:
            r = self.reg(in_, m.Bit(1))
            if sel:
                return r
            else:
                return ~r

    compile_and_check("Accum", Accum, target)
