# Black–Scholes Model

> **AI assistance note:** The original ideas, examples, and structure were provided by the author. AI was used to improve the wording, correct technical notation, complete the formulas, and clarify several explanations.

## What Is the Black–Scholes Model?

The **Black–Scholes model** is a continuous-time mathematical framework used to price European-style financial derivatives.

A European option can only be exercised at expiration, unlike an American option, which may be exercised earlier.

The model obtains a no-arbitrage price through **dynamic replication**. Because an option’s value depends on the underlying asset and time, a portfolio of:

* The underlying asset
* Risk-free borrowing or lending

can be continuously adjusted to replicate the option’s payoff.

If the option can be replicated exactly, the option and the replicating portfolio must have the same price. Otherwise, an arbitrage opportunity would exist.

Because the replication argument removes instantaneous risk, the option’s price does not depend on the underlying asset’s real-world expected return. Instead, the option is priced under the **risk-neutral measure**, under which the expected return of the underlying, after accounting for dividends or carry, is linked to the risk-free rate.

For a dividend-paying asset, the risk-neutral drift is:

[
r-q
]

where (r) is the continuously compounded risk-free rate and (q) is the continuous dividend or carry yield.

In practice, the relevant risk-free rate depends on the currency, collateral arrangement, and maturity. A rate such as SOFR may be used for certain USD-denominated contracts, but it is not universally applicable to every option.

---

## Theoretical Architecture

Under the risk-neutral measure, the underlying asset price is assumed to follow **geometric Brownian motion**:

[
dS_t = (r-q)S_t,dt+\sigma S_t,dW_t^{\mathbb{Q}}
]

where:

| Variable            | Meaning                                                                    |
| ------------------- | -------------------------------------------------------------------------- |
| (S_t)               | Underlying asset price at time (t)                                         |
| (r)                 | Continuously compounded risk-free interest rate                            |
| (q)                 | Continuous dividend, borrow, or carry yield                                |
| (\sigma)            | Constant volatility of the underlying asset                                |
| (dt)                | Infinitesimal change in time                                               |
| (dW_t^{\mathbb{Q}}) | Increment of a Brownian motion under the risk-neutral measure (\mathbb{Q}) |

The model assumes that continuously compounded returns are normally distributed over a fixed time interval. This means the asset price itself follows a lognormal distribution and remains positive.

---

## Core Assumptions

The standard Black–Scholes model assumes:

* The option is European-style.
* Markets are frictionless.
* There are no transaction costs or taxes.
* Trading can occur continuously.
* The underlying asset can be bought or sold in any quantity.
* Short selling is permitted.
* The risk-free rate is constant.
* Volatility is constant.
* Dividend or carry yield is constant.
* The underlying price follows geometric Brownian motion.
* Markets do not experience discontinuous jumps.

These assumptions make the model mathematically tractable, but they do not fully describe real financial markets.

---

## The Black–Scholes Partial Differential Equation

Let the value of an option be:

[
V=V(S,t)
]

Applying Itô’s lemma gives:

[
dV
==

\frac{\partial V}{\partial t}dt
+
\frac{\partial V}{\partial S}dS
+
\frac{1}{2}
\frac{\partial^2 V}{\partial S^2}
(dS)^2
]

Because:

[
(dS)^2=\sigma^2S^2dt
]

the option’s change becomes:

[
dV
==

\left(
\frac{\partial V}{\partial t}
+
(r-q)S\frac{\partial V}{\partial S}
+
\frac{1}{2}\sigma^2S^2
\frac{\partial^2V}{\partial S^2}
\right)dt
+
\sigma S
\frac{\partial V}{\partial S}
dW_t^{\mathbb{Q}}
]

A delta-hedged portfolio can be constructed as:

[
\Pi = V-\Delta S
]

with:

[
\Delta=\frac{\partial V}{\partial S}
]

Choosing this delta removes the instantaneous random component. The resulting riskless portfolio must earn the risk-free rate.

This produces the Black–Scholes partial differential equation:

