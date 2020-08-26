from django.shortcuts import render
import yfinance as yf
from django.http import HttpRequest

tsla =  yf.Ticker("TSLA")
print(tsla.info)
# -------------Company to static table-------------
# 1:Tesla (TSLA)
# 2:Marriott International (MAR)
# 3:Apple (AAPL)
# 4:Nice (NICE)
# 5:SalesForce.com (CRM)
# 6:Amex УТОЧНИТЬ
# 7:LVMH УТОЧНИТЬ
# 8:Starbucks (SBUX)
# 9:Hyatt (H)
# 10:Microsoft (MSFT)
# 11:Amazon (AMZN)


def search_max(arr):
    max_i = arr[0]
    for i in arr:
        if i > max_i:
            max_i = i
    return max_i


def index(request):
    name = ["Tesla", "Marriott International", "Apple", "Nice", "SalecForce.com", "Amazon", "Microsoft", "Hyatt", "Starbucks", "American Express", "LVMH"]
    price = [
            yf.Ticker("TSLA").history().tail(1)['Close'].iloc[0],
            yf.Ticker("MAR").history().tail(1)['Close'].iloc[0],
            yf.Ticker("AAPL").history().tail(1)['Close'].iloc[0],
            yf.Ticker("NICE").history().tail(1)['Close'].iloc[0],
            yf.Ticker("CRM").history().tail(1)['Close'].iloc[0],
            yf.Ticker("AMZN").history().tail(1)['Close'].iloc[0],
            yf.Ticker("MSFT").history().tail(1)['Close'].iloc[0],
            yf.Ticker("H").history().tail(1)['Close'].iloc[0],
            yf.Ticker("SBUX").history().tail(1)['Close'].iloc[0],
            yf.Ticker("AXP").history().tail(1)['Close'].iloc[0],
            yf.Ticker("MC.PA").history().tail(1)['Close'].iloc[0]
            ]
    biggest_price_last_year = [
        search_max(yf.Ticker("TSLA").history(period='12mo').tail(366)['Close']), 
        search_max(yf.Ticker("MAR").history(period='12mo').tail(366)['Close']),
        search_max(yf.Ticker("AAPL").history(period='12mo').tail(366)['Close']),
        search_max(yf.Ticker("NICE").history(period='12mo').tail(366)['Close']),
        search_max(yf.Ticker("CRM").history(period='12mo').tail(366)['Close']),
        search_max(yf.Ticker("AMZN").history(period='12mo').tail(366)['Close']),
        search_max(yf.Ticker("MSFT").history(period='12mo').tail(366)['Close']),
        search_max(yf.Ticker("H").history(period='12mo').tail(366)['Close']),
        search_max(yf.Ticker("SBUX").history(period='12mo').tail(366)['Close']),
        search_max(yf.Ticker("AXP").history(period='12mo').tail(366)['Close']),
        search_max(yf.Ticker("MC.PA").history(period='12mo').tail(366)['Close']),
    ]    
    biggest_price_last_month = [
        search_max(yf.Ticker("TSLA").history(period='1mo').tail(31)['Close']), 
        search_max(yf.Ticker("MAR").history(period='1mo').tail(31)['Close']),
        search_max(yf.Ticker("AAPL").history(period='1mo').tail(31)['Close']),
        search_max(yf.Ticker("NICE").history(period='1mo').tail(31)['Close']),
        search_max(yf.Ticker("CRM").history(period='1mo').tail(31)['Close']),
        search_max(yf.Ticker("AMZN").history(period='1mo').tail(31)['Close']),
        search_max(yf.Ticker("MSFT").history(period='1mo').tail(31)['Close']),
        search_max(yf.Ticker("H").history(period='1mo').tail(31)['Close']),
        search_max(yf.Ticker("SBUX").history(period='1mo').tail(31)['Close']),
        search_max(yf.Ticker("AXP").history(period='1mo').tail(31)['Close']),
        search_max(yf.Ticker("MC.PA").history(period='1mo').tail(31)['Close']),
    ]   
    data = {"Name": name, "Price": price, "Price_in_Year": biggest_price_last_year, "Price_in_Month": biggest_price_last_month}
    return render(request, "index.html", context=data)


def testf(request):
    return HttpRequest("test")