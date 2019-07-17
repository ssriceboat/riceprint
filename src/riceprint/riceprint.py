## Doxygen header
# @author   Kevin Sacca
# @email    ssriceboat@gmail.com
# @title    Riceprint - A Console Printing Utility
#
# @brief    Console printing/writing utility. Includes methods for overwriting
#           lines for progress bars, debugging status updates, etc. Also has
#           support for easy Color Printing to make your console output pretty.
#           Default color is white (or whatever your terminal default is).
#
#           Import riceprint with the following line:
#           from riceprint import tprint, pprint, progressbar
#
#           Then enjoy printing with pretty colors and fancy formatting.
#           pprint('What a pretty shade of red.', color='red')
#
#           Example unit-test command entry in terminal or CMD:
#           python riceprint.py

## Standard library imports
################################################################################
import os
import shutil
import sys
if os.name == 'nt':
   from colorama import init
   init()


## Constants definition
################################################################################
TERM_SIZE = int(shutil.get_terminal_size().columns)


## Public class definitions
################################################################################
class ConsolePrinter:
   """
   Class object to replace Python's built-in print function. This class supports
   colored console output, temporary-prints, and max line length options.
   This class works on both Windows and Linux operating systems/terminals.
   """
   def __init__(self, buff=TERM_SIZE):
      """
      Create the cp object.
      Only optional input is the buffer length (# cols in your terminal window)
      """
      self.setBuffer(buff)
      self.palette = self.Palette()

   def setBuffer(self, buff):
      """
      Sets the buffer length for each print line. Typically you would want this
      buff value to be the integer number of columns per line in your terminal.
      """
      self.buff = abs(int(buff))

   def checkMessage(self, msg, color):
      """
      Checks the message for special text and applies a color to the console
      output accordingly.
      ex: Messages starting with ERROR will be colored red,
      ex2: Messages starting with WARNING will be colored yellow.
      """
      special = {"ERROR" : "red", "WARNING" : "darkyellow"}

      for case in special.keys():
         if str.upper(msg).startswith(case):
            color = special[case]
            break

      return color

   def colorLUT(self, color):
      """
      Returns three/four-letter color printing function name.
      """
      # Selectable colors (Default Terminal ANSI Colors)
      palette = { "red" : "RED",     "darkred" : "DRED",
                  "green" : "GRN",   "darkgreen" : "DGRN",
                  "blue" : "BLU",    "darkblue" : "DBLU",
                  "cyan" : "CYN",    "darkcyan" : "DCYN",
                  "magenta" : "MAG", "darkmagenta" : "DMAG",
                  "yellow" : "YLW",  "darkyellow" : "DYLW",
                  "black" : "BLK",   "darkblack" : "DBLK",
                  "white" : "WHT",   "darkwhite" : "DWHT"}

      # Adding shorthand notation of color designation
      abbrev = {  "r" : "red",     "dr" : "darkred",
                  "g" : "green",   "dg" : "darkgreen",
                  "b" : "blue",    "db" : "darkblue",
                  "c" : "cyan",    "dc" : "darkcyan",
                  "m" : "magenta", "dm" : "darkmagenta",
                  "y" : "yellow",  "dy" : "darkyellow",
                  "k" : "black",   "dk" : "darkblack",
                  "w" : "white",   "dw" : "darkwhite"}

      # Check if given final code, save a few extra steps
      if str(color).upper() in palette.values():
         return str(color).upper()

      # Check if short-hand notation was used, convert to full length, no spaces
      color = str(color).lower()
      if color in abbrev.keys():
         color = abbrev[color]
      else:
         for c in "_ -":
            color = color.replace(c, "")

      # Collect color-code function name or default to terminal default of white
      if color in palette.keys():
         return palette[color]
      else:
         return "WHT"

   class Palette:
      """
      Set of functions to print in colors with console string color codes.
      """
      def __init__(self):
         """ Initialize Palette object """
         self.colors = ["red", "darkred", "green", "darkgreen",
                        "blue", "darkblue", "cyan", "darkcyan",
                        "magenta", "darkmagenta", "yellow", "darkyellow",
                        "black", "darkblack", "white", "darkwhite"]

      # Bright Colors
      def RED(self, text):
         """ Prints with Bright Red text. """
         return '\033[1;31m%s\033[0m' % str(text)

      def GRN(self, text):
         """ Prints with Bright Green text. """
         return '\033[1;32m%s\033[0m' % str(text)

      def BLU(self, text):
         """ Prints with Bright Blue text. """
         return '\033[1;34m%s\033[0m' % str(text)

      def MAG(self, text):
         """ Prints with Bright Magenta text. """
         return '\033[1;35m%s\033[0m' % str(text)

      def YLW(self, text):
         """ Prints with Bright Yellow text. """
         return '\033[1;33m%s\033[0m' % str(text)

      def CYN(self, text):
         """ Prints with Bright Cyan text. """
         return '\033[1;36m%s\033[0m' % str(text)

      def WHT(self, text):
         """ Prints with Bright White text. """
         return '\033[1;37m%s\033[0m' % str(text)

      def BLK(self, text):
         """ Prints with Bright Black text. """
         return '\033[1;30m%s\033[0m' % str(text)

      # Dark Colors
      def DRED(self, text):
         """ Prints with Dark Red text. """
         return '\033[0;31m%s\033[0m' % str(text)

      def DGRN(self, text):
         """ Prints with Dark Green text. """
         return '\033[0;32m%s\033[0m' % str(text)

      def DBLU(self, text):
         """ Prints with Dark Blue text. """
         return '\033[0;34m%s\033[0m' % str(text)

      def DMAG(self, text):
         """ Prints with Dark Magenta text. """
         return '\033[0;35m%s\033[0m' % str(text)

      def DYLW(self, text):
         """ Prints with Dark Yellow text. """
         return '\033[0;33m%s\033[0m' % str(text)

      def DCYN(self, text):
         """ Prints with Dark Cyan text. """
         return '\033[0;36m%s\033[0m' % str(text)

      def DWHT(self, text):
         """ Prints with Dark White text. """
         return '\033[0;37m%s\033[0m' % str(text)

      def DBLK(self, text):
         """ Prints with Dark Black text. """
         return '\033[0;30m%s\033[0m' % str(text)