[
\boxed{
\frac{\partial V}{\partial t}
+
\frac{1}{2}\sigma^2S^2
\frac{\partial^2V}{\partial S^2}
+
(r-q)S\frac{\partial V}{\partial S}
-rV
=0
}
]

The equation applies to many European derivatives, with the derivative’s terminal payoff determining the boundary condition.

For a European call:

[
V(S,T)=\max(S_T-K,0)
]

For a European put:

[
V(S,T)=\max(K-S_T,0)
]

---

## Analytical Solution

For a European call option with continuous dividend yield (q):

[
\boxed{
C
=

## S_0e^{-qT}N(d_1)

Ke^{-rT}N(d_2)
}
]

For a European put option:

[
\boxed{
P
=

## Ke^{-rT}N(-d_2)

S_0e^{-qT}N(-d_1)
}
]

where:

[
d_1
===

\frac{
\ln\left(\frac{S_0}{K}\right)
+
\left(r-q+\frac{1}{2}\sigma^2\right)T
}{
\sigma\sqrt{T}
}
]

and:

[
d_2
===

d_1-\sigma\sqrt{T}
]

Equivalently:

[
d_2
===

\frac{
\ln\left(\frac{S_0}{K}\right)
+
\left(r-q-\frac{1}{2}\sigma^2\right)T
}{
\sigma\sqrt{T}
}
]

The inputs are:

| Variable | Meaning                                          |
| -------- | ------------------------------------------------ |
| (C)      | European call value                              |
| (P)      | European put value                               |
| (S_0)    | Current underlying price                         |
| (K)      | Strike price                                     |
| (T)      | Time to expiration                               |
| (r)      | Continuously compounded risk-free rate           |
| (q)      | Continuous dividend or carry yield               |
| (\sigma) | Volatility                                       |
| (N(x))   | Standard normal cumulative distribution function |

---

## Interpretation of (d_1) and (d_2)

### (d_1)

[
d_1
===

\frac{
\ln\left(\frac{S_0}{K}\right)
+
\left(r-q+\frac{1}{2}\sigma^2\right)T
}{
\sigma\sqrt{T}
}
]

The term (N(d_1)) is closely related to the option’s delta.

For a non-dividend-paying asset:

[
\Delta_{\text{call}}=N(d_1)
]

With a continuous dividend yield:

[
\Delta_{\text{call}}=e^{-qT}N(d_1)
]

For a put:

[
\Delta_{\text{put}}
===================

-e^{-qT}N(-d_1)
]

Therefore, (N(d_1)) should not simply be described as a probability. Its primary interpretation in the pricing formula is as a delta-related weighting factor on the underlying asset.

### (d_2)

[
d_2=d_1-\sigma\sqrt{T}
]

Under the Black–Scholes assumptions:

[
N(d_2)
]

is the risk-neutral probability that a European call finishes in the money:

[
\mathbb{Q}(S_T>K)=N(d_2)
]

Similarly:

[
N(-d_2)
]

is the risk-neutral probability that a European put finishes in the money.

This is a **risk-neutral probability**, not necessarily the real-world probability of the option expiring in the money.

---

## Put–Call Parity

The Black–Scholes call and put prices satisfy put–call parity:

[
\boxed{
C-P
===

## S_0e^{-qT}

Ke^{-rT}
}
]

Equivalently:

[
C+Ke^{-rT}
==========

P+S_0e^{-qT}
]

This relationship shows that a call combined with cash can replicate a put combined with the underlying asset.

If put–call parity is violated beyond trading costs and market frictions, an arbitrage opportunity may exist.

---

## Implied Volatility

Among the main Black–Scholes inputs:

[
S_0,\ K,\ T,\ r,\ q,\ \sigma
]

volatility is the only parameter that cannot be directly observed at the present moment.

The underlying price, strike, maturity, interest rate, and dividend assumptions can generally be observed or estimated from market data. Future volatility, however, is unknown because it represents the annualized standard deviation of the underlying asset’s future returns over the option’s remaining life.

The Black–Scholes formula can therefore be written as:

