.. _func:

Functions
=============

Categories of Functions
-----------------------

1. Takes Something Returns Something.
2. Takes Something Returns Nothing
3. Takes Nothing Returns Nothing
4. Takes Nothing Returns Nothing


Syntax:

.. code-block:: python

    def func_name(arg):
       "function docstring"
        function_suite
        return [expression]

Example:

.. code-block:: python

    def myfunc(arg):
       "this function prints Hello Python"
        print(arg)
        return

    Call a function
    # Now you can call printme function
    myfunc("This is ")

Pass by Reference vs Pass by Value
..................................

Example 1:

.. code-block:: python

    #!/usr/bin/python3

    # Function definition is here
    def mychange( mylist ):
       "This changes a passed list into this function"
       print ("Values inside the function before change: ", mylist)

       mylist[2]=5
       print ("Values inside the function after change: ", mylist)
       return

    # Now you can call mychange function
    mylist = [1,2,3]
    mychange( mylist )
    print ("Values outside the function: ", mylist)

    Output:
    Values inside the function before change:  [1, 2, 3]
    Values inside the function after change:  [1, 2, 5]
    Values outside the function:  [1, 2, 5]

Example 2:

.. code-block:: python

    #!/usr/bin/python3

    # Function definition is here
    def mychange( mylist ):
       "This changes a passed list into this function"
       mylist = [1,2,3,4] # This would assi new reference in mylist
       print ("Values inside the function: ", mylist)
       return

    # Now you can call mychange function
    mylist = [10,20,30]
    mychange( mylist )
    print ("Values outside the function: ", mylist)

    Output:
    Values inside the function:  [1, 2, 3, 4]
    Values outside the function:  [10, 20, 30]


Function Arguments
-------------------
1. Required arguments
2. Keyword arguments
3. Default arguments
4. Variable-length arguments

1. Required arguments
......................

.. code-block:: python

    #!/usr/bin/python3

        # Function definition is here
        def printme( str ):
           "This prints a passed string into this function"
           print (str)
           return

        # Now you can call printme function
        printme()

    Output:
    Traceback (most recent call last):
       File "test.py", line 11, in <module>
          printme();
    TypeError: printme() takes exactly 1 argument (0 given)

2. Keyword arguments
....................

Example 1:

.. code-block:: python

    #!/usr/bin/python3

    # Function definition is here
    def printme( str ):
       "This prints a passed string into this function"
       print (str)
       return

    # Now you can call printme function
    printme( str = "Hello Python")

    Output:
    Hello Python

Example 2:

.. code-block:: python

   #!/usr/bin/python3

    # Function definition is here
    def printinfo( name, marks ):
       "This prints a passed info into this function"
       print ("Name: ", name)
       print ("Marks ", marks)
       return

    # Now you can call printinfo function
    printinfo( marks = 90, name = "Saurabh" )

    Output:
    Name:  Saurabh
    Age  90

3. Default arguments
....................

.. code-block:: python

    #!/usr/bin/python3

    # Function definition is here
    def printinfo( name, marks = 35 ):
       "This prints a passed info into this function"
       print ("Name: ", name)
       print ("Marks ", marks)
       return

    # Now you can call printinfo function
    printinfo( marks = 90, name = "saurabh" )
    printinfo( name = "James" )

    Output:
    Name:  Saurabh
    Marks  50
    Name:  James
    Marks  35

4. Variable-length arguments
............................

Syntax:

.. code-block:: python

    def functionname([formal_args,] *var_args_tuple ):
       "function_docstring"
       function_suite
       return [expression]

Example:

.. code-block:: python

    #!/usr/bin/python3

    # Function definition is here
    def printinfo( arg1, *vartuple ):
       "This prints a variable passed arguments"
       print ("Output is: ")
       print (arg1)

       for var in vartuple:
          print (var)
       return

    # Now you can call printinfo function
    printinfo( 10 )
    printinfo( 90, 80, 70 )

    Output is:
    10
    Output is:
    90
    80
    70
