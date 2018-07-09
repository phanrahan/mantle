from magma import *
from mantle import LUT4, I0, I1, I2, I3, FF, Mux2
import greenery

__all__ = ['DefineFSM']


def State(state, ins, outs, ffs, events):

        # logic entering state
        #  if in a state with an event edge to this state
        ilut = LUT4((I0&I1)|(I2&I3))

        num_entrance_events = len(ins)
        if num_entrance_events < 1:
            wire(0, ilut.I0)
            wire(0, ilut.I1)
        else:
            previous_state_index = ins[0][0]
            trigger_event_index = ins[0][1]
            wire(ffs.O[previous_state_index], ilut.I0)
            wire(events[trigger_event_index], ilut.I1)

        if num_entrance_events < 2:
            wire(0, ilut.I2)
            wire(0, ilut.I3)
        else:
            previous_state_index = ins[1][0]
            trigger_event_index = ins[1][1]
            wire(ffs.O[previous_state_index], ilut.I2)
            wire(events[trigger_event_index], ilut.I3)

        if num_entrance_events > 2:
            print('#Warning:', num_entrance_events, 'inputs (only 2 allowed)')


        # logic for exiting state
        #  if an outgoing event edge from this state
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

        mux = Mux2()
        mux( bits([ilut.O, olut.O]), ffs.O[state] )
        wire(mux.O, ffs.I[state])


def DefineFSM(name, fsm):
    assert isinstance(fsm, greenery.fsm.fsm)

    states = list(fsm.states)
    events = list(fsm.alphabet)
    initial = fsm.initial
    transitions = fsm.map
    nstates = len(states)
    nevents = len(events)

    FSM =  DefineCircuit(name, 
              'events', In(Bits(nevents)),
              'states', Out(Bits(nstates)),
              *ClockInterface(has_ce=True))

    # create a [event] of outgoing transitions for each state
    outs = nstates * [0]

    # create a [(prev_state, event)] of incoming transitions for each state
    ins = nstates * [0]

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


    def ff(y):
        init = 1 if states.index(initial) == y else 0
        return FF(init=init, has_ce=True)
    ffs = join(col(ff, nstates))

    wire(FSM.CE, ffs.CE)
    wire(ffs.O, FSM.states)

    for i in range(nstates):
        #print('ins',ins[i])
        #print('outs',outs[i])
        State(i, ins[i], outs[i], ffs, FSM.events)

    EndCircuit()

    return FSM