[
V_{\text{market}}
=================

V_{\text{BS}}
(S_0,K,T,r,q,\sigma_{\text{imp}})
]

The option’s market price is inserted into the equation, and the formula is inverted numerically to solve for:

[
\sigma_{\text{imp}}
]

This value is called **implied volatility**.

There is generally no simple closed-form formula for implied volatility, so numerical methods are used, such as:

* Newton–Raphson iteration
* Bisection
* Brent’s method

Higher implied volatility widens the risk-neutral distribution of possible future prices. This increases the probability and expected size of extreme outcomes.

Because an option holder has limited downside but potentially large upside, greater uncertainty generally makes both calls and puts more valuable, all else being equal.

Therefore:

[
\frac{\partial V}{\partial \sigma}>0
]

for standard long European calls and puts.

---

## What the Model Is Used For

### Pricing and Quoting

The model provides a common framework for converting between:

* Option prices
* Implied volatilities
* Greeks
* Hedge ratios

In practice, traders often quote options in terms of implied volatility rather than directly in currency units.

### Hedging

The Black–Scholes framework provides estimates of delta, gamma, theta, vega, and rho. These measures help traders monitor and hedge different sources of risk.

### Relative-Value Analysis

Traders can compare implied volatility across:

* Strike prices
* Expiration dates
* Related assets
* Historical periods

This helps identify where options appear relatively expensive or cheap within the market’s own pricing structure.

---

## The Model Is Not a Prediction

The Black–Scholes model is not primarily a directional forecasting model.

It does not predict whether the underlying asset will rise or fall. Instead, it converts a set of assumptions and current market inputs into a no-arbitrage option value.

Implied volatility should therefore be understood as the volatility that makes the model price equal to the observed market price.

It reflects the market price of uncertainty under the model, rather than serving as a guaranteed forecast of future realized volatility.

Market option prices may also contain:

* Risk premia
* Supply-and-demand effects
* Hedging pressure
* Liquidity effects
* Event risk
* Tail-risk compensation

---

## Volatility Smile and Skew

Under the standard Black–Scholes model, all options on the same underlying with the same expiration should have the same implied volatility:

[
\sigma_{\text{imp}}(K,T)=\text{constant}
]

In real markets, implied volatility usually varies with strike:

[
\sigma_{\text{imp}}=\sigma_{\text{imp}}(K)
]

Plotting implied volatility against strike creates a **volatility smile** or **volatility skew**.

### Volatility Smile

A volatility smile occurs when both low-strike and high-strike options have higher implied volatility than at-the-money options, creating a roughly U-shaped curve.

This pattern is common in some foreign-exchange and commodity markets.

### Volatility Skew

A volatility skew occurs when implied volatility is systematically higher on one side of the strike distribution.

For equity indices, lower-strike puts often trade at higher implied volatilities than at-the-money or high-strike options. This is often associated with:

* Demand for downside protection
* Fear of market crashes
* Negative price jumps
* Leverage effects
* Tail-risk premia

---

## Short-Dated Volatility

Short-dated volatility curves can be strongly affected by specific events, including:

* Earnings announcements
* Economic data releases
* Central-bank decisions
* Elections
* Regulatory decisions
* Product launches
* Court rulings

During a calm period, the short-dated volatility curve may appear relatively flat.

During an event-driven period, it may become much steeper or more curved because the market assigns greater probability to discontinuous or unusually large moves.

For example, a one-day move of (10%) may be extremely unlikely under a standard continuous normal-return assumption. If traders believe such a jump is plausible, out-of-the-money options may trade at implied volatilities far above the at-the-money level.

The additional option price above what a simple constant-volatility model might suggest may reflect:

* Jump risk
* Event uncertainty
* Supply and demand
* Volatility risk premium
* Tail-risk premium

It is more precise to say that these options trade at a higher implied volatility than to say they are necessarily mispriced. The market may be compensating sellers for risks that the standard Black–Scholes model does not capture.

---

## Long-Dated Volatility

Long-dated volatility curves are often smoother than very short-dated curves because the effect of a single event is spread across a longer time horizon.

