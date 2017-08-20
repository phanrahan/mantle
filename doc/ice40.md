# Lattice ICE40

These functions are specific to the Lattice ICE40 Devices.

## Combinational Lofic

### LUTS

```
SB_LUT4() :: I0:In(Bit), I1:In(Bit), I2:In(Bit), I3:In(Bit), O:Out(Bit)
```

The LUT is initialized by setting the parameter INIT.

### Carry 

```
SB_CARRY() :: I0:In(Bit), I1:In(Bit), CI:In(Bit), CO:Out(Bit)
```

This functional unit computes the carry out give
3 inputs, including the carry in from the previous logic cell.

```
CO = (I0&I1)|(I1&CI)|(CI&I0)
```

### Flip-Flops

```
SB_DFF() :: C:In(bit), D:In(Bit), Q:Out(Bit)
```

```
# DFF w/ Clock enable
SB_DFFE() :: C:In(Bit), E:In(Bit), D:In(Bit), Q:Out(Bit)
# DFF w/ Synchronous Reset
SB_DFFSR() :: C:In(Bit), R:In(Bit), D:In(Bit), Q:Out(Bit)
# DFF w/ Asynchronous Reset
SB_DFFR() :: C:In(Bit), R:In(Bit), D:In(Bit), Q:Out(Bit)
# DFF w/ Synchronous Set
SB_DFFSS() :: C:In(Bit), S:In(Bit), D:In(Bit), Q:Out(Bit)
# DFF w/ Asynchronous Set
SB_DFFS() :: C:In(Bit), S:In(Bit), D:In(Bit), Q:Out(Bit)
# DFF w/ Synchronous Reset, Clock enable
SB_DFFESR() :: C:In(Bit), E:In(Bit), R:In(Bit), D:In(Bit), Q:Out(Bit)
# DFF w/ Asynchronous Reset, Clock enable
SB_DFFER() :: C:In(Bit), E:In(Bit), R:In(Bit), D:In(Bit), Q:Out(Bit)
# DFF w/ Synchronous Set, Clock enable
SB_DFFESS() :: C:In(Bit), E:In(Bit), S:In(Bit), D:In(Bit), Q:Out(Bit)
# DFF w/ Asynchronous Set, Clock enable
SB_DFFES() :: C:In(Bit), E:In(Bit), S:In(Bit), D:In(Bit), Q:Out(Bit)
```

### Blocked RAM
```
ram = SB_RAM40_4K() ::
    RDATA:Out(Bits(16)),
    RADDR:In(Bits(11)),
    RCLK:In(Bit),
    RCLKE:In(Bit),
    RE:In(Bit),
    WCLK:In(Bit),
    WCLKE:In(Bit),
    WE:In(Bit),
    WADDR:In(Bits(11)),
    MASK:In(Bits(16)),
    WDATA:In(Bits(16)),
```

### IO

```
SB_IO() ::
    CLOCK_ENABLE:In(Bit),
    INPUT_CLOCK':In(Bit),
    OUTPUT_CLOCK':In(Bit),
    OUTPUT_ENABLE':In(Bit),
    LATCH_INPUT_VALUE':In(Bit),
    D_IN_0':In(Bit), # rising
    D_IN_1':In(Bit), # falling
    PACKAGE_PIN: InOut(Bit) 
    D_OUT_0':Out(Bit), # rising
    D_OUT_1':Bit, # falling
    PACKAGE_PIN: Bit # inout
```

This primitive is controlled using the parameter `PIN_TYPE`.
