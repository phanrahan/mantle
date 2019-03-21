import six
from magma.bitutils import *
from collections import defaultdict

def simulate_sb_carry(self, value_store, state_store):
    I0 = value_store.get_value(self.I0)
    I1 = value_store.get_value(self.I1)
    CI = value_store.get_value(self.CI)
    val = (I0 and I1) or (I1 and CI) or (I0 and CI)
    value_store.set_value(self.CO, val)

def simulate_sb_lut4(self, value_store, state_store):
    init = self.kwargs['LUT_INIT']
    if isinstance(init, six.string_types):
        a = init.split("'")
        l = int(a[0])
        p = a[1][0]
        if p == 'h':
            base = 16
        else:
            base = 10

        i = int(a[1][1:], base)
        init = lutinit(i, l)

    if isinstance(init, int):
        init = (init, 16)
    lut = int2seq(init[0], init[1])
    lut = [bool(i) for i in lut]
    inputs = self.interface.inputs()
    I = [value_store.get_value(inputs[x]) for x in range(0, 4)]
    idx = seq2int(I)
    val = lut[idx]
    value_store.set_value(self.O, val)

# SB_DFF*
# ce = Clock Enable
# r = Reset
# sy = Synchronous
# s = Set
# n = Negative Edge
def gen_sb_dff_sim(ce=False, sy=False, r=False, s=False, n=False):
    def sim(self, value_store, state_store):
        cur_clock = value_store.get_value(self.C)

        if not state_store:
            state_store['prev_clock'] = cur_clock
            state_store['cur_val'] = False

        if r:
            cur_r = value_store.get_value(self.R)
        if s:
            cur_s = value_store.get_value(self.S)

        prev_clock = state_store['prev_clock']
        if not n:
            clock_edge = cur_clock and not prev_clock
        else:
            clock_edge = not cur_clock and prev_clock

        new_val = state_store['cur_val']

        if clock_edge:
            input_val = value_store.get_value(self.D)

            enable = True
            if ce:
                enable = value_store.get_value(self.E)

            if enable:
                if r and sy and cur_r:
                    new_val = False
                elif s and sy and cur_s:
                    new_val = True
                else:
                    new_val = input_val

        if r and not sy and cur_r:
            new_val = False
        if s and not sy and cur_s:
            new_val = True

        state_store['prev_clock'] = cur_clock
        state_store['cur_val'] = new_val
        value_store.set_value(self.Q, new_val)

    return sim

# RAM40_4K*
# prc = Positive Edge Read Clock, pwc = Positive Edge Write Clock
def gen_sb_ram40_4k_sim(prc=True, pwc=True):
    def sim(self, value_store, state_store):
        r_clock = value_store.get_value(self.RCLK)
        w_clock = value_store.get_value(self.WCLK)

        w_mode = int(self.kwargs['WRITE_MODE'])
        r_mode = int(self.kwargs['READ_MODE'])
        n_w_blocks = 16 // pow(2, w_mode) # number of blocks the RAM is split into for writing
        n_r_blocks = 16 // pow(2, r_mode) # number of blocks the RAM is split into for reading
        w_block_sz = 7 + w_mode        # how many bits are req to convert address (7 is for 8-bit),
        r_block_sz = 7 + r_mode        # (8 is for 9-bit), etc.

        # initialize RAM
        if not state_store:
            # block
            state_store['block'] = [False] * 4096
            # The SB_RAM primitive has a special initialization mapping for bits,
            # see the init function in mantle/lattice/ice40/RAMB.py
            # Here we invert the mapping and store the memory in a cartesian
            # grid
            N = n_r_blocks
            M = 16 // N
            for i in range(16):
                v = self.kwargs['INIT_' + str(format(i, 'X'))][0]
                for b in range(256):
                    col = (b//M)%N
                    row = 256*(b%M) + 16*i + b//16
                    state_store['block'][row * N + col] = bool((v >> b) & 1)

            state_store['prev_r_clock'] = r_clock
            state_store['prev_w_clock'] = w_clock

        block = state_store['block']

        # obtain clock information
        prev_w_clock = state_store['prev_w_clock']
        if pwc:
            w_clock_edge = w_clock and not prev_w_clock
        else:
            w_clock_edge = not w_clock and prev_w_clock

        prev_r_clock = state_store['prev_r_clock']
        if prc:
            r_clock_edge = r_clock and not prev_r_clock
        else:
            r_clock_edge = not r_clock and prev_r_clock

        # write to RAM
        if w_clock_edge:
            WDATA = value_store.get_value(self.WDATA)
            w_data = [False for _ in range(n_w_blocks)]
            for i in range(n_r_blocks):
                if n_r_blocks == 16:
                    w_data[i] = WDATA[i]
                elif n_r_blocks == 8:
                    w_data[i] = WDATA[i * 2]
                elif n_r_blocks == 4:
                    w_data[i] = WDATA[1 + i * 4]
                elif n_r_blocks == 2:
                    w_data[i] = WDATA[3 + i * 8]
            mask = value_store.get_value(self.MASK)
            w_addr = value_store.get_value(self.WADDR)
            w_e = value_store.get_value(self.WE)
            w_clke = value_store.get_value(self.WCLKE)
            if w_mode == 0: # use MASK
                if w_e and w_clke:
                    idx = n_w_blocks * seq2int(w_addr)
                    for i in range(n_w_blocks):
                        if mask[i] == False:
                            assert w_data[i] == True or w_data[i] == False
                            block[idx + i] = w_data[i]
            else:
                if w_e and w_clke:
                    idx = n_w_blocks * seq2int(w_addr)
                    for i in range(n_w_blocks):
                        assert w_data[i] == True or w_data[i] == False
                        block[idx + i] = w_data[i]

        # read from RAM
        if r_clock_edge:
            r_addr = value_store.get_value(self.RADDR)

        r_e = value_store.get_value(self.RE)
        r_clke = value_store.get_value(self.RCLKE)

        RDATA = [False for _ in range(16)]
        if r_e and r_clock_edge and r_clke:
            r_data = [False] * n_r_blocks
            row = n_r_blocks * seq2int(r_addr)
            for col in range(n_r_blocks):
                r_data[col] = block[row + col];

            for i in range(n_r_blocks):
                if n_r_blocks == 16:
                    RDATA[i] = bool(r_data[i])
                elif n_r_blocks == 8:
                    RDATA[i * 2] = bool(r_data[i])
                elif n_r_blocks == 4:
                    RDATA[1 + i * 4] = bool(r_data[i])
                elif n_r_blocks == 2:
                    RDATA[3 + i * 8] = bool(r_data[i])

            value_store.set_value(self.RDATA, RDATA)

        state_store['prev_w_clock'] = w_clock
        state_store['prev_r_clock'] = r_clock

    return sim