def pprint(msg, color=None, c=None):
   """
   "Permanent Print"

   Prints a string to the console with an optional, (but cool), ANSI color
   assignment. This method uses a newline char at the end of the message
   automatically, so that the next tprint() or pprint() will always be on a new
   line.

   Parameters
   ----------

   msg: str
      A string line you want to print. This function replaces Python's built-in
      print() function to simply add color options. You can specify a print
      color with the additional argument to print(), color='[color-code]'.
   color: str
      One of the standard ANSI color options:

      [r, g, b, c, m, y, k, w, dr, dg, db, dc, dm, dy, dk, dw]
   c: str
      Same as parameter 'color', just an abbreviation. Use whichever you prefer.

   Returns
   -------

   None
   """

   # First, force msg to be a string
   msg = str(msg)

   # Next, get intended 'c' or 'color' argument given.
   choice = list(filter(lambda a: a != None, [color, c]))
   color = choice[0] if len(choice) > 0 else 'dw'

   # Auto-color messages containing special text. Will be ignored by Windows.
   color = cp.checkMessage(msg, color)

   # Calculates size of 'empty' buffer for neatness
   nChars = len(msg)
   buff = (cp.buff - nChars) * ' '

   # Look up color and convert string to color
   code = cp.colorLUT(color)
   convertColor = getattr(cp.palette, code)
   msg = convertColor(msg)

   # Console output with newline so this line is not overwritten.
   sys.stdout.write('\r%s%s\n\r' % (msg, buff))
   sys.stdout.flush()


