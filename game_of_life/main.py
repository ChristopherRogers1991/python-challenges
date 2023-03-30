"""
COPYRIGHT: Christopher Rogers

This file, as a _template_, may be edited and shared, according to the terms
 of the GNU General Public license, the terms of which are here:
 https://www.gnu.org/licenses/gpl-3.0.en.html. _Do not_ post a solution
 (in whole or in part) publicly online.

Additionally, this copyright notice and the license terms must be included in any
re-distribution.


##############
# BEGIN HERE #
##############

If you are new to programming and/or Python, it is recommended that you start with
the lights_out project. This project will assume you've worked through at least
lights_out, and will start to point you to official Python documentation for examples
and explanations. The expectation is that you will begin to familiarize yourself
with the official docs, and become comfortable reading them to learn about new
functions and classes. For now, it is recommended that you stick to just the information
here and in the official docs, as opposed to searching for other documentation online.
Your focus should be on "learning concepts" as opposed to "finding solutions," hence
the emphasis on only using the docs here and the official Python docs. Other sources
may provide "solutions," but without a full understanding of how they work, can
defeat the purpose of completing this exercise.

This project will walk you through creating Conway's Game of Life (see
https://en.wikipedia.org/wiki/Conway's_Game_of_Life). The basic premise is,
given a grid of cells, where each cell is either 'alive' or 'dead', over time
cells die/become alive based on the conditions around them. Specifically:

* Living cells with fewer than two live neighbors die (underpopulation)
* Living cells with 2-3 live neighbors live to the next generation
* Living cells with 4 or more living neighbors die (overpopulation)
* Dead cells with exactly 3 living neighbors become alive (reproduction)

Check out the introduction and 'Rules' section of the wikipedia page to see
more.

Our implementation will be text based. You will need to run the completed
application in your terminal. Note that the python console built into PyCharm
will not work.
"""

# Do not change these imports. You will not need to import
# any other libraries, classes, or functions.
from random import random
from time import sleep
from argparse import ArgumentParser
from sys import argv

# STEP -2:
#
# In our implementation, we will be using a list of lists to represent a 'board',
# containing cells. Cells with either contain '_' or 'X', where '_' represents a
# dead cell, and 'X' represents a live cell. The constants below are defined for you.

DEAD = '_'
LIVE = 'X'

# STEP -1
#
# In order to achieve the right effect, of cells changing from 'X' t0 '_' or vis versa,
# we will need to print over the top of the previously printed board.
LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'


# STEP 1
#
# clear_lines
#
# See the explanation for the function of the same name in the curdle project.
# This will need to behave the same way.
def clear_lines(num_lines):
    pass


# STEP 2
#
# fifty_fifty
#
# See the explanation of the fifty_fifty in the lights_out project. This will
# need to work exactly the same way.
def fifty_fifty():
    pass


# STEP 3:
#
# Given a height and width, generate a new random board. The board should
# be a list of lists, where the inner lists contain DEAD or LIVE. Use your
# fifty_fifty() function to determine if a particular cell is alive or dead.
#
# Note, this should work very similarly to the Board.__init__ from the
# lights_out project.
#
# The board should be random, but it should look something like:
#
#     [['_','_','X','_'].
#      ['_','X','_','_'].
#      ['_','X','X','X']]
def generate_random_board(height, width):
    pass


# STEP 4:
#
# generate_board_from_file
#
# For this function, you will need to read from a file, and create a new
# board (list of lists), based on the contents of the file. You can expect
# the file to contain only '_', 'X', and newline characters. See the examples
# in the 'boards' directory.
#
# If the file contains:
#
#     __X_
#     _X__
#     _XXX
#
# this method should return:
#
#     [['_','_','X','_'].
#      ['_','X','_','_'].
#      ['_','X','X','X']]
#
# To read from a file, you can use Python's built-in `open` method. It is
# recommended that you use the `with` keyword as well, e.g.:
#
#     with open(path) as board_file:
#         # do something with board_file here
#
# Once you have the file object created, you may find the following
# methods useful, you can use the `read` method, to get the contents
# of the file as a string, e.g.
#
#    file_contents = board_file.read()
#
# When you have the contents of the file as a string, you can use
# `split` or `splitlines` to get a list of strings, where each string
# represents one line of the file.
# See:
#     split: https://docs.python.org/3/library/stdtypes.html#str.split
#     splitlines: https://docs.python.org/3/library/stdtypes.html#str.splitlines
#
# WIth the list of strings, one per line, then you just need to convert each
# string to a list of its own. Consider the `list` constructor (see
# https://docs.python.org/3/library/stdtypes.html#typesseq-list). Otherwise,
# you can create an empty list, and use a for loop to copy the characters into
# the list.
#
# Note: If you have an easy time doing this with loops, and would like to
# challenge yourself, consider using a list-comprehension. See:
# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
def generate_board_from_file(path):
    pass


