"""
Starter code for Advent of Code 2019 Day #1

You must implement functions part1 and part2
"""

import sys
import os


def find_total_fuel_reqs(numbers):
    """
    Solves Part 1 (see problem statement for more details)

    Parameter:
    - numbers (list of integers)

    Returns an integer
    """

    ### Replace with your code
    total = 0

    for n in numbers:
        n = (n // 3) - 2
        total += n
    
    return total

# find_total_fuel_reqs(numbers) --> 3331849

def find_added_fuel_reqs(numbers):
    """
    Solves Part 2 (see problem statement for more details)

    Parameter:
    - numbers (list of integers)

    Returns an integer
    """

    ### Replace with your code
    total = 0

    for n in numbers:
        n_total = 0
        
        while n > 0:
            n = find_total_fuel_reqs([n])
            if n > 0:
                n_total += n
        
        total += n_total

    return total

############################################
###                                      ###
###      Do not modify the code below    ###
###                EXCEPT                ###
###    to comment/uncomment the calls    ###
###        to the functions above        ###
###                                      ###
############################################

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"USAGE: python3 {os.path.basename(sys.argv[0])} <INPUT FILE>")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print(f"ERROR: No such file: {input_file}")
        sys.exit(1)

    with open(input_file) as f:
        numbers = [int(x) for x in f.read().split()]

    print(f"Part 1:", part1(numbers))

    # Uncomment the following line when you're ready to work on Part 2
    #print(f"Part 2:", part2(numbers))
