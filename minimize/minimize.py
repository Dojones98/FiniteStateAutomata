"""Description: This is a program that minimizes a DFA from an input file that is a
   description of that DFA and outputs the distinguishibility table, the indistinguishable
   pairs, the sets of states with common transitions, and the description of the minimized DFA."""

import sys

# Input: a character, a nested dictionary of transitions, the current state of the DFA
# Output: the next state of the DFA

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
    """this function breaks up code to keep the nondistunguishable_table
    function from being too long."""
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
    """Create the distinguishibility table based on the Table of Distinguishibilities
        algorithm for DFA minimization located on page 128 of the course-notes.pdf"""
    rows, cols = (num_states, num_states)
    arr = [['_' for i in range(cols)] for j in range(rows)]
    for index_x, row in enumerate(arr):
        for index_y, _ in enumerate(row):
            if((((str(index_x) in accepting_states) and
                 (str(index_y) not in accepting_states)) or
                    ((str(index_x) not in accepting_states) and
                     (str(index_y) in accepting_states))) or
               (index_x < index_y)):
                arr[index_x][index_y] = 'X'
    doing_work = True
    array_temp = arr
    while doing_work:
        arr = nondistinguishable_helper(arr, trans_table, alphabet)
        if arr == array_temp:
            doing_work = False
        array_temp = arr
    return arr

def print_nondist_table(table):
    '''Print the distinguishability table'''
    print("\nHere is the table of non-distinguishables:")
    for row in table:
        for column in row:
            print(column, end=' ')
        print()

def nondistinguishable_pairs(nondist_table):
    """Take the distinguishibility table and generate a list of non-
        distinguishable pairs. From this list, combine non-distinguishable
        pairs into sets of states that share common transitions."""
    nondist_pairs = list()
    for index_x, row in enumerate(nondist_table):
        for index_y, _ in enumerate(row):
            if nondist_table[index_x][index_y] == '_':
                if index_x != index_y:
                    add_it = list()
                    add_it.append(str(index_x))
                    add_it.append(str(index_y))
                    nondist_pairs.append(add_it)
    print("\nHere are the nondistinct pairs: ")
    print(nondist_pairs)

    common_states = []
    while len(nondist_pairs) > 0:
        first, *rest = nondist_pairs
        first = set(first)
        nondist_pairsf = -1
        while len(first) > nondist_pairsf:
            nondist_pairsf = len(first)
            rest2 = []
            for elem in rest:
                if len(first.intersection(set(elem))) > 0:
                    first |= set(elem)
                else:
                    rest2.append(elem)
            rest = rest2
        common_states.append(first)
        nondist_pairs = rest
    print("\nHere are the sets of equivalent states:")
    print(common_states)

    return common_states

def minimize(nondist_pairs, transitions, alphabet, accepting_states):
    """given the nondistinguishable pairs, the transition table, alphabet,
        and accepting states, generate a valid minimized DFA."""
    for pair1 in nondist_pairs:
        for elem in pair1:
            transitions.update({tuple(pair1) : transitions[str(elem)]})
    for pair in nondist_pairs:
        for elem in pair:
            if str(elem) in transitions:
                del transitions[str(elem)]
    new_list = list(transitions.items())
    for elem in new_list:
        for char in alphabet:
            for pair in nondist_pairs:
                if elem[1][char] in pair:
                    elem[1][char] = pair

    print("\nHere is the DFA Description:")
    print(f"Number of states: {len(new_list)}")
    print(f"Accepting states: {accepting_states}")

    for elem in new_list:
        print(f"State: {elem[0]}        Transitions: {elem[1]}")

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
    print_nondist_table(TABLE)
    PAIRS = nondistinguishable_pairs(TABLE)
    minimize(PAIRS, TRANSITION_TABLE, ALPHABET, ACCEPTING_STATES)
