"""
COPYRIGHT: Christopher Rogers

This file, as a template, may be edited and shared, according to the terms
 of the GNU General Public license, the terms of which are here:
 https://www.gnu.org/licenses/gpl-3.0.en.html. Do not post a solution
 (in whole or in part) publicly online.

Additionally, this copyright notice and the license terms must be included in any
re-distribution.


##############
# BEGIN HERE #
##############

This project will walk you through creating a game called "Curdle", a simple
command-line clone of Wordle. To complete this project, you will need some
basic understanding of Python concepts, such as variables, classes, and methods.
If you have not already completed the lights-out project, you should consider
completing that first. At the very least, if you are not already somewhat familiar
with Python, you should read through the documentation in that project.

In this project, new topics will be explained as you hit them.
"""

# Do not add any additional imports. You can complete this project
# with only what has already been imported here.
import time
from random import Random
from sys import argv

# The readline import is not used, but should not be removed.
# By importing the library, we are telling the system to use
# readline for input, which allows us to go back and clear
# lines that were already printed. This isn't necessary on all
# systems, but there's no harm in leaving this here on all
# systems, and ensuring that it works where readline is not the
# default.
import readline  # imported so readline is used for input

# STEP -2
#
# The TextControl and TextColors classes are given to you for
# free. These are used for special features of your terminal
# application. To use them, just add them to your strings and/or
# print them.
# e.g.
#     print(TextColors.RED + "hello " + TextColors.END + "world")
#
# That will print 'hello ' in red, and 'world' in you default terminal
# font color. You can test this in PyCharm's 'Python Console' by running:
#
#    from curdle.main import TextColors
#
# Then run the `print` call above.
#
# Note that while TextColor should work in PyCharm's 'Python Console,'
# TextControl might not work; you may need to use your terminal
# application, or the built-in terminal in PyCharm. To use the built-in
# terminal, at the bottom of the PyCharm window, click the 'Terminal' tab
# (it should be two tabs to the left of the 'Python Console'). Once you are
# presented with your terminal, simply run 'python', then use the following
# imports:
#
#    import readline
#    from curdle.main import TextControl
#
# Then to test, and see the effect, run the following, one line at a time:
#
#    print("1\n2\n3")
#    print((TextControl.LINE_UP + TextControl.LINE_CLEAR) * 4, end='')
#    print("hello")
#
# If everything worked, you should have seen 1,2,3 printed, each number on a new line.
# Then, the next print should have removed them entirely. And the final print("hello")
# should have printed where the original text was.
#
# Note that that print statement makes use of 'string multiplication'. The best way
# to understand what that does, it probably to test it. Try the following:
#
#    print("hello" * 6)
#    many_worlds = "world" * 10
#    print(many_worlds)
#
# One final note - you may have also noticed the `end=''` in that print statement.
# This is an argument to the `print` function, and says we want to end what we are
# printing with the empty string. By default, the value is '\n', which is a new line.
# This is why when you call `print(<anything>)` normally, it prints the output on its
# own line. If this doesn't quite make sense, try playing with different endings:
#
#    print("hello", end=" world")
#    print("python is", end=" fun")
#    print("newlines are the default", end='\n')
#
# If you would like more information on this, run `help(print)` in your python
# console.
class TextControl():
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'

class TextColors():
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'


# STEP -1
#
# This banner is also given for free. You can print this at the start of
# the game. You may of course feel free to make your own banner, and
# replace this one.

_BANNER = """
##################################################################################
#  WELCOME TO                                                                    #
#                                                                                #
#  /////////   //     //   ///////     //////      //          /////////    //   #
#  //          //     //   //    //    //    //    //          //          ////  #
#  //          //     //   //     //   //     //   //          //          ////  #
#  //          //     //   ////////    //     //   //          /////////   ////  #
#  //          //     //   //   //     //     //   //          //           //   #
#  //          //     //   //    //    //    //    //          //                #
#  /////////   /////////   //     //   //////      /////////   /////////    //   #
#                                                                                #
# That's Commandline-WORDLE (with a u...)                                        #
##################################################################################
"""

