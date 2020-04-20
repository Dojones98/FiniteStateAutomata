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

def accept_or_reject_on_char(char, transitions, current_state):
    """helper"""
    return transitions[current_state][char]

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

def nondistinguishable_helper(arr, trans_table, alphabet):
    """Output the minimized DFA"""
    for index_x, row in enumerate(arr):
        for index_y, _ in enumerate(row):
            if arr[index_x][index_y] != 'X':
                for char in alphabet:
                    state1 = int(accept_or_reject_on_char(char, trans_table, str(index_x)))
                    state2 = int(accept_or_reject_on_char(char, trans_table, str(index_y)))
                    if arr[state1][state2] == 'X':
                        arr[index_x][index_y] = 'X'
                        arr[index_y][index_x] = 'X'
    return arr

def nondistinguishable_table(trans_table, num_states, accepting_states, alphabet):
    """Output the minimized DFA"""
    rows, cols = (num_states, num_states)
    arr = [['_' for i in range(cols)] for j in range(rows)]
    for index_x, row in enumerate(arr):
        for index_y, _ in enumerate(row):
            if((((str(index_x) in accepting_states) and
                 (str(index_y) not in accepting_states)) or
                    ((str(index_x) not in accepting_states) and
                     (str(index_y) in accepting_states))) or
               (index_x > index_y)):
                arr[index_x][index_y] = 'X'
    doing_work = True
    array_temp = arr
    while doing_work:
        arr = nondistinguishable_helper(arr, trans_table, alphabet)
        if arr == array_temp:
            doing_work = False
        array_temp = arr
    return arr

def nondistinguishable_pairs(nondist_table):
    """fuck you pylint"""
    nondist_pairs = list()
    for index_x, row in enumerate(nondist_table):
        for index_y, _ in enumerate(row):
            if nondist_table[index_x][index_y] == '_':
                if index_x != index_y:
                    add_it = (index_x, index_y)
                    nondist_pairs.append(add_it)
    return nondist_pairs

def minimize(nondist_pairs, transitions, alphabet, accepting_states):
    for pair in nondist_pairs:
        for elem in pair:
            transitions.update({pair : transitions[str(elem)]}) 
    print(transitions)        

        
        




if __name__ == "__main__":
    DFA_FILE = sys.argv[1]

    with open(DFA_FILE, 'r') as dfa_handle:
        DFA_DATA = dfa_handle.readlines()
        NUMBER_OF_STATES = int(DFA_DATA[0].split(':')[1])
        ACCEPTING_STATES = set(DFA_DATA[1].split(':')[1].split())
        ALPHABET = list(DFA_DATA[2].split(':')[1])[1:-1]

    TRANSITIONS = DFA_DATA[3:]
    TRANSITION_TABLE = build_table(ALPHABET, TRANSITIONS)

    TABLE = nondistinguishable_table(TRANSITION_TABLE, NUMBER_OF_STATES, ACCEPTING_STATES, ALPHABET)
    PAIRS = nondistinguishable_pairs(TABLE)
    minimize(PAIRS, TRANSITION_TABLE, ALPHABET, ACCEPTING_STATES)

