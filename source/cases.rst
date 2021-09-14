.. _case:

Case Studies
===================

1. Speeding Up API with Thread Pools
------------------------------------

**Introduction:**

- Application Program Interface (API) Request information server a through calss and to receive valid response.

**Challenge:**

- Retrieving Huge Amount of Data in Quick time is challenging using multiple API Request

**Solution:**

- Use Thread Pools Library


**Setup:**

.. code-block:: python

    pip install yahoofinancials
    pip install pandas


**Model:**

.. note::

    **Free Cash Flow (FCF)**

    .. math::

       FCF = Cash from Operations - Capital Expenditure


###################
Normal API Request:
###################

.. image:: image/api_single.jpg
  :width: 550
  :alt: Alternative text

.. literalinclude:: normal_api.py
   :emphasize-lines: 2,18,38,47

Output:

.. code-block:: python
   :emphasize-lines: 2,18,38,42,43

    Normal API Program Started .... Please wait for results ...
    ticker:  NEM
    yahoofinancials instance got created
    calculating total from operating activities...
    calculating capital expenditures...
    ticker:  FCX
    yahoofinancials instance got created
    calculating total from operating activities...
    calculating capital expenditures...
    ticker:  BBL
    yahoofinancials instance got created
    calculating total from operating activities...
    calculating capital expenditures...
    ticker:  GLNCY
    yahoofinancials instance got created
    calculating total from operating activities...
    calculating capital expenditures...
    ticker:  VALE
    yahoofinancials instance got created
    calculating total from operating activities...
    calculating capital expenditures...
    ticker:  RTNTF
    yahoofinancials instance got created
    calculating total from operating activities...
    calculating capital expenditures...
    ticker:  SCCO
    yahoofinancials instance got created
    calculating total from operating activities...
    calculating capital expenditures...
    ticker:  AU
    yahoofinancials instance got created
    calculating total from operating activities...
    calculating capital expenditures...
    ticker:  NGLOY
    yahoofinancials instance got created
    calculating total from operating activities...
    calculating capital expenditures...
    ticker:  HL
    yahoofinancials instance got created
    calculating total from operating activities...
    calculating capital expenditures...
    Free Cash Flow (FCF):  [1288000000, 939000000, 2877500000, 406000000, 20925000000, 3375500000, 852100000, 245000000, -441500000, 28267000]
    Time Taken: --- 73.05337882041931 seconds ---

#########################
API Request Thread Pools:
#########################

.. image:: image/api_multi.jpg
  :width: 550
  :alt: Alternative text

.. literalinclude:: multi_api.py
   :emphasize-lines: 2,3,18,34,44

Output:

.. code-block:: python
   :emphasize-lines: 2,18,38,42,43

    Thread Pool API Program Started .... Please wait for results ...
    ticker:  NEM
    yahoofinancials instance got created
    ticker:  FCX
    yahoofinancials instance got created
    ticker:  BBL
    yahoofinancials instance got created
    ticker:  GLNCY
    yahoofinancials instance got created
    ticker:  VALE
    yahoofinancials instance got created
    ticker:  RTNTF
    yahoofinancials instance got created
    ticker:  SCCO
    yahoofinancials instance got created
    ticker:  AU
    yahoofinancials instance got created
    ticker:  NGLOY
    yahoofinancials instance got created
    ticker:  HL
    yahoofinancials instance got created
    calculating total from operating activities...
    calculating capital expenditures...
    calculating total from operating activities...
    calculating capital expenditures...
    calculating total from operating activities...
    calculating capital expenditures...
    calculating total from operating activities...
    calculating capital expenditures...
    calculating total from operating activities...
    calculating capital expenditures...
    calculating total from operating activities...
    calculating capital expenditures...
    calculating total from operating activities...
    calculating capital expenditures...
    calculating total from operating activities...
    calculating capital expenditures...
    calculating total from operating activities...
    calculating capital expenditures...
    calculating total from operating activities...
    calculating capital expenditures...
    Free Cash Flow (FCF):  [1288000000, 939000000, 2877500000, 406000000, 20925000000, 3375500000, 852100000, 245000000, -441500000, 28267000]
    Time Taken with ThreadPool: --- 10.280215740203857 seconds ---


**Using Pandas:**

.. code-block:: python

    df = pd.DataFrame({'Ticker': tickers,'Last quarter reported': quarter_dates, 'Free Cash Flow': fcfs})
    df = df.sort_values(by=['Free Cash Flow'], ascending=False)
    df['Free Cash Flow'] = df['Free Cash Flow'] / 1000000000
    df = df.rename(columns={'Free Cash Flow': 'Free Cash Flow (billions $)'})

**Results Table:**

.. image:: image/result_table.jpg
  :width: 550
  :alt: Alternative text