# STEP 1:
#
# Create a set containing all lowercase letters, from a-z.
#
# A set is similar to a list, except that it does not allow
# duplicates - adding the same item to the set multiple times
# has no effect. For example:
#
#     >>> my_set = set()
#     >>> my_set.add(1)
#     >>> my_set.add(2)
#     >>> my_set.add(3)
#     >>> my_set.add(3)
#     >>> my_set.add(3)
#     >>> print(len(my_set))
#     3
#     >>> print(my_set)
#     {1, 2, 3}
#
# Note also that the `set` constructor can take any iterable, and
# create a set from the values. For example:
#
#     >>> my_list = [1,2,3,4,4,4,4]
#     >>> my_set = set(my_list)
#     >>> print(my_set)
#     {1, 2, 3, 4}
#
# And as a very important hint, recall that strings are iterable, so
# you can make a set, using a string:
#
#     >>> my_set = set("hello world")
#     >>> print(my_set)
#     {'e', ' ', 'w', 'h', 'o', 'r', 'd', 'l'}
#
# run `help(set)` if you'd like to see more. As we use the set
# below, we will explain the concepts necessary for this project.
#
# Just to reiterate the task, _LETTERS should be a set containing
# all the lowercase letters of the alphabet, from a-z.
_LETTERS = set()


# STEP 2 (OPTIONAL):
#
# _print_duration
#
# Computers keep track of time by counting the number of seconds (or
# subsecond units) since midnight on January 1st, 1970. This time is
# known as 'epoch.' To test this on your computer run the following in
# a python console:
#
#     >>> from time import time
#     >>> time()
#     1678673101.2905567
#     >>> start = time()
#     >>> end = time()
#     >>> print(start, end)
#     1678673107.9436266 1678673111.3030763
#     >>> print(end - start)
#     3.359449625015259
#
# Note that python is giving you seconds, to everything after the
# decimal is a subsecond. You can see from the above that 3.36 seconds
# passed between when `start = time()` was run, and `end = time()` was
# run. This is shown by printing the difference: end - start.
#
# _print_duration will do something similar, but will format the output
# a little nicer, specifying the number of hours, minutes, and seconds
# between the two values. This will take a little math, and this will make
# the function slightly challenging. If it seems too hard for now, skip it,
# and come back later. This function will only be used at the end of the game
# to print how long the user took to find the answer. It does not affect
# the gameplay at all, and the game can be played without it.
#
# Note that if you want to do truncated division, you can use `//` instead of
# just a `/`. For example:
#
#     >>> 5 / 3
#     1.6666666666666667
#     >>> 5 // 3
#     1
#
# That can be used to get just the whole number portion, (e.g num_seconds // 60 can be
# used to get the whole number of minutes that have elapsed).
#
# Note that if you are dividing floating point numbers (numbers with decimals), the result
# will also be a float, and will always be X.0, e.g.:
#
#     >>> 134.4125 // 60
#     2.0
#
# You can convert that to just an int by wrapping the value in `int(...)`, e.g:
#
#     >>> int(134.4125 // 60)
#     2
def _print_duration(started, ended):
    """
    Given two numbers, representing the times in seconds
    since epoch, prints a string in the following format:

        Play time: X hours Y minutes Z seconds

    Where X, Y, and Z are replaces with the correct values,
    e.g.

        Play time: 0 hours 4 minutes 33 seconds
    """
    pass


# STEP 3:
#
# clear_previous_lines
#
# If you need help with this, read the section of the docs above
# where we discussed TextControl.
def _clear_previous_lines(lines):
    """
    Given an int, `lines`, clean that many lines of previous output.
    """
    pass


