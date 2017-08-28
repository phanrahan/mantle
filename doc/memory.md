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

The ```ROM``` functions are very similar to the ```LUT``` functions.
The only difference is the the types of the inputs.
The ```LUT``` versions take n input arguments of type Bit.
The ```ROM``` versions of these functions take
a single input, an ```Bits(n)```.

```
rom = ROM1(init) :: I:Bits(1) -> O:Bit
rom = ROM2(init) :: I:Bits(2) -> O:Bit
rom = ROM3(init) :: I:Bits(3) -> O:Bit
rom = ROM4(init) :: I:Bits(4) -> O:Bit
rom = ROM5(init) :: I:Bits(5) -> O:Bit
rom = ROM6(init) :: I:Bits(6) -> O:Bit
rom = ROM7(init) :: I:Bits(7) -> O:Bit
rom = ROM8(init) :: I:Bits(8) -> O:Bit
rom = ROMN(init, n=None) :: I:Bits(n)  ->  O:Bit
```

```
# DefineROM :: I:Bits(n)  ->  O:Bit
ROM = DefineROM(init, height, width)

# ROM :: I:Bits(n)  ->  O:Bit
rom = ROM(init, height, width) :: I:Bits(n)  ->  O:Bit
```

### RAM

RAM circuits are NYI.

```
# DefineRAM :: I:Bits(n)  ->  O:Bit
RAM = DefineRAM(init, height, width)
```

```
# RAM :: I:Bits(n)  ->  O:Bit
rom = RAM(init, height, width) :: I:Bits(n)  ->  O:Bit
```

### Memory

```
# if readonly:
#   ROM :: 
#    "RDATA", Out(Bits(height)),
#    "RADDR", In(Bits(width)),
#    "RCLK",  In(Clock),
#    "RE",    In(Bit)
# else:
#   RAM :: 
#    "RDATA", Out(Bits(16)),
#    "RADDR", In(Bits(11)),
#    "RCLK",  In(Clock),
#    "RE",    In(Bit),
#    "WADDR", In(Bits(11)),
#    "WDATA", In(Bits(16))
#    "WCLK",  In(Clock),
#    "WE",    In(Bit),

rom = Mem( rom, height, width, readonly=False )
```
