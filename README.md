# CSCE 355 Final Project Spring 2020
Daniel Jones


The three subfolders in this directory contain the completed code for the CSCE 355 Final Project.

I completed 3 of the 2 mandatory options for this. They are detailed below:

# Folder 1: simulate
  This folder contains the python3 source file, a sample input DFA, and a sample input strings file.
### Note: ALL program outputs are to standard output
## Simulate Contents:

    1. simulate.py
    2. simulate.txt
    3. strings.txt
    4. dfa.txt
    5. run_simulate.sh
    6. no_args_runsimulate.sh

    ### HOW TO RUN ###

    Valid ways to run:
       1. python3 simulate.py dfa.txt strings.txt
       2. ./run_simulate.sh dfa.txt strings.txt
       3. ./no_args_run_minimize.sh

    To run this code, you need to use python3 with two command line arguments (an input DFA,and a .txt file containing strings to run through the simulated DFA)

    In addition to this option, you could run the no_args shell script which will execute simulate.py using python3 with dfa.txt and strings.txt as input files.

    You could also use run_simulate.sh which will require two additional command line agruments. (i.e. ./run_simulate dfa.txt strings.txt)


# Folder 2: textsearch  
    This folder contains the python3 source file and a sample .txt file containing the string "hello" to be used as example program execution.

## Textsearch Contents:
    1. textsearch.py
    2. text_input.txt
    3. searcher.txt
    4. run_textsearch.sh
    5. no_args_run_textsearch.sh

    ### HOW TO RUN ###
    
     Valid ways to run:
       1. python3 textsearch.py text_input.txt
       2. ./run_textsearch.sh text_input.txt
       3. ./no_args_run_textsearch.sh

    To run this code, you need to use python3 with one command line argument(a .txt file containing exactly one string)

    In addition to this option you could run the no_args shell script which will execute textsearch.py using python3 with text_input.txt as an input file.

    You could also use run_textsearch.sh with one additional command line argument (i.e. ./run_textsearch text_input.txt)

# Folder 3: minimize
    1. minimize.py
    2. minimize.txt
    3. dfa.txt
    4. run_minimize.sh
    5. no_args_run_minimize.sh

    ### HOW TO RUN ###

    Valid ways to run:
       1. python3 minimize.py dfa.txt
       2. ./run_minimize.sh dfa.txt
       3. ./no_args_run_minimize.sh
        

    To run this code, you need to use python3 with one command line argument(a .txt file that is a valid description of a DFA.)

    In addition to this option you could run the no_args shell script which will execute minimize.py using python3 with dfa.txt as an input file.

    You could also use run_minimize.sh with one additional command line argument (i.e. ./run_textsearch dfa.txt)



    