Several forces may contribute to this:

### Diversification Across Time

A long-dated option spans many individual price movements and market events. The impact of any one event may therefore represent a smaller proportion of the option’s total variance.

However, the Central Limit Theorem does not guarantee that long-horizon asset returns will follow the Black–Scholes distribution. Financial returns can remain skewed, heavy-tailed, correlated, and affected by changing volatility regimes.

### Volatility Mean Reversion

Volatility is often treated as mean-reverting. Periods of unusually high or low volatility may gradually move back toward a longer-term average.

As a result, a short-lived volatility shock may have a large effect on near-term options but a smaller effect on long-dated implied volatility.

### Long-Term Uncertainty

Long-dated options also include uncertainty about:

* Future economic regimes
* Interest rates
* Dividends
* Structural market changes
* Long-term earnings growth
* Future volatility regimes

Consequently, long-dated volatility is not always lower or flatter. Its shape depends on current market conditions and the risks relevant to the asset.

---

## Volatility Term Structure

Implied volatility also varies across expiration dates:

[
\sigma_{\text{imp}}=\sigma_{\text{imp}}(T)
]

The relationship between implied volatility and maturity is called the **volatility term structure**.

An upward-sloping term structure means longer-dated implied volatility is higher than shorter-dated volatility.

A downward-sloping term structure means shorter-dated implied volatility is higher, often because of:

* Immediate event risk
* Market stress
* Expected near-term turbulence

The term structure may contain peaks or kinks around known events, such as an earnings announcement or election.

---

## Volatility Surface

The volatility surface extends the smile or skew by incorporating both strike and expiration:

[
\boxed{
\sigma_{\text{imp}}
===================

\sigma_{\text{imp}}(K,T)
}
]

It displays implied volatility across two main dimensions:

* **Strike:** How implied volatility changes with the size and direction of the possible price move
* **Maturity:** How implied volatility changes over time

The standard Black–Scholes model compresses the future into a single constant volatility input. The volatility surface shows that the market does not actually assign the same volatility to every strike and maturity.

A volatility surface can reveal:

* Downside crash concerns
* Demand for upside exposure
* Event risk
* Differences between short-term and long-term uncertainty
* Market expectations of changing volatility
* Supply-and-demand imbalances
* Tail-risk pricing

However, the surface does not provide a complete or unique forecast of how the underlying price will evolve. It is a representation of current option prices translated into Black–Scholes implied volatilities.

---

## Main Limitations

The Black–Scholes model is foundational, but its assumptions are restrictive.

Real markets exhibit:

* Changing volatility
* Price jumps
* Fat-tailed return distributions
* Volatility skew
* Transaction costs
* Discrete hedging
* Liquidity constraints
* Stochastic interest rates
* Stochastic dividends
* Early exercise
* Funding and collateral effects

More advanced models attempt to address these limitations, including:

* Local-volatility models
* Stochastic-volatility models
* Jump-diffusion models
* Stochastic local-volatility models
* Numerical trees and finite-difference methods
* Monte Carlo simulation

Despite its limitations, Black–Scholes remains one of the most important frameworks in derivatives because it provides a common language for pricing, hedging, implied volatility, and risk.


## What I Built 

## Core assumptionss
- lognormal stock returns 
- constant volatility
- constant interest rate
- constant dividend yiels
- frictionless trading 
- condinuous hedging 
- European exercise only
TODO: What any of this means and why it is important

## Why the model works
Under these assumptions, the price solves the no-arbitrage replication problem 
TODO: What this means

## Why it is not fully realistic
- Volatility is not constant in real markets
- returns hace jumps and fat tails
- trading is discrete and not continuous
- bid-ask spead and impact exist
- American exercise and early exercise are ignores
- smils and skew are not captured

## What the model is good for
- clean baseline
- teaching the pricing logic
- sanity checking option data
- generating implied volatility 

## What breaks in practice
- Hedging error
- Volatility smile
- Jump risk 
- Transaction costs 
- Model misspecification 

## Tests I ran 



