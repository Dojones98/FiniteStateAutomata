"""Description: This is a program that simulates a DFA from an input file that is a
   description of that DFA and A file that contains strings that may or may not be
   accepted by that DFA. It outputs whether or not the lines of the strings file
   are accepted or rejected by the DFA."""

import sys

# Input: a text string, a nested dictionary of transitions, the current state of the DFA
# Output: the final state that a DFA is in given a transition table and a string
# Description: This function uses recursion to read in every character of a string
# and parse that through a given DFA to find out the last state the DFA is in

def accept_or_reject_helper(string, transitions, current_state):
    """Return the final state of a DFA after it goes through all of its transitions."""
    char_to_use = string[0]
    fixed = str(string[1:])
    if char_to_use == '\n':
        return current_state
    next_state = transitions[current_state][char_to_use]
    return accept_or_reject_helper(fixed, transitions, next_state)

# Input: a DFA state, the set of accepting states of a given DFA
# Output: A boolean value True if the given state is an accepting state, false if otherwise

def does_it_accept(state, accepting_states):
    """Return true if state is in the list of accepting_states."""
    if state in accepting_states:
        return True
    return False

# Input: A list of characters in the alphabet of a language, a list of the transions
# Output: a nested dictionary of states and their transitions corresponding to the input
# character

def build_table(alphabet, trans):
    """Return a transition table given an alphabet and a list of transitions with
       that given alphabet."""
    outer_dict = {}
    for index_t, value_t in enumerate(trans):
        transiton_dict = {}
        for index_a, value_a in enumerate(alphabet):
            transiton_dict[value_a] = value_t.split()[index_a]
        outer_dict[str(index_t)] = transiton_dict
    return outer_dict

if __name__ == "__main__":
    DFA_FILE = sys.argv[1]
    STRINGS_FILE = sys.argv[2]

    with open(DFA_FILE, 'r') as dfa_handle:
        DFA_DATA = dfa_handle.readlines()
        NUMBER_OF_STATES = int(DFA_DATA[0].split(':')[1])
        ACCEPTING_STATES = set(DFA_DATA[1].split(':')[1].split())
        ALPHABET = list(DFA_DATA[2].split(':')[1])[1:-1]

    with open(STRINGS_FILE, 'r') as strings_handle:
        STRINGS_DATA = strings_handle.readlines()

    TRANSITIONS = DFA_DATA[3:]
    TRANSITION_TABLE = build_table(ALPHABET, TRANSITIONS)

    for x in STRINGS_DATA:
        final_state = accept_or_reject_helper(x, TRANSITION_TABLE, '0')
        if does_it_accept(final_state, ACCEPTING_STATES):
            print(f"ACCEPT {x[:-1]}")
        else:
            print(f"REJECT {x[:-1]}")
            