def tprint(msg, color=None, c=None):
   """
   "Temporary Print"

   Prints a string to the console with an optional, (but cool), ANSI color
   assignment. This method uses a carriage return at the end of the message such
   that the next tprint() or pprint() message will overwrite the same line.

   Parameters
   ----------

   msg: str
      A string line you want to print. This function replaces Python's built-in
      print() function to simply add color options. You can specify a print
      color with the additional argument to print(), color='[color-code]'.
   color: str
      One of the standard ANSI color options:

      [r, g, b, c, m, y, k, w, dr, dg, db, dc, dm, dy, dk, dw]
   c: str
      Same as parameter 'color', just an abbreviation. Use whichever you prefer.

   Returns
   -------

   None
   """

   # First, force msg to be a string
   msg = str(msg)

   # Next, get intended 'c' or 'color' argument given.
   choice = list(filter(lambda a: a != None, [color, c]))
   color = choice[0] if len(choice) > 0 else 'dw'

   # Auto-color messages containing special text. Will be ignored by Windows.
   color = cp.checkMessage(msg, color)

   # Calculates size of 'empty' buffer for neatness
   nChars = len(msg)
   buff = (cp.buff - nChars) * ' '

   # Look up color and convert string to color
   code = cp.colorLUT(color)
   convertColor = getattr(cp.palette, code)
   msg = convertColor(msg)

   # Console output with return carriage so next msg overwrites this line
   sys.stdout.write('\r%s%s\r' % (msg, buff))
   sys.stdout.flush()


def progressbar(done, total, c=None, color=None, char='=', blank=' ',
               width=TERM_SIZE, lend='[', rend=']', keep=False):
   """
   "Progress Bar"

   Takes advantage of tprint's lack of a newline character to repeatedly print
   over the same line in the console/terminal. This will give the effect of a
   moving/updating progress bar.

   If you start a progress bar then use pprint or Python's built-in 'print'
   function, the progress bar will be interrupted and could lead to messy
   output, so keep that in mind.

   Parameters
   ----------

   done: int
      From a scale of zero to 'total' where your current progress is at. If you
      are iterating over a range, the iterated value could be this argument.
   total: int
      The end value of the progress bar, when process is complete. If you are
      iterating over a range, the max value of the range could be this argument.
   color: str
      One of the standard ANSI color options. 'r,g,b,c,m,y,k,w,...'
   c: str
      Same as parameter 'color', just an abbreviation. Use whichever you prefer.
   char: str
      The character you want the progress portion of the bar to be. Default is a
      '=' character. Unicode character codes work. Try char='[backslash]u2587'.
   blank: str
      The character you want the unfinished portion of the bar to be. Default is
      a blank space character.
   width: int
      The desired width of the progress bar. The default is to use the entire
      width of the current terminal window for the progress bar.
   lend: str
      The desired character of the left end of the progress bar. The default
      character is '['.
   rend: str
      The desired character of the right end of the progress bar. The default
      character is ']'.
   keep: bool
      Boolean for whether you want the progress bar to be printed permanently
      (uses a newline character using pprint) or not. If you want the completed
      progress bar to not be overwritten, the last time you call progressbar()
      in your loop, you should give use keep=True.

   Returns
   -------

   None
   """

   # Do some input checking with absolute values, limits, and color choices.
   done, total, width = abs(done), abs(total), abs(width)
   if width + 6 > TERM_SIZE:
      width = TERM_SIZE - 6
   if color != c:
      choice = list(filter(lambda a: a != None, [color, c]))
      color = choice[0] if len(choice) > 0 else 'dw'
   c = color

   # Calculate the percentage done, then get variables for progress bar.
   percent = int((done / float(total)) * 100.0)
   progress = str(percent).rjust(3)
   done = int((percent / 100.0) * width)
   togo = int(width - done)

   # Print the current state of the progress bar to the console
   if keep:
      pprint('%s%%%s%s%s%s' % (progress, lend, done*char, togo*blank, rend), c)
   else:
      tprint('%s%%%s%s%s%s' % (progress, lend, done*char, togo*blank, rend), c)


cp = ConsolePrinter()
if __name__ == '__main__':
   import time

   # Fake a loading bar that takes 2 seconds to complete and print the colors.
   pprint('Loading colored console printer ink...')
   for x in range(100 + 1):
      c = cp.palette.colors[x % 16]
      progressbar(x, 100, color=c, char='\u2587', lend='|', rend='|')
      time.sleep(0.01)
   pprint('Colored console printer ink loaded.')

   pprint('ERROR: This is what an error will look like.')
   pprint('WARNING: This is what a warning will look like.')

   # Test pprint-ing all the colors
   for i in cp.palette.colors:
      pprint('What a lovely shade of %s' % i, c=i)
