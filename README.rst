riceprint
=========

About
=====

Author: Kevin Sacca ssriceboat@gmail.com

Simple Python package to replace the built-in print() function. This
module contains functions for colored print statements and temporary
print statements. Also contained in this package is a full-featured
example usage of this package's tprint() function to create a beautiful
progressbar in the console.

Works on Linux, macOS, Windows.

License
=======

MIT License

Copyright (c) 2019 ssriceboat

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Installation
============

Using pip
~~~~~~~~~

.. code:: bash

    pip install riceprint

Usage:
======

After you have installed the package, check that its working by running
the module directly. This will show you all the vailable print colors:

.. code:: bash

    cd /path/to/riceprint-package/src/riceprint/
    python riceprint.py

Below is an example of how you can use the functions:

.. code:: python

    from riceprint import tprint, pprint, progressbar
    import time

    # Simple pprint, tprint demo
    print('This is not using riceprint.')
    pprint('This is using riceprint. (Same unless you add some spice)')
    pprint('This is using riceprint with style.', 'c')
    tprint('This message will be erased by the next line.', 'b')
    tprint('This message overwrites the previous tprint and will also be overwritten.', 'r')
    pprint('This message overwrites the previous tprint and is permanent.', 'g')

    # Overwriting previous messages, like status changes.
    message = 'This is an example of something you can do with tprint().'
    elements = message.split(' ')
    some_colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w', 'dr', 'dk', 'dc']
    for i in range(len(elements)):
       msg = ''
       for y in range(i + 1):
          msg += elements[y] + ' '

       color = some_colors[i]

       tprint(msg, color)
       time.sleep(0.25)

    # Progress bar example
    for x in range(100 + 1):
       progressbar(x, 100, color='dg', char='\u2587', lend='|', rend='|')
       time.sleep(0.01)

    # Adding keep=True here will leave the completed progressbar in the console
    progressbar(x, 100, color='dg', char='\u2587', lend='|', rend='|', keep=True)

    pprint('Done! I hope you use this package!', 'dm')

