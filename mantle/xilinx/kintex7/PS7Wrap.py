from magma import *

__all__ = ['PS7Wrap']

def PS7Wrap():

    PS7Path = os.path.dirname(__file__) + "/vsrc/"
    vlibs = [PS7Path+"ps7_wrap.v",PS7Path+"axi_master_stub.v",PS7Path+"axi_master32_stub.v",PS7Path+"axi_slave_stub.v"]

    verilogFile = PS7Path + "ps7_stub.v"

    ps7 = DefineCircuit("ps7_stub",
    "inout MIO", Array(54,Bit),
    "output DDR_WEB", Bit,
    "inout DDR_VRP", Bit,
    "inout DDR_VRN", Bit,
    "inout DDR_RAS_n", Bit,
    "inout DDR_ODT", Bit,
    "inout DDR_DRSTB", Bit,
    "inout DDR_DQS", Array(4,Bit),
    "inout DDR_DQS_n", Array(4,Bit),
    "inout DDR_DQ", Array(32,Bit),
    "inout DDR_DM", Array(4,Bit),
    "inout DDR_CS_n", Bit,
    "inout DDR_CKE", Bit,
    "inout DDR_Clk", Bit,
    "inout DDR_Clk_n", Bit,
    "inout DDR_CAS_n", Bit,
    "inout DDR_BankAddr", Array(3,Bit),
    "inout DDR_Addr", Array(15,Bit),
    "inout PS_PORB", Bit,
    "inout PS_SRSTB", Bit,
    "inout PS_CLK", Bit,
    "output CLK", Bit,
    "output RST_n", Bit
    )
    with open(verilogFile,'r') as verilog:
        ps7.verilog=verilog.read()
    ps7.verilogLib = vlibs
    EndCircuit()
    
    return ps7
