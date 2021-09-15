.. _process:

Multiprocessing
===============

* In order to actually make use of the extra cores present in nearly all modern consumer processors we can instead use the Multiprocessing library.

**Advantages**

* The Multiprocessing library actually spawns multiple operating system processes for each parallel task.
* This nicely side-steps the GIL, by giving each process its own Python interpreter and thus own GIL.
* Hence each process can be fed to a separate processor core and then regrouped at the end once all processes have finished.

**Drawbacks**

* Spawning extra processes introduces I/O overhead as data is having to be shuffled around between processors.
* This can add to the overall run-time.
* Assuming the data is restricted to each process, it is possible to gain significant speedup.

**Of course, one must always be aware of Amdahl's Law!**

CPU Heavy Computation with Multithreading
-----------------------------------------

* The following code illustrates a multithreaded implementation for a "toy" code that sequentially adds numbers to lists. Each thread creates a new list and adds random numbers to it. This has been chosen as a toy example since it is CPU heavy.

* The following code will outline the interface for the Threading library but it will not grant us any additional speedup beyond that obtainable in a single-threaded implementation. When we come to use the Multiprocessing library below, we will see that it will significantly decrease the overall runtime.

Let's examine how the code works.

**Steps:**

1. Firstly we import the threading library.
2. Then we create a function list_append that takes three parameters.
3. The first, count, determines the size of the list to create.
4. The second, id, is the ID of the "job" (which can be useful if we are writing debug info to the console).
5. The third parameter, out_list, is the list to append the random numbers to.
6. The __main__ function creates a size of  and uses two threads to carry out the work.
7. It then creates a jobs list, which is used to store the separate threads.
8. The threading.Thread object takes the list_append function as a parameter and then appends it to the jobs list.
9. Finally, the jobs are sequentially started and then sequentially "joined".
10. The join() method blocks the calling thread (i.e. the main Python interpreter thread) until the thread has terminated.

**This ensures that all of the threads are complete before printing the completion message to the console:**

**Example**

.. literalinclude:: mprocess1.py
   :emphasize-lines: 26, 31, 35

**We can time this code using the following console call:**

.. code-block:: python

    time python thread_test.py

**Output:**

.. code-block:: python

    List processing complete.

    real    0m2.003s
    user    0m1.838s
    sys     0m0.161s


CPU Heavy Computation with Multiprocessing
------------------------------------------

**The only modifications needed for the Multiprocessing implementation include**
* Changing the import line
* The functional form of the multiprocessing.Process line.

**In this case the arguments to the target function are passed separately.**
Beyond that the code is almost identical to the Threading implementation above

**Example**

.. literalinclude:: mprocess2.py
   :emphasize-lines: 32,36

**We can time this code using the following console call:**

.. code-block:: python

    time python multiproc_test.py

**Output:**

.. code-block:: python

    List processing complete.

    real    0m1.045s
    user    0m1.824s
    sys     0m0.231s

* In this case you can see that while the user and sys times have remained approximately the same,
* the real time has dropped by a factor of almost two. This makes sense since we're using two processes.

**we can scale to 4 processors**

**Output:**

.. code-block:: python

    List processing complete.

    real    0m0.540s
    user    0m1.792s
    sys     0m0.269s

**This is an approximate 3.8x speed-up with four processes.**

Process Vs Pool Class
---------------------

**Management**

* The Pool class is easier to use than the Process class because you do not have to manage the processes by yourself.
* It creates the processes, splits the input data, and returns the result in a list.
* It also waits for the workers to finish their tasks, i.e., you do not have to call the join() method explicitly.

**Memory**

* While the Process keeps all the processes in the memory, the Pool keeps only those that are under execution.
* Therefore, if you have a large number of tasks, and if they have more data and take a lot of space too, then using process class might waste a lot of memory.
* The overhead of creating a Pool is more.
* Therefore, when there are a small number of tasks, and they are not repetitive, it is advisable to use a Process in this case.

**I/O operations**

* Both the Process and the Pool class use FIFO (First In First Out) scheduler.
* if the current process is waiting for, or executing an I/O operation, then the Process class halts the current one and schedules another one from the task queue.
* The Pool class, on the other hand, waits for the process to complete its I/O operation, i.e., it does not schedule another one until the current has finished its execution.
* Because of this, the execution time might increase.

* **Process is preferred over Pool when your task is I/O bound** (A program is I/O bound if it spends most of its time waiting for the I/O operation to complete).

**Example:**

we create a file, write to it, and close it using the test() function.

.. literalinclude:: mprocess3.py
   :emphasize-lines: 17,18

**Output:**

.. code-block:: python

    Time taken 0.1002953052520752 seconds

**Let’s do the same using the Pool class.**

.. literalinclude:: mprocess4.py
   :emphasize-lines: 17,18

**Output:**

.. code-block:: python

    Time taken 0.1964569091796875 seconds