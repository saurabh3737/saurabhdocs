.. _cls:

Classes and Objects
===================

Creating Classes
----------------

Syntax:

.. code-block:: python

    class ClassName:
       'Optional class documentation string'
       class_suite

Example:

.. code-block:: python

    class Student:
       'Common base class for all students'
       studCount = 0

       def __init__(self, name, marks):
          self.name = name
          self.marks = marks
          Student.studCount += 1

       def displayCount(self):
         print ("Total Student %d" % Student.studCount)

       def displayStudent(self):
          print ("Name : ", self.name,  ", Marks: ", self.marks)

Creating Instances
------------------

.. code-block:: python

    This would create first object of Student class
    stud1 = Student("Saurabh", 75)
    This would create second object of Student class
    stud2 = Student("SJ", 90)

Accessing Attributes
--------------------

.. code-block:: python

    stud1.displayStudent()
    stud2.displayStudent()
    print ("Total Student %d" % Student.studCount)

Complete Program

.. code-block:: python

    class Student:
       'Common base class for all students'
       studCount = 0

       def __init__(self, name, marks):
          self.name = name
          self.marks = marks
          Student.studCount += 1

       def displayCount(self):
         print ("Total Student %d" % Student.studCount)

       def displayStudent(self):
          print ("Name : ", self.name,  ", Marks: ", self.marks)

    #This would create first object of Student class
    stud1 = Student("Saurabh", 75)
    #This would create second object of Student class
    stud2 = Student("SJ", 90)
    stud1.displayStudent()
    stud2.displayStudent()
    print ("Total Student %d" % Student.studCount)

Output:

.. code-block:: python

    Name :  Saurabh , Marks:  75
    Name :  SJ , Marks:  90
    Total Student 2

Built-In Class Attributes
-------------------------

.. note::

    * *__dict__* − Dictionary containing the class's namespace.

    * *__doc__* − Class documentation string or none, if undefined.

    * *__name__* − Class name.

    * *__module__* − Module name in which the class is defined. This attribute is "__main__" in interactive mode.

    * *__bases__* − empty tuple containing the base classes.


.. code-block:: python

    class Student:
       'Common base class for all students'
       studCount = 0

       def __init__(self, name, marks):
          self.name = name
          self.marks = marks
          Student.studCount += 1

       def displayCount(self):
         print ("Total Student %d" % Student.studCount)

       def displayStudent(self):
          print ("Name : ", self.name,  ", Marks: ", self.marks)

    #This would create first object of Student class
    stud1 = Student("Saurabh", 75)
    #This would create second object of Student class
    stud2 = Student("SJ", 90)
    stud1.displayStudent()
    stud2.displayStudent()
    print ("Total Student %d" % Student.studCount)
    print ("Student.__doc__:", Student.__doc__)
    print ("Student.__name__:", Student.__name__)
    print ("Student.__module__:", Student.__module__)
    print ("Student.__bases__:", Student.__bases__)
    print ("Student.__dict__:", Student.__dict__ )

Output:

.. code-block::

    Student.__doc__: Common base class for all students
    Student.__name__: Student
    Student.__module__: __main__
    Student.__bases__: (<class 'object'>,)
    Student.__dict__: {'__module__': '__main__', '__doc__': 'Common base class for all students', 'studCount': 2, '__init__': <function Student.__init__ at 0x015993D0>, 'displayCount': <function Student.displayCount at 0x01599388>, 'displayStudent': <function Student.displayStudent at 0x01599340>, '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__' of 'Student' objects>}


Class Inheritance
-----------------

Syntax:

.. code-block:: python

    class SubClassName (ParentClass1[, ParentClass2, ...]):
       'Optional class documentation string'
       class_suite

Example:

.. code-block:: python

    #!/usr/bin/python3

    class Parent:        # define parent class
       parentAttr = 10
       def __init__(self):
          print ("Calling parent constructor")

       def parentMethod(self):
          print ('Calling parent method')

       def setAttr(self, attr):
          Parent.parentAttr = attr

       def getAttr(self):
          print ("Parent attribute :", Parent.parentAttr)

    class Child(Parent): # define child class
       def __init__(self):
          print ("Calling child constructor")

       def childMethod(self):
          print ('Calling child method')

    c = Child()          # instance of child
    c.childMethod()      # child calls its method
    c.parentMethod()     # calls parent's method
    c.setAttr(20)       # again call parent's method
    c.getAttr()          # again call parent's method

Output:

.. code-block:: python

    Calling child constructor
    Calling child method
    Calling parent method
    Parent attribute : 20


Multiple Inheritance:
---------------------

.. code-block:: python

    class A:        # define your class A
    .....

    class B:         # define your calss B
    .....

    class C(A, B):   # subclass of A and B
    .....

* issubclass(sub, sup)
* isinstance(obj, Class)

Overriding Methods
------------------

.. code-block:: python

    #!/usr/bin/python3

    class Parent:        # define parent class
       def myMethod(self):
          print ('Calling parent class method')

    class Child(Parent): # define child class
       def myMethod(self):
          print ('Calling child class method')

    c = Child()          # instance of child
    c.myMethod()         # child calls overridden method

Output:

.. code-block:: python

    Calling child class method

Magic Methods
-------------
(Built_in Functions or Base Overloading Methods)

.. note::

    1. __init__ ( self [,args...] )
    2. __del__( self )
    3. __repr__( self )
    4. __str__( self )
    5. __cmp__ ( self, x )


Overloading Operators
---------------------

.. code-block:: python

    #!/usr/bin/python3

    class Vector:
       def __init__(self, a, b):
          self.a = a
          self.b = b

       def __str__(self):
          return 'Vector (%d, %d)' % (self.a, self.b)

       def __add__(self,other):
          return Vector(self.a + other.a, self.b + other.b)

    v1 = Vector(2,10)
    v2 = Vector(5,-2)
    print (v1 + v2)

Output:

.. code-block:: python

    Vector(7,8)