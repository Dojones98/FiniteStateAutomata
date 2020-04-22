"""Description: This is a program that simulates a DFA from an input file that is a
   string. The generated DFA description accepts any word w where x (the string in the input file)
   is a substring of w."""

import sys

# Input: A list of characters in the alphabet of a language, a list of the transions
# Output: a nested dictionary of states and their transitions corresponding to the input
# character

def build_table(alphabet, word):
    """Return a transition table given an alphabet and a list of transitions with
       that given alphabet."""
    outer_dict = list()
    for index_t, value_t in enumerate(word):
        transiton_dict = list()
        for value_a in alphabet:
            if value_a == value_t:
                transiton_dict.append(index_t + 1)
            else:
                transiton_dict.append(0)
        outer_dict.append(transiton_dict)
    outer_dict.append([len(word)]*len(alphabet))
    return outer_dict

def print_dfa(alphabet, number_states, accepting_state, transition_table):
    '''Print the Valid DFA description given all of the elements that make up
        a DFA description.'''
    print(f"Number of states: {number_states}")
    print(f"Accpeting states: {accepting_state}")
    print(f"Alphabet: {alphabet}")
    for row in transition_table:
        for column in row:
            print(column, end=' ')
        print()

if __name__ == "__main__":
    TEXT_FILE = sys.argv[1]
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET_LENGTH = 26

    with open(TEXT_FILE, 'r') as text_handle:
        WORD_DATA = text_handle.readlines()
        WORD = WORD_DATA[0]
    NUM_STATES = len(WORD) + 1
    ACCEPTING_STATE = len(WORD)
    TABLE = build_table(ALPHABET, WORD)
    print_dfa(ALPHABET, NUM_STATES, ACCEPTING_STATE, TABLE)