# STEP 5:
#
# board_to_string
#
# Given a board (list of lists), create and return a string by concatenating
# the contents, separated by newlines.
#
# For example, given:
#
#     [['_','_','X','_'].
#      ['_','X','_','_'].
#      ['_','X','X','X']]
#
# This should return:
#
#    "__X_\n_X__\n_XXX"
def board_to_string(board):
    pass


# STEP 6:
#
# print_board
#
# Given, a board, e.g.:
#
#     [['_','_','X','_'].
#      ['_','X','_','_'].
#      ['_','X','X','X']]
#
# Print the board, e.g.
#
#     __X_
#     _X__
#     _XXX
def print_board(board):
    pass


# STEP 7:
#
# Given a board, and a row and column, return True if the
# corresponding cell is alive (if it == LIVE). Otherwise,
# return False.
def cell_is_alive(board, row, column):
    pass


# STEP 8:
#
# Given a board, and a row and column, return the number of
# living neighbors, of the corresponding cell. E.g. given
#
#     [['_','_','X','_'].
#      ['_','X','_','_'].
#      ['_','X','X','X']]
#
# and row=0, column=1, this should return 2 (the cell at (0,1)
# has 2 living neighbors).
#
# Given the same board, with row=1, column=2, this should return 5.
#
# Note that in general, you will need to check all 8 neighbors, however
# you will need to be careful at the edges of the board - e.g. if you
# try to check the right neighbor of any cell in the far right column,
# you will be over the end of your list. Similarly, in the first column,
# first row, and last row, you will need to be careful not to walk off
# the ends of your lists.
def num_living_neighbors(board, row, column):
    pass


# STEP 9:
#
# update_board
#
# Given a board, return a new board representing the next generation. To do
# this, you will need to iterate through all cells on the board, and get a
# count of their living neighboars (use the function you defined in the
# previous step). In your new board, cells will need to be set to LIVE or
# DEAD based on the rules defined at the beginning of this file (see the
# linked wikipedia page, if you have questions about how it should work).
#
# Note that you will need to create a new board, and set the values for the
# next generation in that new board. If you try to update the board in place,
# you will be changing neighbor counts as you move through the board.
def update_board(board):
    pass


# STEP 10:
#
# main
#
# This function will create a board, and repeatedly (in a loop) update
# the board, printing the result after each update.
#
# It takes two optional arguments. If you are not familiar with default function
# arguments, see https://docs.python.org/3/tutorial/controlflow.html#default-argument-values.
#
# The `board_file` argument, if provided, should be a string, representing a path to a
# file defining a board, e.g. 'boards/single-glider.txt'. If a file is not
# given, main should generate a new random board.
#
# The `generations` argument, if provided, should be an int, indicating the number of
# generations for which the game should run. E.g. if generations is 10,
# the board should be updated and printed 10 times.
#
# After printing the board, the program should temporarily sleep, to
# display the board for a time, before updating and reprinting. It is
# recommended that you sleep for .15s, e.g. `sleep(.15)`.
#
# Between each printing of the board, the previously printed board should
# be cleared, so the next is printed in the same place (use your clear_lines
# function).
def main(board_file=None, generations=100):
    pass


