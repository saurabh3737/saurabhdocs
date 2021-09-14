.. _modpackg:

Modules and Packages
====================

1. Creating Modules
...................
a) import
.........

Syntax:

.. code-block:: python

    import module1[, module2[,... moduleN]

Example:

Step 1:
.......
Create module hello.py

.. code-block:: python

    def myprint_func( par ):
       print "Hello : ", par
       return

Step 2:
.......
Now import this module hello.py in your test.py

.. code-block:: python

    #!/usr/bin/python3

    # Import module hello
    import hello

    # Now you can call defined function that module as follows
    hello.myprint_func("Saurabh")

    Output:
    Hello : Saurabh

b) The from...import Statement
..............................

Python's from statement lets you import specific attributes from a module into the current namespace
Syntax:

.. code-block:: python

    from modname import name1[, name2[, ... nameN]]

2. Creating Packages
....................

Step 1:
.......
Consider a file Apple.py available in Phone directory. This file has the following line of source code −

.. code-block:: python

    #!/usr/bin/python3

    def Apple():
    print ("I'm Apple Phone")

Step 2:
.......
Similar, we have other two files having different functions with the same name as above.
They are −

Phone/Nokia.py file having function Nokia()

Phone/Oppo.py file having function Oppo()

Step 3:
.......
Now, create one more file __init__.py in the Phone directory −

Phone/__init__.py

Step 4:
.......
To make all of your functions available when you have imported Phone, you need to put explicit import statements in __init__.py as follows −

.. code-block:: python

    from Apple import Apple
    from Nokia import Nokia
    from Oppo import Oppo

Step 5:
.......
After you add these lines to __init__.py, you have all of these classes available when you import the Phone package.

.. code-block:: python

    #!/usr/bin/python3

    # Now import your Phone Package.
    import Phone

    Phone.Apple()
    Phone.Nokia()
    Phone.Oppo()

    Output:
    I'm Apple Phone
    I'm Oppo Phone
    I'm Nokia Phone