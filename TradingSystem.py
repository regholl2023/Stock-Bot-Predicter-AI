from abc import ABC, abstractmethod
from threading import Thread
import yfinance as yf
from math import floor

company_symbols = ["AAPL"]

class TradingSystem(ABC):
    def __init__(self, api, symbol, time_frame, system_id, system_label):
        self.api = api
        self.symbol = symbol
        self.time_frame = time_frame
        self.system_id = system_id
        self.system_label = system_label
        thread = Thread(target=self.system_loop)
        thread.start()

    @abstractmethod
    def buy(self):
        pass

    @abstractmethod
    def sell(self):
        pass

    @abstractmethod
    def loop(self):
        pass

    @abstractmethod
    def create_sequences(data, num_days):
        pass
        
class DayTrader():
    def __init__(self, start_date: str = "2020-01-01",
                 end_date: str = "2023-06-09",
                 stock_symbol: str = "AAPL") -> None:
        pass

"""
NOTE: Change to use amount of stock not money in stock.
"""

all_models = {}#???????????? USE?????
holdings = {}
def update_all(model, manager):
    #predicts tommorrows prices and sorts it
    predictions = {}
    for company_ticker in company_symbols:
        prediction = model.predict()####
        predictions[company_ticker] = prediction
    predictions = predictions.sort()

    #Sell unprofitable ones
    vals = holdings.values()
    length = len(vals)

    keys = holdings.values()
    for holding, amount in zip(vals, keys):
        #if the index is too low, or the prediction is negative
        if keys.index(holding) < 5+length or prediction[company_ticker] < 0:
            manager.sell(amount, holding)

    #Buy new more profitable ones
    for company_ticker in predictions.keys():
        use = manager.check()
        #If there is not enough money to use
        if use <= 5 or prediction[company_ticker] < 0:
            break
        elif stock_price > use:
            continue
        stocks = floor(use/stock_price)
        holdings[company_ticker] = stocks
        manager.buy(stocks, company_ticker)


        

    
