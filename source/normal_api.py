from yahoofinancials import YahooFinancials
import pandas as pd
#import concurrent.futures

print("Normal API Program Started .... Please wait for results ...")
import time
start_time = time.time()

def calculate_fcf(ticker):
    print("ticker: ", [ticker][0])

    # make yahoofinancials instance
    yahoo_financials = YahooFinancials(ticker)
    print("yahoofinancials instance got created")


    # get date for the last quarter reported
    last_quarter_reported = next(iter(yahoo_financials.get_financial_stmts('quarterly', 'cash')['cashflowStatementHistoryQuarterly'][ticker][0]))

    # get total cash from operating activities
    print("calculating total from operating activities...")
    tcfoa = yahoo_financials.get_financial_stmts('quarterly', 'cash')['cashflowStatementHistoryQuarterly'][ticker][0][last_quarter_reported]['totalCashFromOperatingActivities']

    # get capital expenditures
    print("calculating capital expenditures...")
    capex = yahoo_financials.get_financial_stmts('quarterly',  'cash')['cashflowStatementHistoryQuarterly'][ticker][0][last_quarter_reported]['capitalExpenditures']

    # get free cash flow
    fcf = tcfoa-abs(capex)

    # return date of last quarter reported and free cash flow
    return last_quarter_reported, fcf


tickers = ['NEM', 'FCX', 'BBL', 'GLNCY', 'VALE', 'RTNTF', 'SCCO', 'AU', 'NGLOY', 'HL']  # ticker list
quarter_dates = []  # list to store quarter dates
fcfs = []  # list to store free cash flows
for ticker in tickers:  # loop through tickers list
    calc_fcf = calculate_fcf(ticker) # use function for API request
    quarter_date = calc_fcf[0] # get date element from function
    fcf = calc_fcf[1]  # get fcf element from function
    # append results to lists
    quarter_dates.append(quarter_date)
    fcfs.append(fcf)

print("Free Cash Flow (FCF): ",fcfs)
print("Time Taken: --- %s seconds ---" % (time.time() - start_time))