# STEP 11:
#
# ArgumentParser
#
# This program will take two command line arguments, allowing the user to
# change the behavior of the program at runtime. For example, the user could
# run the following to run a random board for 50 generations:
#
#     python main.py --generations 50
#
# Or the following, to run a specific board, for 200 generations:
#
#     python main.py --board-file boards/single-glider.txt --generations 200
#
# To do this, you will need to use an ArgumentParser. Here is a quick example of
# how to make and use one - try running this in your python console:
#
#     1.  from argparse import ArgumentParser
#     2.  ap = ArgumentParser(description="My Arg Parser")
#     3.  ap.add_argument("-m", "--my-argument", help="A simple string argument")
#     4.  ap.add_argument("-i", "--my-int-argument", type=int, default=10, help="An argument of type int")
#     5.  result = ap.parse_args(["-m", "a string argument", "-i", "150"])
#     6.  print(result)
#     7.  result = ap.parse_args(["--my-argument", "A string arg using the long argument name"])
#     8.  print(result)
#     9.  print(result.my_int_argument)
#     10. ap.print_help()
#
# Note that in your console you will need to run the `from... import...` line, but that is
# already present in this file, so you will not need to import it here.
#
# Going through the rest of it, line by line:
#
# Line (1) creates a new ArgumentParser object, and assigns it to the `ap` variable.
# You can of course substitute in any variable name you like. The description is optional,
# but it is a good idea to include a description. It will be printed as part of the 'help'
# message (see the last line).
#
# Line (2) adds an argument to your parser. The first two arguments to the function
# call are "flags" - these define how you can pass the arguments on the command line. It
# is common (but not required) to have both a short (single character) and a long flag. At
# the command line, either the short or the long can be used (more on this later). The `help`
# argument passed to this function is optional, but again, it is a good idea to include. It
# can be anything you want, but should be some text that, when shown to the user, will help
# them understand what this argument is for. It will be printed as part of the help message
# for the program.
#
# Line (3) adds an additional argument to the parser. The twist here are the `type` and
# `default` arguments. Both of these are optional - when not specified, the `type` is str. The
# first argument we added was a str type, so there was no need to specify it in the method call.
# This argument takes an int, so it needs to be specified here. The `default` argument sets the
# default value, in the event the user does not supply one. The `default` is not given, then
# value will be `None`, if the user does not supply anything on the command line.
#
# Line (4) parses a list of arguments, and returns the results as a
# `Namespace` object, which is assigned to the `result` variable. Note that the short argument
# names are used in the list (`-m` and `-i`).
#
# Line (6) prints our Namespace (`result`), and shows what we've parsed.
#
# Line (7) parses another list of arguments. Note that this list does
# not contain the int argument. The resulting Namespace will therefore use the default
# value specified in the `add_argument(...)` call. Note also that the list of arguments
# here uses the long name.
#
# Line (8) prints our new Namespace. Note that although we only supplied one argument,
# the namespace contains a value for both `my_argument` and `my_int_argument`.
#
# Line (9) demonstrates how to access the specific values in the Namespace.
#
# Line (10) prints the help message that has been mentioned several times. Note that it
# includes the arguments and descriptions you provided, but also specifies `-h` and
# `--help` flags. If your user runs the application with the `-h` or `--help` flag, this
# message will be printed, and the program will exit without taking any further action. This
# is a common practice for commandline applications, so Python generates this for you
# automatically.
#
# If you'd like to read more about ArgumentParser, the official docs can be found
# here: https://docs.python.org/3/library/argparse.html#module-argparse
#
# Now, a question you might be asking is "where do the arguments come from?". The
# parsing we've done so far has come from a list, but you supplied the list. Where/how
# does the user supply list? In other words, how do you take something from the
# commandline, like:
#
#     python main.py -m "my argument" -i 100
#
# and get the `-m "my argument" -i 100` as a list, that you can pass to the parse_args
# call?
#
# To do this, you will need to use the `argv` list. The `argv` list contains "argument
# values" supplied by the user. To see this, try creating a new python file named `argv_test.py`,
# with just the following contents:
#
#     from sys import argv
#
#    if __name__ == '__main__':
#        print(argv)
#
# Then run the file from your terminal like this:
#
#    python argv_test.py -a "an argument" -b "another argument" -c -d 10
#
# Note that in the output, the file name is included as the first (0th) argument. When you
# pass the list to your `parse_arguments` call, you will not want that, so you'll have to get
# rid of it (or create a new list without it) before you pass the rest of the arguments into
# the `parse_arguments` call.
#
# Once you have your arguments parsed into a Namespace, you can call your `main` function,
# and pass in the user supplied values for `board_file` and `generations`.
#
# After completing this step, you should have a functional application, that you can run
# from your terminal, with something like:
#
#     python main.py -f boards/single-glider.txt -g 15
#
# or
#
#    python main.py
if __name__ == '__main__':
    pass

# STEP 12
#
# Challenge yourself
#
# Make this program your own, e.g. tweak it to add extra functionality, make adjustments to the
# code to make it cleaner/easier to read, or more efficient, or make a gui.
#
# Here are a few ideas to get you started:
#
# Take extra command line arguments to set the size of a board. Note that these won't
# make sense if `--board-file` is supplied, so you will need to check that size and
# file arguments are not given at the same time, and if they are, tell the user the
# issue before exiting.
#
# Make a `Board` class, and use that, rather than just a list of lists.
#
# Make a `Game` class.
#
# Have the program exit when there are no more live cells, regardless of how many
# generations remain. OR, even more challenging, have the program exit when the
# board "stabilizes," e.g. if you encounter a simple, repeating pattern.