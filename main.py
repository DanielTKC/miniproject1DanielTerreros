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

mytickers = ["RKLB", "INTC", "TSLA", "GME", "LCID" ]
mydata = {}

for ticker in mytickers:
    result = yf.Ticker(ticker)
    mydata[ticker] = {'dayHigh': result.info['dayHigh']}
    # print(f"{ticker} \tDaily High: : {result.info['dayHigh']}")

pprint.pprint(mydata)
dat = yf.Ticker("MSFT")


#pprint.pprint(dat.info)

# hist = dat.history(period="10d")
# pprint.pprint(hist)