# STEP 4
#
# _print_guess_result
#
# This will leverage the TextColors class. See the documentation
# about that class above, if you need help with this method.
def _print_guess_result(current_guess, word):
    """
    Given a guess, and the correct word, prints the guess word
    where letters that are in the correct location are green,
    letters that are in the correct word but not in the correct
    location are orange, and all other letters are not colored.

    For example, if `current_guess` is "hello" and `word` is
    "world", this will print "hello", where the "he" are default
    colors, the first "l" is orange, the second "l" is green,
    and the "o" is orange - the letters "he" do not appear in
    "world" at all, the first "l" represents a letter that does
    appear in "world" but is not in the correct location, the
    second "l" represents a letter that is both in "world" and
    in the correct location, and the "o" represents another letter
    which is in "world", but not in the correct location.
    """
    pass


# STEP 5:
#
# Implement the Game class.
class Game():

    # STEP 5.1
    #
    # __init__
    #
    # Here you will need to initialize your Game object. The only argument that
    # will be necessary to create a game will be a list of words, however, there
    # will be two parameters with default values. The first is `num_guesses`. This
    # is fairly straightforward - it allows you to let the player guess fewer times
    # or more times, to make the game easier or more difficult.
    #
    # The second optional parameter, `seed` will require some explanation:
    #
    # In order to play the game, we are going to choose a word at random,
    # from the list of words supplied. This can be done using the `Random`
    # class built-in to Python. For example:
    #
    #     >>> from random import Random
    #     >>> rand = Random()
    #     >>> my_list = ["these", "are", "words", "in", "a", "list"]
    #     >>> rand.choice(my_list)
    #     'words'
    #     >>> rand.choice(my_list)
    #     'in'
    #
    # If you run that same code (and you should, test it in your console), you
    # will likely see difference words chosen. And if you run the same code again,
    # it will choose different words again. In general, this is what we want. The
    # game is fun because we have no idea what word will be chosen. Always choosing
    # a word at random, however, can make the game difficult to test. For example,
    # if you want to make sure your game properly handles a win on the first guess,
    # that would be very challenging to test, without knowing the word in advance.
    #
    # The solution to this problem is to supply a seed value to your Random class:
    #
    #     >>> from random import Random
    #     >>> seed = 1942
    #     >>> my_list = ["these", "are", "words", "in", "a", "list"]
    #     >>> rand = Random(seed)
    #     >>> rand.choice(my_list)
    #     'words'
    #     >>> rand.choice(my_list)
    #     'these'
    #
    # If you test this yourself, you will see the same results. As long as you
    # construct the Random object with the same seed, the calls to `choice` will
    # produce the same results, in the same order.
    #
    # When you computer wants to generate a "random" number, selection, etc,
    # it takes a 'seed' value, and runs it through a mathematical formula.
    # The next random value is based on the previous result. In this way, a single
    # seed gives you a random sequence of values, rather than a single random value.
    # By default, the seed is typically based on the current time, e.g. the number of
    # milliseconds since epoch. By using this value, the results appear random, because
    # we don't know what the seed was.
    #
    # If that doesn't completely make sense yet, don't worry - the only thing you need
    # to remember is that if you use the same seed, you will get the same "random"
    # selections every time. By default, we will have the seed be "None", so that it
    # is unpredictable. Later on, we'll show you how to set it when you create your game,
    # so that you can test with known sequence of words.
    #
    # Now, to actually write your init method:
    #
    # Create the following values:
    #
    #     self._words
    #     self._num_guesses
    #     self._random
    #     self._word
    #     self._previous_guesses
    #
    # Set self.words and self.num_guesses to the values passed in.
    #
    # self.random should be a new Random object. Be sure to pass the seed in
    # when you create it, as shown in the examples above.
    #
    # self.word and self.previous_guesses should both be set to `None`.
    # These will be set up later, when we start the game. self.word will
    # contain the solution (the word the player is attempting to guess),
    # and self.previous_guesses will contain each of the words the player
    # guesses (this will allow us to determine which letters have/have not
    # been used).
    def __init__(self, words, num_guesses=6, seed=None):
        pass

    # STEP 5.2
    #
    # _initialize
    #
    # This is a very simple method. All this needs to do is:
    #     1. Select a random word from self.words
    #     2. Set self.word to that chosen word
    #     3. Set self.previous_guesses to a new empty list
    #
    # This will be called at the beginning of the `play` method,
    # to set up a new game, with a fresh word.
    def _initialize(self):
        pass

    # STEP 5.3
    #
    # _set_to_alphabetical_string
    #
    # This method will take a set of letters, and return a string. The string
    # should contain all the letters in the set, sorted alphabetically.
    #
    # For example, _set_to_alphabetical_string(set("bcda")) should return
    # "abcd".
    #
    # To sort a set, use the sorted(...) method. This method takes a set,
    # and returns a list:
    #
    #     >>> my_set = set("abdc")
    #     >>> print(sorted(my_set))
    #     ['a', 'b', 'c', 'd']
    #
    # Once you have the sorted list, all you need to do is convert it to a
    # string. HINT: A `for` loop will be useful here.
    def _set_to_alphabetical_string(self, letters):
        pass

    # STEP 5.4
    #
    # _remaining_letters
    #
    # To make this method, you will need to learn a little about sets. Recall that
    # _LETTERS is a set, and that a set, like a list, is a collection of values, with
    # two key differences being that a set does not allow duplicate values, and a set
    # is not ordered.
    #
    # So, why are sets useful? Well, there's an entire branch of mathematics that can
    # explain that (Set https://en.wikipedia.org/wiki/Set_(mathematics)). For our
    # purposes, however, we're mostly going to be relying on the ability for sets to be
    # easily "unioned" (added together), the ability to quickly determine the "difference"
    # between two sets (items in one set, that are not in another), and that 'no duplicates'
    # feature.
    #
    # This method is going to look at all the player's previous guesses, and return
    # a sorted list of all the letters that do not appear in any of those words.
    #
    # For example, if the player has guessed "hello" and "world", this should return
    # 'abcfgijkmnpqstuvxyz', the alphabet (_LETTERS) minus h, e, l, o, w, r, and d.
    #
    # To do this, you will need to create a set containing all the letters from the
    # previously guessed words. There are a few ways to do this. For example, you
    # can create an empty set, and then update it with the set of letters for each
    # word:
    #
    #     >>> some_letters = set()
    #     >>> print(some_letters)
    #     set()
    #     >>> some_letters.update("hello")
    #     >>> print(some_letters)
    #     {'e', 'l', 'o', 'h'}
    #     >>> some_letters.update("world")
    #     >>> print(some_letters)
    #     {'e', 'w', 'h', 'o', 'r', 'd', 'l'}
    #
    # Another option is to create a string, combining all the guesses words, and then
    # make a set from the string:
    #
    #     >>> word1 = "hello"
    #     >>> word2 = "world"
    #     >>> all_words = word1 + word2
    #     >>> print(all_words)
    #     helloworld
    #     >>> my_set = set(all_words)
    #     >>> print(my_set)
    #     {'e', 'w', 'h', 'o', 'r', 'd', 'l'}
    #
    # HINT: This is a good opportunity to practice your `for` loops.
    #
    # Once you have the set of guessed letters, you can find the letters that have
    # not yet been guessed by simply subtracting your set from _LETTERS:
    #
    #     >>> print(my_set)
    #     {'e', 'w', 'h', 'o', 'r', 'd', 'l'}
    #     >>> _LETTERS = set("abcdefghijklmnopqrstuvwxyz")
    #     >>> print(_LETTERS - my_set)
    #     {'n', 'v', 'y', 'm', 'k', 'j', 's', 't', 'q', 'f', 'x', 'u', 'a', 'z', 'g', 'i', 'c', 'p', 'b'}
    #
    # Once you have the set, use your _set_to_alphabetical_string method. Don't forget that you will
    # need to prefix the method name with `self.`, e.g. `self._set_to_alphabetical_list(my_set)`.
    # Return the resulting string.
    def _remaining_letters(self):
        pass

    # STEP 5.5
    #
    # _accept_guess
    #
    # This method will continually prompt the user for a valid guess, until a
    # valid guess is entered. A valid guess is one that is exactly 5 letters long,
    # and a valid word from the `words` list. When a valid guess has been entered,
    # it will return the guess.
    #
    # To accept input from a user, you will need the built-in `input` method:
    #
    #     >>> user_text = input("Please enter some text: ")
    #     Please enter some text: hello world
    #     >>> print(user_text)
    #     hello world
    #
    # The string you pass to `input` will be displayed as a prompt for the player.
    # The prompt should include the un-guessed letters (use your _remaining_letters
    # method).
    #
    # Once you have the player's guess, you will need to verify that it is exactly
    # 5 letters long. If it is not, you should print a message telling them to
    # enter a valid guess of exactly 5 letters. Additionally, if the guessed word
    # is not in `words`, you should print a message indicating that the player did
    # not enter a valid word. In both of these error cases, after printing the error,
    # you should re-prompt the player for a new word.
    #
    # For this method, you will need a `while` loop, and `if/else` statements. If you
    # are not familiar with these concepts, see the `lights_out` project. The documentation
    # for the `__str__` method in the `Light` class describes `if/else` statements, and
    # `STEP 3`, for the `play_game()` function, describes `while` loops.
    #
    # Between each invalid guess, clear the previous lines related to the current
    # guess attempt. When a valid word is found, clear the output from this method,
    # before returning the guess. Use the `_clear_previous_lines(...)` function you
    # defined earlier.
    def _accept_guess(self):
        pass

    # STEP 5.6
    #
    # play
    #
    # This method should first run the `self._initialize` method, to set
    # a word, and set `self._previous_guesses` to an empty list. After the
    # `self._initialize` call, this should:
    #
    # 1) Ask the player to make a guess (use accept guess)
    # 2) Append the guess to the list of previous guesses
    # 3) Print the guess result (use _print_guess_result)
    # 4) Check if the current guess matches self._word
    # 4.1) If it matches, print a message indicating the
    #      player has won the game, and return (exiting the game)
    # 4.2) If it does not match, ask the player for another guess.
    # 4.3) If the user is out of guesses, a message indicating
    #      the user has lost should be printed, and should `return`
    #      to end the game.
    #
    # The guessing/checking should happen in a loop, allowing the user
    # at most `self._num_guesses` guesses, before ending the game.
    #
    # OPTIONAL: If you implemented the _print_duration function, you can
    # use that here to print the amount of time the user played the game.
    # You can use `time.time()` to get the current time. Use that once
    # before you loop to get the start time, then once after the game
    # has been won or lost, to get the end time. Then you can pass those
    # values to your `_print_duration` function.
    def play(self):
        pass


