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


This project will walk you through creating a game called "Lights Out",
while teaching some of the basics of Object Oriented programming and
Python. Anywhere you see the `pass` keyword, you should replace it with
the appropriate code, as described by the comments above it.

Python OOP (object oriented programming) basics:


Variables:

    In Python, state (information/values) can be maintained in "variables". This is done
    by defining a variable (giving it a name), and "assigning" it a
    value, via the assignment operator: "=". For example:

        my_variable = 5

    Variable names can be almost anything, however, there are a few
    words that should not be used, e.g. 'True', 'False', 'list', and 'dict'.
    These words (non-exhaustive) represent other things in Python, and
    therefore shouldn't be used as variable names.



Functions:

    Functions in python can be "passed" arguments, and then return a value. All
    functions return a value - the default value, if one is not explicitly given,
    is 'None'.

    Functions can be defined like this:

        def my_function(argument1, argument2):
            return argument1 + argument2

    ----

    Arguments to functions are like variables - you can name them almost anything you like,
    and they hold some state for you.

    ----

    You can define variables in a function, and they will be "scoped" to that
    function, meaning they cannot be accessed outside of that function. For example:

        def scale_by_five(value1):
            my_scalar = 5
            scaled_value = value1 * my_scalar
            return scaled_value

    ----

    Functions can "call" other functions, and the result can be saved to a variable.
    For example:

        def add(number1, number2):
            return number1 + number2

        def add3(number1, number2, number3):
            sum = add(number1, number2)
            sum = add(sum, number3)
            return sum

    ----

    In your code, any place that could use a value (a "constant" or a variable), you
    can use a function call. In other words, it is not necessary to save off the result
    of a function call - it is only used for readability, or if the result is used more
    than one time. For example, using the `add` function defined above, we could define
    `add4` like this:

        def add4(number1, number2, number3, number4):
            partial_sum1 = add(number1, number2)
            partial_sum2 = add(number3, number4)
            sum = add(partial_sum1, partial_sum2)
            return sum

    OR like this:

        def add4(number1, number2, number3, number4):
            return add(number1, number2) + add(number3, number4)



