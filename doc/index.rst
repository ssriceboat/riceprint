Welcome to riceprint's documentation!
=====================================

Replacement for Python's built-in print() function that allows for fast colored printing, progress bars, and more. Works on Linux, macOS, Windows.

|gifdemo|

.. |gifdemo| image:: https://github.com/ssriceboat/riceprint/raw/master/screenshots/demo.gif
   :width: 60%

*pprint()* and *tprint()* are the focus of this package.

**pprint** is '*permanent*' print, which automatically adds a newline to the end of your string the same way Python's *print()* function does.

**tprint** is '*temporary*' print, which does not add a newline to the end of your string. Successive tprints will simply overwrite the same line in your console.

Color Codes for pprint() and tprint()
-------------------------------------

+----------+---------+--------------+----------+-------------+-------------------+
| Abbr. CC | Full CC | Result       | Abbr. CC | Full CC     | Result            |
+==========+=========+==============+==========+=============+===================+
| r        | red     | ANSI Red     | dr       | darkred     | ANSI Dark Red     |
+----------+---------+--------------+----------+-------------+-------------------+
| g        | green   | ANSI Green   | dg       | darkgreen   | ANSI Dark Green   |
+----------+---------+--------------+----------+-------------+-------------------+
| b        | blue    | ANSI Blue    | db       | darkblue    | ANSI Dark Blue    |
+----------+---------+--------------+----------+-------------+-------------------+
| c        | cyan    | ANSI Cyan    | dc       | darkcyan    | ANSI Dark Cyan    |
+----------+---------+--------------+----------+-------------+-------------------+
| m        | magenta | ANSI Magenta | dm       | darkmagenta | ANSI Dark Magenta |
+----------+---------+--------------+----------+-------------+-------------------+
| y        | yellow  | ANSI Yellow  | dy       | darkyellow  | ANSI Dark Yellow  |
+----------+---------+--------------+----------+-------------+-------------------+
| k        | black   | ANSI Black   | dk       | darkblack   | ANSI Dark Black   |
+----------+---------+--------------+----------+-------------+-------------------+
| w        | white   | ANSI White   | dw       | darkwhite   | ANSI Dark White   |
+----------+---------+--------------+----------+-------------+-------------------+

.. automodule:: src.riceprint.riceprint
    :members:
    :exclude-members: ConsolePrinter

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Progress Bar
------------

The progressbar() function has a lot of customization already, including being able to choose what your progress bar is made up of. Unicode character strings do work, so you can even make a progress bar of emojis or webding-like characters.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