# STEP 6 (OPTIONAL)
#
# _get_words_list
#
# The words/american-english file has been included in this project
# to allow you to generate a long list of words for the game. You can
# of course supply your own list of words (e.g. `["hello", "world",...]),
# but it would be pretty tedious to type us a long list. Instead, you can
# read from the file, filter to the relevant words, and return the result
# a list. Then you can simply pass that list in when you create the Game
# instance.
#
# To read from the file and get a list of all words, use the following:
#
#     with open('words/american-english') as words_file:
#         all_words = words_file.read().split('\n')
#
# That will give you a list of strings. Don't worry about the details
# of how this works for now - just know that all_words is a list, and you
# can now work with it like any other.
#
# Once you have the `all_words` list, create a new empty list. Then, iterate
# over `all_words`, and add valid words to your new list. Valid words are those
# that are 5 letters long, and contain only the characters `a-z` (some words
# in the file contain special characters, such as apostrophes, as in "world's",
# and we do not want to include those when we play the game). Note that
# characters are comparable:
#
#     >>> print("a" < "h")
#     True
#     >>> print("h" < "z")
#     True
#     >>> print("a" < "'")
#     False
#
# You will want to keep only words where each letter is >= 'a' and <= 'z'.
#
# Return your new list, containing only the valid words.
def _get_words_list():
    pass


# STEP 7
#
# Play the game! At this point, you should be able to run
# this file, and play a game. If you did not do step 6 (implementing
# _get_words_list), in the `if` block below, create a list of words,
# and pass to the `Game` constructor (replacing the call to
# `_get_words_list()`
if __name__ == '__main__':
    print(_BANNER)
    game = Game(_get_words_list())
    game.play()

