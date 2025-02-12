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
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import os
os.makedirs("charts", exist_ok=True)
my_tickers = ["RKLB", "INTC", "TSLA", "GME", "LCID"]




my_tickers.sort()
for ticker in my_tickers:
    result = yf.Ticker(ticker)
    hist = result.history(period="10d")
    last_ten_days = []
    for date in hist["Close"][:11]:
        last_ten_days.append(date)
    if len(last_ten_days) == 10:
        my_array = np.array(last_ten_days)
        max_price = my_array.max() + (my_array.max()*.05)
        min_price = my_array.min() - (my_array.min()*.05)
        plt.xlabel('Days Ago')
        plt.ylabel('Closing Price')
        plt.axis((9, 0, min_price, max_price ))
        plt.title(f"{ticker} Last 10 Closing Prices")
        plt.plot(my_array)
        plt.savefig(f"charts/{ticker}.png")
    else:
        print(f"Do not have 10 days of data. Only have {len(last_ten_days)} days")
