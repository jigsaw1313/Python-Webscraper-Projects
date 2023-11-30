import requests as r
from bs4 import BeautifulSoup
from tabulate import tabulate
from models import Portfolio


def get_fx_to_usd(currency):
    fx_url = f"https://www.google.com/finance/quote/{currency}-USD"
    resp = r.get(fx_url)
    soup = BeautifulSoup(resp.content, "html.parser")

    fx_rate = soup.find("div", {"data-last-price": True})
    fx = float(fx_rate["data-last-price"])
    return fx


def get_price_information(ticker, exchange):
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    resp = r.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")

    price_div = soup.find("div", attrs={"data-last-price": True})
    price = float(price_div["data-last-price"])
    currency = price_div["data-currency-code"]

    usd_price = price
    if currency != "USD":
        fx = get_fx_to_usd(currency)
        usd_price = round(price * fx, 2)

    return {
        "ticker": ticker,
        "exchange": exchange,
        "price": price,
        "currency": currency,
        "usd_price": usd_price
    }


def display_portfolio_summary(portfolio):
    if not isinstance(portfolio, Portfolio):
        raise TypeError("Please provide an instance of the Portfolio type")

    portfolio_value = portfolio.get_total_value()

    position_data = []

    for position in sorted(portfolio.positions,
                           key=lambda x: x.quantity * x.stock.usd_price,
                           reverse=True):
        position_data.append([
            position.stock.ticker,
            position.stock.exchange,
            position.quantity,
            position.stock.usd_price,
            position.quantity * position.stock.usd_price,
            position.quantity * position.stock.usd_price / portfolio_value * 100
        ])

    print(tabulate(position_data,
                   headers=["Ticker", "Exchange", "Quantity", "Price", "Market Value", "% Allocation"],
                   tablefmt="psql",
                   floatfmt=".2f"
                   ))

    print(f"Total portfolio value: ${portfolio_value:,.2f}.")
