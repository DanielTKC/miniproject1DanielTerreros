"""

INF601 - Programming in Python

Assignment # Mini Project 1
I, Daniel Terreros, affirm that the work submitted for this assignment is entirely my own. 
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, 
or the use of unauthorized materials. I have neither provided nor received unauthorized assistance 
and have accurately cited all sources in adherence to academic standards. I understand that failing to 
comply with this integrity statement may result in consequences, including disciplinary actions as 
determined by my course instructor and outlined in institutional policies. By signing this statement, I
acknowledge my commitment to upholding the principles of academic integrity.

"""
import pprint
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

mytickers = ["RKLB", "INTC", "TSLA", "GME", "LCID"]
mydata = {}



mytickers.sort()
for ticker in mytickers:
    result = yf.Ticker(ticker)
    hist = result.history(period="10d")
    last_ten_days = []
    for date in hist["Close"][:11]:
        last_ten_days.append(date)
    if len(last_ten_days) == 10:
        myarray = np.array(last_ten_days)
        max_price = myarray.max() + (myarray.max()*.05)
        min_price = myarray.min() - (myarray.min()*.05)
        plt.xlabel('Days Ago')
        plt.ylabel('Closing Price')
        plt.axis((9, 0, min_price, max_price ))
        plt.title(f"{ticker} Last 10 Closing Prices")
        plt.plot(myarray)
        plt.show()
    else:
        print(f"Do not have 10 days of data. Only have {len(last_ten_days)} days")
