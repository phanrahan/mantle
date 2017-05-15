from magma.bits import *
from collections import defaultdict

def simulate_sb_carry(self, value_map, state_storage):
    I0 = value_map[self.interface.ports['I0']]
    I1 = value_map[self.interface.ports['I1']]
    CI = value_map[self.interface.ports['CI']]
    val = (I0 and I1) or (I1 and CI) or (I0 and CI)
    value_map[self.interface.ports['CO']] = val
    
def simulate_sb_lut4(self, value_map, state_storage):
    init = self.kwargs['LUT_INIT']
    lut = int2seq(init[0], init[1])
    lut = [bool(i) for i in lut]
    inputs = self.interface.inputs()
    I = [value_map[inputs[x]] for x in range(0, 4)]
    idx = seq2int(I)
    val = lut[idx]
    value_map[self.interface.ports['O']] = val

# SB_DFF*
# ce = Clock Enable
# r = Reset
# sy = Synchronous
# s = Set
# n = Negative Edge
def gen_sb_dff_sim(ce=False, sy=False, r=False, s=False, n=False):
    def sim(self, value_map, state_storage):
        cur_clock = value_map[self.interface.ports['C']]

        if not state_storage:
            state_storage['prev_clock'] = cur_clock
            state_storage['cur_val'] = False

        if r:
            cur_r = value_map[self.interface.ports['R']]
        if s:
            cur_s = value_map[self.interface.ports['S']]

        prev_clock = state_storage['prev_clock']
        if not n:
            clock_edge = cur_clock and not prev_clock
        else:
            clock_edge = not cur_clock and prev_clock

        new_val = state_storage['cur_val']

        if clock_edge:
            input_val = value_map[self.interface.ports['D']]

            enable = True
            if ce:
                enable = value_map[self.interface.ports['E']]

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

        state_storage['prev_clock'] = cur_clock
        state_storage['cur_val'] = new_val
        value_map[self.interface.ports['Q']] = new_val

    return sim

# RAM40_4K*
# prc = Positive Edge Read Clock, pwc = Positive Edge Write Clock
def gen_sb_ram40_4k_sim(prc=True, pwc=True):
    def sim(self, value_map, state_storage):
        r_clock = self.interface.ports['RCLK'].get_simulated_value(loc)
        w_clock = value_map[self.interface.ports['WCLK']]

        w_mode = int(self.kwargs['WRITE_MODE'])
        r_mode = int(self.kwargs['READ_MODE'])
        n_w_blocks = 16 // pow(2, w_mode) # number of blocks the RAM is split into for writing
        n_r_blocks = 16 // pow(2, r_mode) # number of blocks the RAM is split into for reading
        w_block_sz = 7 + w_mode        # how many bits are req to convert address (7 is for 8-bit),
        r_block_sz = 7 + r_mode        # (8 is for 9-bit), etc.

        # initialize RAM
        if not state_storage:
            # block
            state_storage['block'] = [False] * 4096
            for i in range(16):
                init_block = self.kwargs['INIT_' + str(format(i, 'X'))]
                for x in range(256):
                    assert ((init_block[0] >> x) & 1) == 1 or ((init_block[0] >> x) & 1) == 0
                    state_storage['block'][(i * 256) + x] = bool((init_block[0] >> x) & 1)
            
            state_storage['prev_r_clock'] = r_clock
            state_storage['prev_w_clock'] = w_clock
            state_storage['r_data'] = [False] * n_r_blocks

        block = state_storage['block']

        # obtain clock information
        prev_w_clock = state_storage['prev_w_clock']
        if pwc:
            w_clock_edge = w_clock and not prev_w_clock
        else:
            w_clock_edge = not w_clock and prev_w_clock

        prev_r_clock = state_storage['prev_r_clock']
        if prc:
            r_clock_edge = r_clock and not prev_r_clock
        else:
            r_clock_edge = not r_clock and prev_r_clock

        # write to RAM
        if w_clock_edge:
            w_data = [value_map[bit] for bit in self.interface.ports['WDATA']]
            mask = [value_map[bit] for bit in self.interface.ports['MASK']]
            w_addr = [value_map[bit] for bit in self.interface.ports['WADDR']]
            w_e = value_map[self.interface.ports['WE']]
            w_clke = value_map[self.interface.ports['WCLKE']]
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
            r_addr = [value_map[bit] for bit in self.interface.ports['RADDR']]

        r_e = value_map[self.interface.ports['RE']]
        r_clke = value_map[self.interface.ports['RCLKE']]
        r_data = state_storage['rdata']

        if r_e and r_clock_edge and r_clke:
            idx = n_r_blocks * seq2int(r_addr)
            for i in range(n_r_blocks):
                r_data[i] = block[idx + i];

        for i in range(n_r_blocks):
            assert isinstance(r_data[i], bool)
            value_map[self.interface.ports['RDATA'][i]] = r_data[i];

        state_storage['prev_w_clock'] = w_clock
        state_storage['prev_r_clock'] = r_clock

    return sim
