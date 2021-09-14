.. _datatyp:

Data Types
=============

1. Number
---------------------------------------
.. note::
    Types of Number

    * int (signed integers)
    * float (floating point real values)
    * complex (complex numbers)


.. list-table:: Example
   :widths: 25 25 50
   :header-rows: 1

   * - int
     - float
     - complex
   * - 5
     - 5.5
     - 2+4j
   * - -100
     - 8.5555
     - -i+2j

How to Assign Numbers

.. code-block:: python

   a = 10


How to Access Numbers

.. code-block:: python

   num1 = 10
   num2 = 5.5
   num3 = 2+3j
   print ("num1 integer: ", num1)
   print ("num2 float: ", num2)
   print ("num3 complex: ", num3)


Output:

.. code-block:: python

    num1 integer:  10
    num2 float:  5.5
    num3 complex:  (2+3j)

2. Strings
---------------------------------------

How to Assign Strings

.. code-block:: python

   mystr = 'python'

How to Access Strings

.. code-block:: python

   mystr = 'python'
   print ("mystr[0]: ", mystr[0])
   print ("mystr[1:5]: ", mystr[1:5])
   print ("mystr[:] ", mystr[:])
   print ("mystr[::]: ", mystr[::])

Output:

.. code-block:: python

    mystr[0]:  p
    mystr[1:5]:  ytho
    mystr[:]:  python
    mystr[::]:  python

3. Lists
---------------------------------------
How to Assign List

.. code-block:: python

   mylist = ['python',1,5.5,'saurabh','100',True]

How to Access List

.. code-block:: python

   mylist = ['python',1,5.5,'saurabh','100',True]
   print ("mylist[0]: ", mylist[0])
   print ("mylist[1:5]: ", mylist[1:5])
   print ("mylist[:]: ", mylist[:])
   print ("mylist[::]: ", mylist[::])

Output:

.. code-block:: python

    mylist[0]:  python
    mylist[1:5]:  [1, 5.5, 'saurabh', '100']
    mylist[:]:  ['python', 1, 5.5, 'saurabh', '100', True]
    mylist[::]:  ['python', 1, 5.5, 'saurabh', '100', True]

4. Tuple
---------------------------------------
How to Assign List

.. code-block:: python

   mytuple = ('python',1,5.5,'saurabh','100',True)

How to Access List

.. code-block:: python

   mytuple = ('python',1,5.5,'saurabh','100',True)
   print ("mytuple[0]: ", mytuple[0])
   print ("mytuple[1:5]: ", mytuple[1:5])
   print ("mytuple[:]: ", mytuple[:])
   print ("mytuple[::]: ", mytuple[::])

Output:

.. code-block:: python

    mytuple[0]:  python
    mytuple[1:5]:  (1, 5.5, 'saurabh', '100')
    mytuple[:]:  ('python', 1, 5.5, 'saurabh', '100', True)
    mytuple[::]:  ('python', 1, 5.5, 'saurabh', '100', True)


5. Dictionary
---------------------------------------
How to Assign Dictionary

.. code-block:: python

   mydict = {'Name':'Saurabh','Marks': 90,'Subjects':['Maths','Science']}

How to Access Dictionary

.. code-block:: python

   mydict = {'Name':'Saurabh','Marks': 90,'Subjects':['Maths','Science']}
   print ("mydict['Name']: ", mydict['Name'])
   print ("mydict['Marks']: ", mydict['Marks'])
   print ("mydict['Subjects']: ", mydict['Subjects'])
   print ("mydict: ", mydict)

Output:

.. code-block:: python

    mydict['Name']:  Saurabh
    mydict['Marks']:  90
    mydict['Subjects']:  ['Maths', 'Science']
    mydict:  {'Name': 'Saurabh', 'Marks': 90, 'Subjects': ['Maths', 'Science']}

