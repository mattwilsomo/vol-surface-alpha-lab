import numpy as np
from scipy.stats import norm 

TOLERANCE = 0.01

def d1_d2(spot: float, strike: float, time_to_expiry: float, risk_free_rate: float, volatility: float) -> tuple[float, float]:
    d1 = (np.log(spot/strike) + (risk_free_rate + 0.5 * volatility **2) * time_to_expiry) / (volatility * np.sqrt(time_to_expiry))
    d2 = d1 - volatility * np.sqrt(time_to_expiry)

    return d1,d2

def black_scholes_call_price(spot: float, strike: float, time_to_expiry: float, risk_free_rate: float, volatility: float) -> float:
    if volatility <=0:
        raise ValueError("Volatility must be positive")

    if time_to_expiry <= 0:
        raise ValueError("time_to_expiry must be positive")

    d1,d2 = d1_d2(spot, strike, time_to_expiry, risk_free_rate, volatility)
    
    #the amount of shares you would need to buy to hedge an option 
    delta = norm.cdf(d1, 0, 1)
    #the rist neutral probability that the option will end up expriting in the money 
    prob_ITM = norm.cdf(d2, 0, 1)

    discount = np.exp(-1 * risk_free_rate * time_to_expiry)

    return spot * delta - strike * discount * prob_ITM


def black_scholes_put_price(spot: float, strike: float, time_to_expiry: float, risk_free_rate: float, volatility: float) -> float:

    if volatility <= 0:
        raise ValueError("Volatility must be positive")
    
    if time_to_expiry <= 0:
        raise ValueError("time_to_expiry must be positive")
    
    d1,d2 = d1_d2(spot, strike, time_to_expiry, risk_free_rate, volatility)

    delta = norm.cdf(-1*d1, 0, 1)
    prob_ITM = norm.cdf(-1 * d2, 0, 1)

    discount = np.exp( -1 * risk_free_rate * time_to_expiry)

    return strike * discount * prob_ITM - spot * delta


def black_scholes_put_IV(spot: float, strike: float, time_to_expiry: float, risk_free_rate: float, option_price: float) -> float: 
    """
    Using the Newton-Raphson method we will determine the implied volatility of an option given its price 
    """
    
    guess = 0.2

    model_price = black_scholes_put_price(spot, strike, time_to_expiry, risk_free_rate, guess)

    count = 0
    # Implements the newton raphson method
    while abs(model_price - option_price) > TOLERANCE:
        d1,d2 = d1_d2(spot, strike, time_to_expiry, risk_free_rate, guess)
        # This is the first derivative of the Black-scholes option price with respect to volatility 
        vega = spot * np.sqrt(time_to_expiry) * norm.pdf(d1)

        # if vega ecomes too small(deep ITM/OT< or near expiry then Newton Raphson can become unstable )
        if abs(vega) < 1e-8:
            raise RuntimeError("Vega too small, Newton-Raphson failed.")

        model_price = black_scholes_put_price(spot, strike, time_to_expiry, risk_free_rate, guess)

        guess = guess - (model_price - option_price)/ vega
        #makes sure the guess does not become less than 0
        guess = max(1e-6, guess)

        count +=1
        if count > 100:
            raise RuntimeError("Newton-Raphson not converging")
    
    return guess


def black_scholes_call_IV(spot: float, strike: float, time_to_expiry: float, risk_free_rate: float, option_price: float) -> float:
    ...

