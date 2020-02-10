## Memory

### Lookup Tables (LUTs)

The fundamental combinational primitive in an FPGA 
is a lookup-table, or LUT.
LUTs are indexed by an n-bit value.

The argument to the LUT function initializes the LUT. 
```init``` can be an int, a sequence, or an expression.

If ```init``` is a Sequence of 0s and 1s, 
each output bit in the table is initialized with those values.
An n-bit LUT is initialized with a sequence of length  2^n.
For example, to create a 2-input and gate,
```LUT2``` can be initialized to with the sequence```[0,0,0,1]```.

If ```init``` is an int, then the int is converted to a list of bits.
If the LUT contains n-bits, the sequence used to initialize is is 2^n bits.
The bit in the sequence, is set to the bit in ```init```.
For example, initializing ```LUT2``` with ```init=0x8``` 
is equivalent to initializing it to ```[0,0,0,1]```.
The 4th entry in the sequence is 1 because
the both bit in ```0x8``` is set.
All the other entries in the sequence are 0,
since all the other bits in ```init``` are cleared.
Since the number of bits depends on the size of the LUT,
using this method of initialization requires you to set
the size of the LUT by calling a LUT function with
a known numbers of bits 
(in this case, ```LUT2``` or ```LUTN(init,2)```;
you cannot call the general ```LUT``` function.

Integer expressions can also be created from python expressions.
The constants ```I0```, ```I1```, ```I2```, and ```I3``` 
have been predefined values.  
For example, ```LUT2(I0 & I1)``` will create an ```LUT```
which corresponds to a 2-input and gate.

The final way to initialize an ```LUT``` is to use a python function.
This function will be called for each input value,
and should return True or False.

The various LUT functions are shown below.
Note that we are using type signatures to indicate
the inputs and the outputs of the circuit.
For example, ```I0, I1 -> O``` 
indicates that there are two inputs named ```I0``` and ```I1```,
and a single outout ```O```.


```
lut = LUT1(init) :: I0:Bit -> O:Bit
lut = LUT2(init) :: I0:Bit, I1:Bit -> O:Bit
lut = LUT3(init) :: I0:Bit, I1:Bit, I2:Bit -> O:Bit
lut = LUT4(init) :: I0:Bit, I1:Bit, I2:Bit, I3:Bit -> O:Bit
lut = LUT5(init) :: I0:Bit, I1:Bit, I2:Bit, ..., I4:Bit -> O:Bit
lut = LUT6(init) :: I0:Bit, I1:Bit, I2:Bit, ..., I5:Bit -> O:Bit
lut = LUT7(init) :: I0:Bit, I1:Bit, I2:Bit, ..., I6:Bit -> O:Bit
lut = LUT8(init) :: I0:Bit, I1:Bit, I2:Bit, ..., I7:Bit -> O:Bit

lut = LUTN(init, n=None) :: I0:Bit, ..., In:Bit -> O:Bit
```

### ROM

```
# DefineROM :: 
#  RADDR:In(Bits(clog2(height))), 
#  RDATA:Out(Bits(width))
ROM = DefineROM(height, width)

# ROM :: 
#  RADDR:In(Bits(clog2(height))), 
#  RDATA:Out(Bits(width)),
rom = ROM(height, width) 
```

### RAM

1 read port, 1 write port RAM

```
# DefineRAM :: 
#  RADDR:In(Bits(clog2(height))), 
#  RDATA:Out(Bits(width)),
#  WADDR:In(Bits(clog2(height))), 
#  WDATA:Out(Bits(width)),
#  WE,In(Bit),
#  CLK:In(Clock)
RAM = DefineRAM(height, width)

# RAM :: 
#  RADDR:In(Bits(clog2(height))), 
#  RDATA:Out(Bits(width)),
#  WADDR:In(Bits(clog2(height))), 
#  WDATA:Out(Bits(width)),
#  WE,In(Bit),
#  CLK:In(Clock)
ram = RAM(height, width)
```

# DualRAM

Two read port, one write port RAM

```
# DefineDualRAM :: 
#  RADDR0:In(Bits(height)), 
#  RDATA0:Out(Bits(width)),
#  RADDR1:In(Bits(height)), 
#  RDATA1:Out(Bits(width)),
#  WADDR:In(Bits(height)), 
#  WDATA:Out(Bits(width)),
#  WE,In(Bit),
#  CLK:In(Clock)
DualRAM = DefineDualRAM(height, width)

# DualRAM :: 
#  RADDR0:In(Bits(height)), 
#  RDATA0:Out(Bits(width)),
#  RADDR1:In(Bits(height)), 
#  RDATA1:Out(Bits(width)),
#  WADDR:In(Bits(height)), 
#  WDATA:Out(Bits(width)),
#  WE,In(Bit),
#  CLK:In(Clock)
ram = DualRAM(height, width)
```

### Memory

Implement a blocked or SRAM.
Currently all SRAMs are 4k bits.
Only certain heights and widths are currently supported:
(height, width) = (256, 16), (512,8), (1024, 4), (2048, 2)

```
# if readonly:
#   ROM :: 
#    "RDATA", Out(Bits(width)),
#    "RADDR", In(Bits(clog2(height))),
#    "RCLK",  In(Clock),
#    "RE",    In(Bit)
# else:
#   RAM :: 
#    "RDATA", Out(Bits(width)),
#    "RADDR", In(Bits(clog2(height))),
#    "RCLK",  In(Clock),
#    "RE",    In(Bit),
#    "WADDR", In(Bits(height)),
#    "WDATA", In(Bits(width))
#    "WCLK",  In(Clock),
#    "WE",    In(Bit),

mem = Memory( height, width, data=None, readonly=False )
```

