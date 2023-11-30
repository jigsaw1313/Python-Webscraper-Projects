# Portfolio Valuation

This Python application scrapes price information from Google Finance for given stock tickers and exchanges, summarizes portfolio valuation, and reflects amounts in USD.

## Usage

1. Import the required methods and models.
```python
from methods import *
from models import *
```

2. Define stocks and create a portfolio with positions.
```python
shop = Stock("SHOP", "TSE")  # CAD
msft = Stock("MSFT", "NASDAQ")  # USD
googl = Stock("GOOGL", "NASDAQ")
bns = Stock("BNS", "TSE")

positions = [Position(shop, 10),
             Position(msft, 2),
             Position(bns, 100),
             Position(googl, 30)]

portfolio = Portfolio(positions)
```

3. Display portfolio summary.
```python
display_portfolio_summary(portfolio)
```

## Models

### Stock
- Ticker: Stock ticker symbol.
- Exchange: Stock exchange.
- Price: Current stock price.
- Currency: Currency of the stock.
- USD Price: Stock price in USD.

### Position
- Stock: Stock object.
- Quantity: Number of shares held.

### Portfolio
- Positions: List of Position objects.

## Methods

### get_fx_to_usd(currency)
- Returns the FX rate from the given currency to USD.

### get_price_information(ticker, exchange)
- Scrapes stock price information from Google Finance.
- Returns a dictionary with ticker, exchange, price, currency, and USD price.

### display_portfolio_summary(portfolio)
- Displays a summary of the portfolio, including ticker, exchange, quantity, price, market value, and percentage allocation.

Feel free to use and customize this application for your portfolio management needs.
