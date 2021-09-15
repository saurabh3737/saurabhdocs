.. _parallel:

Basics of Concurrency vs Parallelism
====================================

* **CPU**
We can think of a CPU as the brain of a computer. A CPU has its cycles that are essentially the time that the CPU takes for the execution of one processor operation. One tick of a cycle is 1 bytecode instruction.

* **Cores And Processes**
1. A CPU can have multiple cores.
2. Each core can run multiple processes.
3. A process is essentially the applications/the instructions of the programs we run on our computer.
4. Each process has its own memory space.

Example:
If we click on the Processes tab, we will see all of the processes that are currently running on our computer such as iexplorer.exe, chrome.exe, PyCharm, Python.exe, and so on. Each Python process has its own Python interpreter, memory space, and the GIL (which I will explain shortly).

* **Threads**
1. Furthermore, each process can run multiple threads within its context.
2. A thread is a set of coded computer instructions.
3. Each thread has its own memory space.
4. It also has access to the process memory and context information.
Example:
When we run a process, such as Python.exe, it executes the code within its Main thread. The main thread can start up multiple threads. Subsequently, a process can start up multiple subprocesses.

A Cooking Example
-----------------
This example will help us understand the concurrency and parallelism concepts better

Scenario:
It’s a Sunday morning and I am expecting 10 of my friends to visit my house for lunch. I have around 3 hours to cook a meal for all of my 10 friends.
So I decide to write down the sequence of the cooking steps along with the time each of these steps would take me:

.. image:: image/cook.png
  :width: 550
  :alt: Alternative text

Now, some of the steps are more time consuming than others.

1. I start by washing vegetables which would take me around 5 minutes.
2. Then I move on to cutting the vegetables which consume around 13 minutes of my time.
3. The cooking process requires boiling the vegetables which can take around 30 minutes.
4. Lastly, I serve the cooked food on a plate that takes around 2 minutes.

In total, it would consume approximately 50 minutes to cook the food for one of my friends.
Now, repeat the process 10 times and it will take me 500 minutes.
That’s around 8 hours of cooking.

* **But hold on, I only have 3 hours to do an 8 hours task.**
* **How do I do 8 hours task within 3 hours?**
* **Can I parallelise it?**

.. image:: image/cook2.png
  :width: 550
  :alt: Alternative text

When to use Threads versus Processes
------------------------------------

* **Threads** are typically best for IO tasks or tasks involving external systems since threads work well to combine results quickly. On the other hand, processes need to pickle their results and therefore take more time to combine results from multiple processes.

* **Threads** provide no benefit for expensive CPU tasks since threads must run within the GIL.

* **Multiple processes** can speed up Python operations that are CPU intensive because they can utilize multiple cores and avoid Python's GIL.

Concurrency in Python
---------------------
One of the most frequently asked questions from beginning Python programmers when they explore multithreaded code for optimisation of CPU-bound code is
**"Why does my program run slower when I use multiple threads?".**

* The expectation is that on a multi-core machine a multithreaded code should make use of these extra cores and thus increase overall performance.
* Unfortunately the internals of the main Python interpreter, CPython, negate the possibility of true multi-threading due to a process known as the Global Interpreter Lock (GIL).

* The GIL is necessary because the Python interpreter is not thread safe.
* This means that there is a globally enforced lock when trying to safely access Python objects from within threads.
* At any one time only a single thread can acquire a lock for a Python object or C API.
* The interpreter will reacquire this lock for every 100 bytecodes of Python instructions and around (potentially) blocking I/O operations.
* Because of this lock CPU-bound code will see no gain in performance when using the Threading library,
* But it will likely gain performance increases if the Multiprocessing library is used.

.. image:: image/gil.png
  :width: 550
  :alt: Alternative text

**Concurrent applications are usually less expensive than parallel applications because creating new processes are more expensive than creating new threads.**

Python Global Interpreter Lock (GIL)
-------------------------------------

The GIL is one of the most important concepts to understand for the advanced Python users.
To understand GIL.

* It’s important to remember that the python memory manager is not thread-safe.
* As a result, multi-threads can update the same object in memory.
* This can end up corrupting the state of objects in an application.
* CPython is built on C code and the interpreter's internal structures along with the C code structures are not thread-safe.

**The GIL is a lock acquired by the Python Interpreter**
**GIL ensures that only one thread can run the interpreter at a given instance of time.**

How To MultiProcess In Python?
------------------------------

* Finally, I wanted to explain how parallelism works in Python.
* Most of the data cleaning and model training tasks in data science are CPU bound in nature.
* We can improve the performance of CPU bound operations in a multi-core machine by utilising the multiprocessing features of Python.