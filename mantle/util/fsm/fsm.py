from magma import *
from mantle import *
from mantle.xilinx.spartan import MUXF5
import greenery

__all__ = ['FSM']


def State(state, ins, outs, states, events):

        # entering state
        ilut = LUT4((I0&I1)|(I2&I3))

        num_entrance_events = len(ins)
        if num_entrance_events < 1:
            wire(0, ilut.I0)
            wire(0, ilut.I1)
        else:
            previous_state_index = ins[0][0]
            trigger_event_index = ins[0][1]
            wire(states.O[previous_state_index], ilut.I0)
            wire(events[trigger_event_index], ilut.I1)

        if num_entrance_events < 2:
            wire(0, ilut.I2)
            wire(0, ilut.I3)
        else:
            previous_state_index = ins[1][0]
            trigger_event_index = ins[1][1]
            wire(states.O[previous_state_index], ilut.I2)
            wire(events[trigger_event_index], ilut.I3)

        if num_entrance_events > 2:
            print('#Warning:', num_entrance_events, 'inputs (only 2 allowed)')


        olut = LUT4(~(I0|I1|I2|I3))

        num_exit_states = len(outs)
        if num_exit_states < 1:
            wire(0, olut.I0)
        else:
            next_state_index = outs[0]
            wire(events[next_state_index],olut.I0)

        if num_exit_states < 2:
            wire(0, olut.I1)
        else:
            next_state_index = outs[1]
            wire(events[next_state_index],olut.I1)

        if num_exit_states < 3:
            wire(0, olut.I2)
        else:
            next_state_index = outs[2]
            wire(events[next_state_index],olut.I2)

        if num_exit_states < 4:
            wire(0, olut.I3)
        else:
            next_state_index = outs[3]
            wire(events[next_state_index],olut.I3)

        if num_exit_states > 4:
            print('#Warning:', n, 'outputs (only 4 allowed)')

        mux = MUXF5()
        mux( ilut, olut, states.O[state] )
        wire(mux.O, states.I[state])


def FSM(fsm):
    assert isinstance(fsm, greenery.fsm.fsm)

    states = fsm.states
    events = fsm.alphabet
    initial = fsm.initial
    transitions = fsm.map

    nstates = len(states)

    # outs is an array with index=state 
    # and values=[events that exit this state]
    outs = range(nstates)

    # ins is an array with index=state and values=[(prev_state, event)]
    # that represent previous states and associated events
    # that cause a transititon to this state
    ins = range(nstates)

    for state, state_transitions in transitions.items():
        state_index = states.index(state)
        outs[state_index] = list()
        for event, next_state in state_transitions.items():
            event_index = events.index(event)
            next_state_index = states.index(next_state)

            # skip over transitions that stay in the same state
            if next_state_index == state_index:
                continue

            outs[state_index].append(event_index)

            if isinstance(ins[next_state_index], list):
                ins[next_state_index].append((state_index, event_index))
            else:
                ins[next_state_index] = [(state_index, event_index)]

    CE = Bit()
    EV = Array(len(events), Bit)()

    def ff(y):
        init = 1 if states.index(initial) == y else 0
        return FF(init=init, ce=True)
    ffs = join(col(ff, nstates))
    wire(CE, ffs.CE)

    for i in range(nstates):
        State(i, ins[i], outs[i], ffs, EV)

    return AnonymousCircuit('input events', EV, 'output states', ffs.O, 'input CE', CE)
