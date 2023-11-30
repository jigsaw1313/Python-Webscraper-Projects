from methods import *
from models import *

if __name__ == "__main__":
    shop = Stock("SHOP", "TSE")  # CAD
    msft = Stock("MSFT", "NASDAQ")  # USD
    googl = Stock("GOOGL", "NASDAQ")
    bns = Stock("BNS", "TSE")

    positions = [Position(shop, 10),
                 Position(msft, 2),
                 Position(bns, 100),
                 Position(googl, 30)]

    portfolio = Portfolio(positions)

    display_portfolio_summary(portfolio)

    # Stock -> Position -> Portfolio
