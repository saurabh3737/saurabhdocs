.. _thread:

Multithreading
==============

**Running several threads is similar to running several different programs concurrently**


**Advantages :**

1. Multiple threads within a process share the same data space with the main thread
2. Share information
3. Communicate with each other


**A Thread has :**

a. Beginning,
b. Execution sequence
c. Conclusion

**Salient Features :**

* It has an instruction pointer ( keep track of context)
* It can be pre-empted (interrupted)
* It can temporarily be put on hold (yielding)

**Kinds of Threads :**

* Kernel thread (part of operating system)
* User thread

**Modules supported in Python3**

* _thread (backward compatible)
* threading

Starting a New Thread
---------------------

To spawn another thread, you need to call the following method

.. code-block:: python

    _thread.start_new_thread ( function, args[, kwargs] )

Example

.. literalinclude:: mthread1.py
   :emphasize-lines: 16,17

Output:

.. code-block:: python

    Thread-1: Wed Sep 15 11:23:04 2021
    Thread-1: Wed Sep 15 11:23:06 2021
    Thread-2: Wed Sep 15 11:23:06 2021
    Thread-1: Wed Sep 15 11:23:08 2021
    Thread-1: Wed Sep 15 11:23:10 2021
    Thread-2: Wed Sep 15 11:23:10 2021
    Thread-1: Wed Sep 15 11:23:12 2021
    Thread-2: Wed Sep 15 11:23:14 2021
    Thread-2: Wed Sep 15 11:23:18 2021
    Thread-2: Wed Sep 15 11:23:22 2021

**Program goes in an infinite loop. You will have to press ctrl-c to stop**

Threading Module
----------------

The threading module exposes all the methods of the thread module and provides some additional methods −

* **threading.activeCount()** − Returns the number of thread objects that are active.

* **threading.currentThread()** − Returns the number of thread objects in the caller's thread control.

* **threading.enumerate()** − Returns a list of all thread objects that are currently active.

**The threading module has the Thread class that implements threading**
methods provided by the Thread class

* **run()**  - The run() method is the entry point for a thread.

* **start()** - The start() method starts a thread by calling the run method.

* **join([time])** - The join() waits for threads to terminate.

* **isAlive()** - The isAlive() method checks whether a thread is still executing.

* **getName()** - The getName() method returns the name of a thread.

* **setName()** - The setName() method sets the name of a thread.

Creating Thread Using Threading Module
--------------------------------------

**Steps to implement a new thread using the threading module**

1. Define a new subclass of the Thread class.
2. Override the __init__(self [,args]) method to add additional arguments.
3. Then, override the run(self [,args]) method to implement what the thread should do when started
4. Once you have created the new Thread subclass, you can create an instance of it
5. Then start a new thread by invoking the start(), which in turn calls the run() method

Example

.. literalinclude:: mthread2.py
   :emphasize-lines: 32,36

Output:

.. code-block:: python

    Starting Thread-1
    Starting Thread-2
    Thread-1: Wed Sep 15 11:34:21 2021
    Thread-2: Wed Sep 15 11:34:22 2021
    Thread-1: Wed Sep 15 11:34:22 2021
    Thread-1: Wed Sep 15 11:34:23 2021
    Thread-2: Wed Sep 15 11:34:24 2021
    Thread-1: Wed Sep 15 11:34:24 2021
    Thread-1: Wed Sep 15 11:34:25 2021
    Exiting Thread-1
    Thread-2: Wed Sep 15 11:34:26 2021
    Thread-2: Wed Sep 15 11:34:28 2021
    Thread-2: Wed Sep 15 11:34:30 2021
    Exiting Thread-2
    Exiting Main Thread

Synchronizing Threads
---------------------

The threading module has locking mechanism that allows you to synchronize threads.

**Steps to implement synchronization using the threading module**


1. A new lock is created by calling the Lock() method, which returns the new lock.

2. The acquire(blocking) method of the new lock object is used to force the threads to run synchronously.
3. The optional blocking parameter enables you to control whether the thread waits to acquire the lock.

4. If blocking is set to 0, the thread returns immediately
   with a 0 value if the lock cannot be acquired and with a 1 if the lock was acquired.
5. If blocking is set to 1, the thread blocks and wait for the lock to be released.

6. The release() method of the new lock object is used to release the lock when it is no longer required.

Example

.. literalinclude:: mthreadsync.py
   :emphasize-lines: 32,36

Output:

.. code-block:: python

    Starting Thread-1
    Starting Thread-2
    Thread-1: Wed Sep 15 11:42:28 2021
    Thread-1: Wed Sep 15 11:42:29 2021
    Thread-1: Wed Sep 15 11:42:30 2021
    Thread-2: Wed Sep 15 11:42:32 2021
    Thread-2: Wed Sep 15 11:42:34 2021
    Thread-2: Wed Sep 15 11:42:36 2021
    Exiting Main Thread

Multithreaded Priority Queue
----------------------------

**The Queue module allows you to create a new queue object that can hold a specific number of items**

Methods to control Queue

* **get()** - The get() removes and returns an item from the queue.

* **put()** - The put adds item to a queue.

* **qsize()** - The qsize() returns the number of items that are currently in the queue.

* **empty()** - The empty( ) returns True if queue is empty; otherwise, False.

* **full()** - the full() returns True if queue is full; otherwise, False.

Example

.. literalinclude:: mthreadqueue.py
   :emphasize-lines: 32,36

Output:

.. code-block:: python

    Starting Thread-1
    Starting Thread-2
    Starting Thread-3
    Thread-3 processing One
    Thread-3 processing Two
    Thread-3 processing Three
    Thread-3 processing Four
    Thread-3 processing Five
    Exiting Thread-1
    Exiting Thread-3
    Exiting Thread-2
    Exiting Main Thread


