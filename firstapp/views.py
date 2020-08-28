from django.shortcuts import render
import yfinance as yf
from django.http import HttpResponse
from datetime import datetime
import json

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


second_table = []
today = datetime.today()


class Company:

    def __init__(self, name, price, biggest_price_last_year, biggest_price_last_month, image, currency):
        self.name = name
        self.price = price
        self.biggest_price_last_year = biggest_price_last_year
        self.biggest_price_last_month = biggest_price_last_month
        self.image = image
        self.currency = currency


def test(request, companyId):
    companies = []
    nm = companyId
    try:
        companies.append(
            Company(
                yf.Ticker(nm).info['longName'],
                yf.Ticker(nm).history().tail(1)['Close'].iloc[0],
                search_max(yf.Ticker(nm).history(start=str(today.year-1)+ "-01-01", end=str(today.year-1)+ "-12-31").tail(366)['Close']),
                search_max(yf.Ticker(nm).history(period='1mo').tail(31)['Close']),
                yf.Ticker(nm).info['logo_url'],
                yf.Ticker(nm).info['currency']
            ).__dict__
        )

    except:
        print("Something wrong!")
    data = json.dumps(companies)
    return HttpResponse(data)


def index(request):
    name = ["Tesla", "Marriott International", "Apple", "Nice", "SalesForce.com", "Amazon", "Microsoft", "Hyatt", "Starbucks", "American Express", "LVMH"]
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
        search_max(yf.Ticker("TSLA").history(start=str(today.year-1)+ "-01-01", end=str(today.year-1)+ "-12-31").tail(366)['Close']),
        search_max(yf.Ticker("MAR").history(start=str(today.year-1)+ "-01-01", end=str(today.year-1)+ "-12-31").tail(366)['Close']),
        search_max(yf.Ticker("AAPL").history(start=str(today.year-1)+ "-01-01", end=str(today.year-1)+ "-12-31").tail(366)['Close']),
        search_max(yf.Ticker("NICE").history(start=str(today.year-1)+ "-01-01", end=str(today.year-1)+ "-12-31").tail(366)['Close']),
        search_max(yf.Ticker("CRM").history(start=str(today.year-1)+ "-01-01", end=str(today.year-1)+ "-12-31").tail(366)['Close']),
        search_max(yf.Ticker("AMZN").history(start=str(today.year-1)+ "-01-01", end=str(today.year-1)+ "-12-31").tail(366)['Close']),
        search_max(yf.Ticker("MSFT").history(start=str(today.year-1)+ "-01-01", end=str(today.year-1)+ "-12-31").tail(366)['Close']),
        search_max(yf.Ticker("H").history(start=str(today.year-1)+ "-01-01", end=str(today.year-1)+ "-12-31").tail(366)['Close']),
        search_max(yf.Ticker("SBUX").history(start=str(today.year-1)+ "-01-01", end=str(today.year-1)+ "-12-31").tail(366)['Close']),
        search_max(yf.Ticker("AXP").history(start=str(today.year-1)+ "-01-01", end=str(today.year-1)+ "-12-31").tail(366)['Close']),
        search_max(yf.Ticker("MC.PA").history(start=str(today.year-1)+ "-01-01", end=str(today.year-1)+ "-12-31").tail(366)['Close']),
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
    images = [
        yf.Ticker("TSLA").info['logo_url'],
        yf.Ticker("MAR").info['logo_url'],
        yf.Ticker("AAPL").info['logo_url'],
        yf.Ticker("NICE").info['logo_url'],
        yf.Ticker("AMZN").info['logo_url'],
        yf.Ticker("MSFT").info['logo_url'],
        yf.Ticker("H").info['logo_url'],
        yf.Ticker("SBUX").info['logo_url'],
        yf.Ticker("AXP").info['logo_url'],
        yf.Ticker("MC.PA").info['logo_url'],
    ]
    currency = [
        yf.Ticker("TSLA").info['currency'],
        yf.Ticker("MAR").info['currency'],
        yf.Ticker("AAPL").info['currency'],
        yf.Ticker("NICE").info['currency'],
        yf.Ticker("AMZN").info['currency'],
        yf.Ticker("MSFT").info['currency'],
        yf.Ticker("H").info['currency'],
        yf.Ticker("SBUX").info['currency'],
        yf.Ticker("AXP").info['currency'],
        yf.Ticker("MC.PA").info['currency'],

    ]
    data = {
    "Name": name, "Price": price, "Price_in_Year": biggest_price_last_year,
    "Price_in_Month": biggest_price_last_month, "Images": images, "Currency":currency}
    return render(request, "index.html", context=data)