Classes:

    A class is a collection of variables representing the state of _something_, and a
    collection of "methods" for interacting with that state (a "method" is a function
    defined on an Object - the terms are often used interchangeably).

    A class can be defined like this:

        class MyClass():
            def __init__(self, scalar, values):
                self.scalar = scalar
                self.values = values

            def scaled_sum(self):
                return self.scalar() * sum(self.values)

            def every_Nth_value(self, n):
                result = []
                for index, value in enumerate(self.values):
                    if index % n == 0:
                        result.append(value)
                return result

    Note that all the methods (functions) take `self` as the first argument. The first argument
    represents the "instance" of the class the function is being "called on". This allows you
    to access that "object's" state. (By convention, the first argument is called `self`, but it
    could be called anything - for sake of ease, everything below will assume convention is
    followed). Python passes this argument in for you, so when you call methods on the object, you
    will not need to pass in anything for `self`, and will just manually pass in the remaining
    arguments (examples will follow).

    The `__init__(self,...)` function is special, in that is is used to "initialize" an
    "instance" of the class, creating an "object". It is sometimes referred to as a "constructor".
    Note that you should not explicitly return anything from this function.

    Within a method, anytime you define a variable with `self.`, you are creating an "instance variable".
    This is state maintained on that specific instance (you can create multiple instances, all with their own
    state). These values can be created in any method, but in practice (and generally by convention) should only be
    done in the `__init__` method.

    You can "construct" an instance of an object like this (using the class defined above):

        my_instance = MyClass(5, [3,5,8,2,1])

    Note that you pass the arguments in that are defined by `__init__(...)`, excluding the `self`
    value`.

    Then you can call methods on the instance like this:

        my_instance.scaled_sum()
        my_instance.every_Nth_value(3)

    Note again that you do not need to pass anything for `self` - python will automatically pass
    that value in for you. the `self` value will always be the object before the `.`

    You can also access the instances variables, e.g.

        my_instance.scalar



Flow of control:

    Program flow can be defined with branch statements, e.g. `if`, and loop
    statements, e.g. `for` and `while`. These constructs will be described
    before the first time they are used below.



LIGHTS OUT

The game of Lights Out is played by attempting to turn lights in a grid off. Each time a light is toggled,
the lights above, below, and beside it are also toggled. The player is tasked with toggling lights until
all of the lights are off.

For example, if we have a grid of lights like this (x = on, o = off):

o o o o o o
o o x o o o
o o o o o o
o o o o o o

if the `x` is toggled, the new state of the board would be:

o o x o o o
o x o x o o
o o x o o o
o o o o o o

If the right-most x were then toggled, the state of the board would be:

o o x x o o
o x x o x o
o o x x o o
o o o o o o
"""




from random import random


##########################################
#  STEP 0:
#
#  Utility functions
#
#  Define the functions below:
##########################################


#  Use the `random` function imported above. A call to `random`
#  returns a value [0, 1). That is, it will generate a value
# from 0 inclusive, to 1 excliseve (greater-than-or-equal to 0,
# but always less than 1). e.g.
#
#  >>> print(random())
#  0.9682691615564194
#
#  >>> print(random())
#  0.2675536986063396
#
# Note that all values in that range are equally likely, so 0.0
# is just as likely as 0.18472, which is just as likely as
# 0.74981839284, which is just as likely as 0.9 (it is a
# "uniform distribution"). This fact can be leveraged to make
# something happen a certain percentage of the time, e.g.
#
#  >>> print(random() < 0.3))
#
# That should print `True` 30% of the time, and `False` 70% of
# the time, because the value of `random()` will be less than
# `0.3` 30% of the time it runs.
#
# To make this more clear, a simplified example may help:
#
# Assume that rather than any value in the range [0, 1), the
# random function must return one of the values in this set:
#
# {0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9}
#
# There are 10 values there. Our simplified random will still
# have a uniform distribution, so all values are equally likely.
# This means each of the values will be chosen about 1 out of
# every 10 calls to our random function. So again, if we had:
#
#  >>> print(random() < 0.3))
#
# That should print `True` 30% of the time, because there are
# three values less than `0.3`, and there are seven values that
# are greater-than-or-equal to `0.3`.
#
# Even though there are many more values to be chosen from in
# the real `random` function, the math works out exactly the
# the same.
#
# You can of course change the values to cause something to happen
# a different percentage of the time, e.g.
#
#  >>> if random() < 0.65:
#          x = 5
#      else:
#          x = 10
#
# This will cause x to be set to five 65% of the time, and set to
# ten the remaining 45% of the time.
#
# With that in mind, define the fifty_fifty function below.


def fifty_fifty():
    """
    return True, 50% of the time, and False the other 50%.
    """
    pass


#  STEP 1:
#
# Create a class called Light
#   * The class should take a boolean argument called `on`
#   * The class should store the argument as an instance variable, also called `on`
#   * The class should have a `toggle` method that flips the `on` variable
#   * The class should implement a `__str__` method, that returns a string representation
#     of the light - it should return 'x' if the light is on and 'o' if the light is off.

class Light():

    # Save the value of `on` into `self.on`
    def __init__(self, on):
        pass

    # Return 'x' if `on` is True, otherwise return 'o'
    # This will allow you to use the `str` method with a light,
    # e.g.
    #
    #     >>> my_light = Light(on=True)
    #     >>> print(str(my_light))
    #     x
    #
    #     >>> my_light = Light(on=False)
    #     >>> print(str(my_light))
    #     o
    #
    #  To do this, you'll need branching logic. Branching can be achieved using the `if`
    #  and `else` keywords. The `if` keyword is used to check if a
    #  condition is True. In the event it is true, the block of code
    #  defined by the `if` is executed. An `else` block can optionally
    #  be defined, and it will run only if the condition is False.
    #  Here are some examples:
    #
    #      values = [1,2,3,4,5,6]
    #      if 4 in values:
    #          print("Found it!")
    #
    #      if len(values) > 10:
    #          print("long list!")
    #      else:
    #          print("short list!")
    def __str__(self):
        pass

    # This can be done with an `if/else`, but there is a shortcut.
    # Think about how you might be able to use the `not` keyword.
    # Don't forget that you need to save the result back into `self.on`.
    def toggle(self):
        """
        Flips the value of `on` from True to False or vice versa.
        """
        pass

#  STEP 2:
#
#  Create a class called "Board".
#    * The class should take an argument called "dimension".
#    * The class should have an instance variable called `lights`.
#    * `lights` should be a two-dimensional list filled with Light objects
#    * The `lights` list should be a square of size `dimension`.
#    * Use the fifty_fifty() function as the argument to light, to randomly
#      turn lights on, e.g. `Light(fifty_fifty())`

class Board():

    #  STEP 2a:
    #
    #  Implement __init__
    #
    #  For this function, you will need to create a 2d list, and
    #  populate it with values. Python has a concept called
    #  "list comprehension" that could be used here, but for sake
    #  of learning, you should use a "for" loop.
    #
    #  A "for" loop iterates over items, and runs a block of code
    #  for each item. For example, you could manually create a list
    #  of items, and iterate over it like this:
    #
    #      my_list = ['a', 'b', 'c', 'd']
    #      for letter in my_list:
    #          print(letter)
    #
    #  A construct that you might find useful here is a `Range`.
    #  A `Range` object is an object that produces a sequence of
    #  integers. You can iterate over the sequence of integers,
    #  just like you could iterate over the list above.
    #
    #  To create a `Range` object, you can use the `range` function.
    #  For example:
    #
    #      twenty_values = range(20)
    #      for value in twenty_values:
    #          print(value)
    #
    #  The code above would print the values from 0 to 19, inclusive (it does _not_ print 20).
    #  You can read more about the `range` function and the `Range` object by opening a python
    #  console, and running `help(range)`, however, the above should be sufficient to complete
    #  this project.
    #
    #  Recall from earlier that a function call can be used any place a value can be used, so it
    #  is not necessary to save off the `Range` object, and the following code would be equivalent
    #  to the above:
    #
    #      for value in range(20):
    #          print(value)
    #
    #  Note that a loop can contain any code, including simple statements, function calls,
    #  and even other loops. For example:
    #
    #      for character in "abc":
    #          for number in [1,2,3]:
    #              print(character, number)
    #
    #  The code above would print the following:
    #
    #     a 1
    #     a 2
    #     a 3
    #     b 1
    #     b 2
    #     b 3
    #     c 1
    #     c 2
    #     c 3
    #
    #  For this task, you may find the list.append method useful. It can be used like this:
    #
    #      >>> my_list = list()
    #      >>> print(my_list)
    #      []
    #      >>> my_list.append("x")
    #      >>> print(my_list)
    #      ['x']
    #      >>> my_list.append("y")
    #      >>> print(my_list)
    #      ['x', 'y']
    #
    #  Be sure that the 2d list you create is a square of size `dimension`,
    #  and save the result into `self.lights`.
    def __init__(self, dimension):
        pass

    #  STEP 2b
    #
    #  Implement __str__
    #
    #  Similar to the Light object, we want a string representation of the board.
    #  This should return a string of the following form:
    #
    #       0 1 2 3 4 5 6 7 8 9
    #   ------------------------
    #   0 | x x o o x x x o o o
    #   1 | o x o x o o x x o x
    #   2 | x x x o x o x o o x
    #   3 | o x o o x x o o o o
    #   4 | o x x o x x o o o o
    #   5 | x x o x o x x x o o
    #   6 | x x o o x x x x x x
    #   7 | x o x o x o x o o o
    #   8 | x x o o x o x x x x
    #   9 | x x o x o o o x o o
    #
    #  This method will be fairly complex, relative to what you have done so far.
    #  You will need for loops and variables to store intermediate state, in order to
    #  build up the final string. Do not be discouraged if it takes you a while to get
    #  it perfect.
    #
    #  To assist you, here is an example that will give you
    #  an idea of how to construct each row:
    #
    #      >>> my_lights = [Light(True), Light(False), Light(False), Light(True), Light(True)]
    #      >>> my_string = ""
    #      >>> my_string = my_string + "line prefix: "
    #      >>> for light in my_lights:
    #      ...     my_string = my_string + " " + str(light)
    #      ...
    #      >>> print(my_string)
    #      line prefix:  x o o x x
    #
    #  Note the use of the `str` function with the `light`. You do not need to
    #  determine whether the light is an 'x' or 'o' here, you just need to use
    #  the `str` function, which will leverage the `__str__` method you implemented
    #  in the Light class.
    #
    #  I would recommend that you test your code at this point. You can do so in Pycharm
    #  by opening the `Python console` at the bottom of the window, and running the
    #  following code (the code assumes you have the top-level python-challenges directory as the
    #  root of your project - if you are working directly in the lights_out directory, substitute
    #  `from lights_out.main...` with `from main...`):
    #
    #      >>> from lights_out.main import Board
    #      >>> board = Board(10)
    #      >>> print(str(board))
    #          0 1 2 3 4 5 6 7 8 9
    #      ------------------------
    #      0 | x o x o x o x x x x
    #      1 | o o x x o o o x o x
    #      2 | o x o x x o x o o o
    #      3 | o x x x o o x x x o
    #      4 | x o o o o o o o o x
    #      5 | o x x x x o x x o o
    #      6 | x x o o o x o x o x
    #
    #  Note that the code above assumes the name of your file is `main.py`. if you change the
    #  name of the file, you will need to adjust the import to match.
    def __str__(self):
        pass

    # STEP 2c
    #
    # Implement all_off
    #
    #  To implement this, you should use nested for loops
    #  and branching logic (see above).
    def all_off(self):
        """
        Returns True if all Lights in board are off, otherwise False.
        """
        pass

    #  STEP 2d
    #
    #  Implement toggle_light
    #
    #  This function will take two numbers as arguments, and should toggle the
    #  light at that location, as well as the lights, above, below, and beside it.
    #
    #  For this function, do not use loops. Instead, acess the lights by their index
    #  in the list. For example:
    #
    #      >>> my_list = ["a", "b", "c", "d"]
    #      >>> print(my_list[2])
    #      c
    #
    #  Keep in mind, to toggle a light, all you have to do is call it's `toggle` function,
    #  e.g.
    #
    #      >>> my_light = Light(on=True)
    #      >>> print(my_light.on)
    #      True
    #      >>> my_light.toggle()
    #      >>> print(my_light.on)
    #      False
    #
    #  You should not need to insert anything into the lists in this function, i.e.
    #  you will not need to do anything like this:
    #
    #      >>> my_lights[3] = Light(on=True)
    #
    #  Instead, you'll just be updating the state of the lights, in place, via the
    #  aforementioned `toggle` method.
    #
    #  Note: Be careful with lights on the ends of the array, e.g. lights in the
    #  first row do not have lights above them, lights in the last column do not
    #  have a light to their right, etc.
    def toggle_light(self, row, column):
        """
        Toggles the light at (row, column), as well as the lights above, below
        and beside.
        """
        pass


#  STEP 3
#
#  Implement play_game()
#
#  The core game consists of a loop, prompting the user for input, and displaying
#  the result of their action.
#
#  To implement this function, you will need a `while` loop. A `while` loop repeatedly
#  runs a block of code while a given condition is true. For example:
#
#      while True:
#          print("Hello!")
#
#  The above loop will run forever.
#
#      while False:
#        print("Hi!")
#
#  The above loop will not run at all.
#
#      counter = 0
#      while counter < 3:
#        print(counter)
#        counter = counter + 1
#
#  The above loop will run 3 times.
#
#  In this function, you'll want to create a board of size 10. Then, you'll
#  need to create a while loop that will run as long as any of the lights
#  are still on (keep in mind your board has an 'all_off' method, that returns
#  True if all of the lights are off).
#
#  On each iteration of the loop, print the string representation of the board
#  e.g. if your board is called `my_board`:
#
#      print(str(my_board))
#
#  After printing the current state of the board, prompt the user for input, first
#  for a row, then a column. Here's an example of how to get the input as a number:
#
#      >>> row = int(input("Row: "))
#      Row: 5
#      >>> print(row)
#      5
#
#  Once you have the row and column, call your board's toggle_light method, and
#  pass in those two values.
#
#  That should be your complete loop - print the board, prompt for input, then update the
#  board with the toggle_light method. When your board's all_off method returns True,
#  the player has won the game, and the loop should stop.

def play_game():
    pass


if __name__ == "__main__":
    play_game()
