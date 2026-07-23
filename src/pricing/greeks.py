import numpy as np
import scipy.stats

def d1_d2(spot: float, strike: float, rfr: float, time_to_expiry: float, iv: float, dividend: float = 0.0) -> tuple:
    """
    Calculates BSM standard normal d1 and d2 parameters.
    
    d1: Standardized moneyness adjusted for drift and variance.
    d2: Risk-neutral probability of option expiring ITM: N(d2).
    """
    # Floor T to prevent division by zero near or at expiration
    time_to_expiry = max(time_to_expiry, 1e-12)
    
    term_1 = np.log(spot / strike)
    term_2 = (rfr - dividend + 0.5 * (iv**2)) * time_to_expiry
    denom = iv * np.sqrt(time_to_expiry)

    d1 = (term_1 + term_2) / denom
    d2 = d1 - denom 

    return (d1, d2)


def calc_call_delta(time_to_expiry: float, dividend: float, d1: float) -> float:
    # Hedge ratio for calls; e^(-qT) * N(d1)
    return scipy.stats.norm.cdf(d1) * np.exp(-dividend * time_to_expiry)


def calc_put_delta(time_to_expiry: float, dividend: float, d1: float) -> float:
    # Hedge ratio for puts; -e^(-qT) * N(-d1)
    return -scipy.stats.norm.cdf(-d1) * np.exp(-dividend * time_to_expiry)


def calc_gamma(spot: float, time_to_expiry: float, iv: float, dividend: float, d1: float) -> float:
    # Rate of change of Delta per $1 move in underlying (identical for Calls and Puts)
    numerator = np.exp(-dividend * time_to_expiry) * scipy.stats.norm.pdf(d1)
    denom = spot * iv * np.sqrt(time_to_expiry)

    return numerator / denom


def calc_vega(spot: float, time_to_expiry: float, dividend: float, d1: float) -> float:
    # Sensitivity to IV shifts; divided by 100 for trading convention ($ change per 1% IV shift)
    vega = spot * np.exp(-dividend * time_to_expiry) * scipy.stats.norm.pdf(d1) * np.sqrt(time_to_expiry)
    return vega / 100.0


def calc_call_theta(spot: float, strike: float, rfr: float, time_to_expiry: float, iv: float, dividend: float, d1: float, d2: float) -> float:
    # Time decay for calls; divided by 365 for daily loss
    term_1 = -(spot * np.exp(-dividend * time_to_expiry) * scipy.stats.norm.pdf(d1) * iv) / (2 * np.sqrt(time_to_expiry))
    term_2 = rfr * strike * np.exp(-rfr * time_to_expiry) * scipy.stats.norm.cdf(d2)
    term_3 = dividend * spot * np.exp(-dividend * time_to_expiry) * scipy.stats.norm.cdf(d1)

    return (term_1 - term_2 + term_3) / 365.0


def calc_put_theta(spot: float, strike: float, rfr: float, time_to_expiry: float, iv: float, dividend: float, d1: float, d2: float) -> float:
    # Time decay for puts; divided by 365 for daily loss
    term_1 = -(spot * np.exp(-dividend * time_to_expiry) * scipy.stats.norm.pdf(d1) * iv) / (2 * np.sqrt(time_to_expiry))
    term_2 = rfr * strike * np.exp(-rfr * time_to_expiry) * scipy.stats.norm.cdf(-d2)
    term_3 = dividend * spot * np.exp(-dividend * time_to_expiry) * scipy.stats.norm.cdf(-d1)

    return (term_1 + term_2 - term_3) / 365.0


def calc_call_rho(strike: float, rfr: float, time_to_expiry: float, d2: float) -> float:
    # Sensitivity to interest rates; divided by 100 ($ change per 1% rate shift)
    rho = strike * time_to_expiry * np.exp(-rfr * time_to_expiry) * scipy.stats.norm.cdf(d2)
    return rho / 100.0


def calc_put_rho(strike: float, rfr: float, time_to_expiry: float, d2: float) -> float:
    # Sensitivity to interest rates; divided by 100 ($ change per 1% rate shift)
    rho = -strike * time_to_expiry * np.exp(-rfr * time_to_expiry) * scipy.stats.norm.cdf(-d2)
    return rho / 100.0


def call_greeks(spot: float, strike: float, rfr: float, time_to_expiry: float, iv: float, dividend: float = 0.0) -> tuple:
    """Wrapper to compute and return all Call option Greeks as a tuple: (Delta, Gamma, Vega, Theta, Rho)."""
    time_to_expiry = max(time_to_expiry, 1e-12)
    d1, d2 = d1_d2(spot, strike, rfr, time_to_expiry, iv, dividend)

    delta = calc_call_delta(time_to_expiry, dividend, d1)
    gamma = calc_gamma(spot, time_to_expiry, iv, dividend, d1)
    vega = calc_vega(spot, time_to_expiry, dividend, d1)
    theta = calc_call_theta(spot, strike, rfr, time_to_expiry, iv, dividend, d1, d2)
    rho = calc_call_rho(strike, rfr, time_to_expiry, d2)

    return (delta, gamma, vega, theta, rho)


def put_greeks(spot: float, strike: float, rfr: float, time_to_expiry: float, iv: float, dividend: float = 0.0) -> tuple:
    """Wrapper to compute and return all Put option Greeks as a tuple: (Delta, Gamma, Vega, Theta, Rho)."""
    time_to_expiry = max(time_to_expiry, 1e-12)
    d1, d2 = d1_d2(spot, strike, rfr, time_to_expiry, iv, dividend)

    delta = calc_put_delta(time_to_expiry, dividend, d1)
    gamma = calc_gamma(spot, time_to_expiry, iv, dividend, d1)
    vega = calc_vega(spot, time_to_expiry, dividend, d1)
    theta = calc_put_theta(spot, strike, rfr, time_to_expiry, iv, dividend, d1, d2)
    rho = calc_put_rho(strike, rfr, time_to_expiry, d2)

    return (delta, gamma, vega, theta, rho)