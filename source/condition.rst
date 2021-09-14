.. _cond:

Conditions
=============

1. if statement
---------------------------------------
Syntax:

.. code-block::

    if expression:
       statement(s)

Example: ::

    var = 10
    if (var==10):
       print ("my variable is assigned with 10")
       print (var)

    if var:
       print ("my variable is assigned with 10")
       print (var)

    myvar = 0
    if (myvar==0):
       print ("my variable is assigned with 0")
       print (myvar)

    if myvar:
       print ("my variable is assigned with 0")
       print (myvar)
    print ("Thank You!")

Output: ::

    my variable is assigned with 10
    10
    my variable is assigned with 10
    10
    my variable is assigned with 0
    0
    Good bye!

2. if else statement
---------------------------------------
Syntax:

.. code-block:: python

    if expression:
       statement(s)

    else:
       statement(s)

Example:

.. code-block:: python

    Marks=75
    if (Marks>=35):
       print ("Pass: Congratulations!!")
    else:
       print ("Fail: Better luck Next Time!!")

Output: ::

    Pass: Congratulations!!

3. if elif else statement
---------------------------------------
Syntax:

.. code-block:: python

    if expression:
       statement(s)
    elif:
       statement(s)
    else:
       statement(s)

Example:

.. code-block:: python

    Marks=75
    if (Marks>=80):
       print ("Distinction!!")
    elif(Marks>=60 and Marks<80):
       print ("First Division")
    elif(Marks>=45 and Marks<60):
       print ("Second Division")
    elif (Marks >= 35 and Marks < 45):
       print("Third Division")
    else:
       print("Fail")

Output:

.. code-block:: python

    First Division

4. Nested statements
---------------------------------------
Syntax:

.. code-block:: python

    if expression1:
       statement(s)
       if expression2:
          statement(s)
       elif expression3:
          statement(s)
       else
          statement(s)
    elif expression4:
       statement(s)
    else:
       statement(s)

Example:

.. code-block:: python

    num1 = 10
    num2 = 30
    num3 = 20

    if (num1 >= num2):
       if (num1 >= num3):
          greater = num1
       else:
          greater = num3
    elif(num2>=num3):
       greater = num2
    else:
       greater= num3
    print("The Greater number is", greater)

Output:

.. code-block:: python

    The Greater number is 30