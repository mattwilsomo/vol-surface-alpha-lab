import csv 
import numpy as np 
from enum import StrEnum

#How the volume of the stock persists day by day 
PERSISTENCE_PARAMETER = 0.75
# How violent the daily volume spikes are, 0.25 means it can swing within +- 0.25 to +- 0.5
VOLUME_VOLATILITY = 0.25

TRADING_DAYS = 252

class Cap(StrEnum):
    PENNY = "pennystock"
    SMALL = "small_cap"
    MID = "mid_cap"
    LARGE = "large_cap"
    MEGA = "mega_cap"

VOLUME_BY_CAP = {
    Cap.PENNY: 500000, #pennystocks
    Cap.SMALL: 10000000, #small cap
    Cap.MID:50000000, #mid cap
    Cap.LARGE: 250000000, #large cap
    Cap.MEGA:1000000000  # mega cap
}

MARKET_CAP_BY_CAP ={
    Cap.PENNY: 250_000_000, #pennystocks
    Cap.SMALL: 1_000_000_000, #small cap
    Cap.MID:5_000_000_000, #mid cap
    Cap.LARGE: 100_000_000_000, #large cap
    Cap.MEGA:500_000_000_000  # mega cap
}

class Stock():
    def __init__(self, name: str, *, volatility: float , growth: float, years: int = 2, starting_price: float = 100, cap_profile: Cap = Cap.MID, seed: int = 42):
        self.name = name
        self.volatility = volatility
        self.growth = growth
        self.years = years
        self.starting_price = starting_price
        self.cap_profile = cap_profile
        self.days = TRADING_DAYS * years
        self.prices = None
        self.log_prices_arr = None
        self.log_returns_arr = None
        self.log_vol = None
        self.shares_outstanding_val = None
        self.rng = np.random.default_rng(seed)

    def generate_prices(self) -> np.ndarray:
        # Uses GBM to generate :the stock prices over the set amount of years 
        
        
        norm = self.rng.normal(0, 1, self.days)
        dt = 1/TRADING_DAYS

        prices = np.empty(self.days)
        prices[0] = self.starting_price


        for i in range(1,self.days,1):

            #Uses GBM to find the prices
            exponential_factor = (self.growth - 1/2 * self.volatility** 2 )* dt + self.volatility * norm[i] *np.sqrt(dt)
            prices[i] = prices [i - 1] * np.exp(exponential_factor)

        self.prices = prices 
        return prices

    def log_prices(self) -> np.ndarray:
        if self.prices is None:
            self.generate_prices()
        #We use the log of the prices so that it is easier to find the daily returns 
        
        self.log_prices_arr = np.log(self.prices)
        return self.log_prices_arr

    def log_returns(self) -> np.ndarray:
        if self.prices is None:
            self.generate_prices()
        if self.log_prices_arr is None:
            self.log_prices()

        self.log_returns_arr = np.diff(self.log_prices_arr, prepend=self.log_prices_arr[0])

        return self.log_returns_arr

    def log_volume(self) -> np.ndarray:
        # We take the log volume because the raw volume cannot be negative 

        if self.prices is None:
            self.generate_prices()
        # monetary value of the daily volume 

        volume_USD = VOLUME_BY_CAP[self.cap_profile]

        log_mean_vol = np.log( volume_USD/self.prices[0])

        log_vol = np.empty(self.days)
        log_vol[0] = log_mean_vol

        for i in range(1,self.days):
            log_vol[i] = log_mean_vol + PERSISTENCE_PARAMETER* (log_vol[i - 1] - log_mean_vol) +   self.rng.normal() * VOLUME_VOLATILITY

        self.log_vol = log_vol
        return log_vol

    @property
    def shares_outstanding(self):


        self.shares_outstanding_val = MARKET_CAP_BY_CAP[self.cap_profile]/self.prices[0]
        return self.shares_outstanding_val

Headers = ["Date", "Ticker", "Price", "Return", "Volume", "Log_Price", "Log_Returns", "Log_Volume" , "Shares_Outstanding"]
stocks = [
    # Volatile pennystock
    Stock("AAA", volatility = 1, growth = 0.5, cap_profile = Cap.PENNY),
    # Mega cap tech company
    Stock("BBB", volatility = 0.25, growth = 0.3, cap_profile = Cap.MEGA),
    # Large industials company
    Stock("CCC", volatility = 0.12, growth = 0.15, cap_profile = Cap.LARGE ),
    # Higher growth tech company 
    Stock( "DDD", volatility = 0.4, growth = 0.4, cap_profile = Cap.MID),
    #Small biotech company 
    Stock("EEE", volatility = 0.6, growth = 0.5, cap_profile = Cap.SMALL),
]       

days = range(stocks[0].days)

prices = [stock.prices if stock.prices is not None else stock.generate_prices() for stock in stocks]
log_prices = [stock.log_prices() for stock in stocks]
returns = [stock.log_returns() for stock in stocks]
volume = [stock.log_volume() for stock in stocks]

filename = "data/synthetic/sythetic_prices.csv"

with open(filename, "w", newline = "") as csvfile:
    csvwriter = csv.writer(csvfile) #create a writer objuect
    csvwriter.writerow(Headers)
    for i in days:
        for stock in stocks:
            csvwriter.writerow([
                i,
                stock.name,
                stock.prices[i],
                np.exp(stock.log_returns_arr[i]),
                np.exp(stock.log_vol[i]),
                stock.log_prices_arr[i],
                stock.log_returns_arr[i],
                stock.log_vol[i],
                stock.shares_outstanding
            ])
            
