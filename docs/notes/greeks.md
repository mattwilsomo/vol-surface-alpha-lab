# The Option Greeks

> **AI assistance note:** The original ideas, examples, and structure were provided by the author. AI was used to correct grammar, improve formatting, clarify explanations, and complete the mathematical formulas.

The **Greeks** are calculations used to measure the different factors that affect an option’s price.

They are risk-management tools that help traders understand how an option’s value may change when factors such as the underlying price, time to expiration, implied volatility, and interest rates change.

An option’s price can be represented as a function:

[
V = f(S,K,T,\sigma,r,q)
]

where:

| Variable | Meaning                          |
| -------- | -------------------------------- |
| (V)      | Option value                     |
| (S)      | Underlying asset price           |
| (K)      | Strike price                     |
| (T)      | Time to expiration               |
| (\sigma) | Implied volatility               |
| (r)      | Interest rate or risk-free rate  |
| (q)      | Dividend, borrow, or carry yield |

The Greeks are primarily **partial derivatives** of the option price with respect to these inputs.

| Greek | Measures sensitivity to | Main exposure             |
| ----- | ----------------------- | ------------------------- |
| Delta | Underlying price        | Directional exposure      |
| Gamma | Changes in delta        | Convexity or acceleration |
| Theta | Passage of time         | Time decay or carry       |
| Vega  | Implied volatility      | Volatility exposure       |
| Rho   | Interest rates          | Rate sensitivity          |

---

## Delta

[
\Delta = \frac{\partial V}{\partial S}
]

Delta measures the sensitivity of an option’s price to a change in the price of the underlying asset.

For example:

* If a call option has a delta of (0.60), a (+1) move in the underlying should increase the option’s value by approximately (0.60), all else being equal.
* If a put option has a delta of (-0.60), a (+1) move in the underlying should decrease the option’s value by approximately (0.60).

### Typical delta ranges

[
0 \leq \Delta_{\text{call}} \leq 1
]

[
-1 \leq \Delta_{\text{put}} \leq 0
]

Delta changes as the underlying price changes.

For a call option with a strike price of (100):

* **Far out of the money:** Delta may be close to (0).
* **At the money:** Delta is often close to (0.50).
* **Far in the money:** Delta may be close to (1).

Because one standard equity option contract generally represents 100 shares:

* A delta of (0.50) creates approximately the same immediate directional exposure as 50 shares.
* A delta of (1.00) creates approximately the same immediate directional exposure as 100 shares.

Delta is sometimes used as a rough shortcut for the probability that an option will expire in the money. However, **delta is not an exact probability**.

Its more direct use is as a hedge ratio. It estimates how many units of the underlying are required to offset an option position’s immediate directional exposure.

---

## Gamma

[
\Gamma = \frac{\partial \Delta}{\partial S}
= \frac{\partial^2 V}{\partial S^2}
]

Gamma measures how delta changes when the underlying price changes.

* Long options generally have **positive gamma**.
* Short options generally have **negative gamma**.

| Position   |    Gamma | General effect                                |
| ---------- | -------: | --------------------------------------------- |
| Long call  | Positive | Gains can accelerate as the underlying rises  |
| Long put   | Positive | Gains can accelerate as the underlying falls  |
| Short call | Negative | Losses can accelerate as the underlying rises |
| Short put  | Negative | Losses can accelerate as the underlying falls |

### Positive gamma

For a positive-gamma position:

* As the underlying rises, the position becomes more positive in delta.
* As the underlying falls, the position becomes more negative in delta.
* The position generally benefits from sufficiently large realized price movements.

A long-gamma position therefore tends to adjust in a favorable direction as the market moves.

### Negative gamma

For a negative-gamma position:

* As the underlying rises, the position becomes increasingly short relative to the market.
* As the underlying falls, the position becomes increasingly long relative to the market.
* The position generally loses from sufficiently large realized price movements.

A short-gamma position is therefore exposed to adverse acceleration and is commonly described as being **short realized volatility**.

Gamma is generally largest:

* Near the at-the-money strike
* Close to expiration
* When implied volatility is relatively low

---

## Theta

[
\Theta = \frac{\partial V}{\partial t}
]

Theta measures the change in an option’s value as calendar time passes, all else being equal.

It is commonly expressed as the approximate amount an option loses or gains per day because of the passage of time.

Long options usually have negative theta because the remaining opportunity for a favorable move decreases as expiration approaches.

Theta is not linear:

* A 90-day option may decay relatively slowly.
* A three-day at-the-money option may decay rapidly.

Theta and gamma are closely linked. Long-option positions typically have:

[
\Gamma > 0
\qquad\text{and}\qquad
\Theta < 0
]

Short-option positions typically have:

[
\Gamma < 0
\qquad\text{and}\qquad
\Theta > 0
]

Ignoring interest rates, dividends, transaction costs, and other adjustments, the approximate change in a delta-hedged option position can be written as:

[
d\Pi \approx \Theta,dt+\frac{1}{2}\Gamma(dS)^2
]

Using realized and implied volatility, this relationship is often approximated as:

[
d\Pi
\approx
\frac{1}{2}\Gamma S^2
\left(
\sigma_{\text{realized}}^2
--------------------------

\sigma_{\text{implied}}^2
\right)dt
]

This highlights the relationship between gamma, theta, and volatility:

* When buying options, you are generally **long gamma** and **paying theta**. Realized volatility must be high enough relative to implied volatility to overcome time decay, transaction costs, and hedging costs.
* When selling options, you generally **collect theta** but are **short gamma**. Realized volatility must remain sufficiently below implied volatility, and the position must survive large or extreme market moves.

---

## Vega

[
\nu = \frac{\partial V}{\partial \sigma}
]

Vega measures an option’s sensitivity to changes in implied volatility.

Although vega is commonly represented by the symbol (\nu), traders usually refer to it simply as **vega**.

For example, suppose an option has a vega of (0.20). A one-volatility-point increase in implied volatility—for example, from (20%) to (21%)—would increase the option’s value by approximately (0.20), all else being equal.

* Long options are generally **long vega**.
* Short options are generally **short vega**.

When implied volatility rises:

* Long calls generally gain value.
* Long puts generally gain value.
* Short calls and short puts generally lose value.

Vega is not one-dimensional. There is no single implied volatility for an entire market.

Implied volatility varies according to both strike price and expiration:

[
\sigma_{\text{imp}}=\sigma(K,T)
]

This produces an implied-volatility surface containing:

* **Volatility skew or smile** across strike prices
* **Volatility term structure** across expiration dates

---

## Rho

[
\rho = \frac{\partial V}{\partial r}
]

Rho measures an option’s sensitivity to changes in interest rates.

Calls usually have positive rho:

[
\rho_{\text{call}} > 0
]

Higher interest rates generally increase call values because paying the strike price is deferred until expiration, allowing the cash to earn interest in the meantime.

Puts usually have negative rho:

[
\rho_{\text{put}} < 0
]

Higher interest rates reduce the present value of the strike price that may be received when a put is exercised.

Rho usually matters most for:

* Longer-dated options
* High-interest-rate environments
* Options with significant financing or carry effects

For short-dated options, rho is often less important than delta, gamma, theta, and vega.
