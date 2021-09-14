.. _loop:

Loops
=============

1. while
---------------------------------------
Syntax:

.. code-block:: python

    while expression:
       statement(s)

Example:

.. code-block:: python

    count = 0
    while (count < 5):
       print ('The count is:', count)
       count = count + 1

    print ("Thank You!")

Output: ::

    The count is: 0
    The count is: 1
    The count is: 2
    The count is: 3
    The count is: 4
    Thank You!

2. for
---------------------------------------
Syntax:

.. code-block:: python

    for iterating_var in sequence:
       statements(s)

Example:

for statement on List

.. code-block:: python

    >>> for i in [1, 2, 3, 4]:
    ...     print(i)
    ...
    1
    2
    3
    4




for statement on Strings

.. code-block:: python

    >>> for c in "python":
    ...     print(c)
    ...
    p
    y
    t
    h
    o
    n

for statement on Dictionary

.. code-block:: python

    >>> for k in {"x": 1, "y": 2}:
    ...     print(k)
    ...
    y
    x

The range() function
.....................

Syntax:

.. code-block:: python

    range([Include], <Exclude>, [Step Size])

Example:

.. code-block:: python

    >>> range(5)
    range(0, 5)
    >>> list(range(5))
    [0, 1, 2, 3, 4]

for with range function
.......................

Example:

.. code-block:: python

    >>> for var in list(range(5)):
       print (var)
       Output:
            0
            1
            2
            3
            4

Example:

.. code-block:: python

    #!/usr/bin/python3

    cars = ['Renault', 'Nissan',  'Maruti']
    for car in cars:        # traversal of List sequence
       print ('Current car :', car)
    print ("Thank You")

    Output:
    Current car : Renault
    Current car : Nissan
    Current car : Maruti
    Thank You


Iterating by Sequence Index
...........................

Example:

.. code-block:: python

    #!/usr/bin/python3

    cars = ['Renault', 'Nissan',  'Maruti']
    for index in range(len(cars)):
       print ('Current car :', cars[index])

    print ("Thank You")

    Output:
    Current car : Renault
    Current car : Nissan
    Current car : Maruti
    Thank You