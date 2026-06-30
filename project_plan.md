# Project Plan: Feasible Volatility Surface Research Lab

## From Stochastic Pricing to Cross-Sectional Alpha

---

## 1. Project Purpose

This project is a feasible, standalone version of the broader **Volatility Surface Research Lab**.

The goal is to build a serious but attainable research platform that connects:

```text
Mathematical finance:
option pricing, stochastic simulation, Greeks, implied volatility, hedging error

Systematic equities:
equity signals, option-derived signals, volatility forecasting, cross-sectional return prediction, portfolio construction
```

The project should be impressive on its own, even without the extraordinary extensions such as SABR calibration, Breeden-Litzenberger density extraction, or Markov volatility regimes.

The central research question is:

```text
Can option-implied features derived from first-principles pricing tools improve volatility forecasting, equity selection, and portfolio risk control beyond traditional equity signals and vendor-provided option fields?
```

---

## 2. Guiding Principle

This project should be built in two modes.

### Mode 1: Training Wheels

At the start, every module should be tiny, explicit, and tested on synthetic data.

You should use:

```text
small data
simple functions
clear notebooks
hand-calculated examples
unit tests
plain-English explanations
```

The goal is to understand what every part is doing.

---

### Mode 2: Research Mode

As the project matures, you gradually move toward:

```text
larger datasets
modular code
reusable pipelines
real OptionMetrics data
real CRSP returns
model comparisons
robustness tests
research reporting
```

The goal is to stop following instructions mechanically and start making defensible research decisions.

---

## 3. Final Feasible Project Outcome

By the end of the feasible version, you should have:

```text
1. A mathematical finance library with Black-Scholes, binomial pricing, Monte Carlo pricing, Greeks, GBM simulation, and jump-diffusion simulation.
2. A delta-hedging simulator that shows hedging error under wrong volatility, jumps, discrete rebalancing, and transaction costs.
3. An implied-volatility solver built from scratch.
4. A small OptionMetrics + CRSP research dataset.
5. A validation study comparing your implied volatility estimates against vendor implied volatility.
6. A simple volatility smile/surface construction module.
7. A feature table containing equity features, vendor option features, and self-derived option features.
8. A volatility forecasting test.
9. An equity-only vs equity+options model comparison.
10. A basic portfolio backtest with costs and attribution.
11. A final research report explaining what worked, what failed, and what should be extended.
```

This is enough to stand alone.

---

## 4. What Is In Scope

The feasible project includes:

```text
Black-Scholes pricing
binomial tree pricing
Monte Carlo pricing
Greeks
GBM simulation
jump-diffusion simulation
delta-hedging error simulation
implied-volatility solver
OptionMetrics IV validation
simple volatility smile construction
simple volatility surface construction
CRSP returns
OptionMetrics option chains
basic equity signals
basic option signals
volatility forecasting
equity-only vs equity+options comparison
basic portfolio construction
transaction costs
attribution
robustness tests
final report
```

---

## 5. What Is Out of Scope for the Feasible Version

These are not required for the feasible standalone version:

```text
SABR calibration
Breeden-Litzenberger density extraction
risk-neutral density moments
Markov volatility-regime model
full factor risk model
capacity analysis
deep learning
exotic option pricing beyond simple demonstration
live trading
production-grade portfolio optimizer
```

They are extension modules.

---

## 6. Project Structure

Use this repo structure:

```text
vol-surface-alpha-lab/
│
├── README.md
├── research_charter.md
├── project_plan.md
├── theory_notes.md
├── limitations.md
├── requirements.txt
├── pyproject.toml
├── .gitignore
│
├── configs/
│   ├── pricing.yaml
│   ├── simulation.yaml
│   ├── data_sources.yaml
│   ├── option_filters.yaml
│   ├── signals.yaml
│   ├── models.yaml
│   └── backtest.yaml
│
├── data/
│   ├── raw/               # local only, gitignored
│   ├── interim/           # local only, gitignored
│   ├── processed/         # local only, gitignored
│   └── synthetic/         # safe to publish
│
├── src/
│   ├── stochastics/
│   │   ├── brownian.py
│   │   ├── gbm.py
│   │   └── jump_diffusion.py
│   │
│   ├── pricing/
│   │   ├── black_scholes.py
│   │   ├── binomial.py
│   │   ├── monte_carlo.py
│   │   └── greeks.py
│   │
│   ├── hedging/
│   │   ├── delta_hedge.py
│   │   └── hedging_costs.py
│   │
│   ├── volatility/
│   │   ├── implied_vol.py
│   │   ├── option_filters.py
│   │   ├── smile.py
│   │   └── surface.py
│   │
│   ├── data/
│   │   ├── synthetic.py
│   │   ├── crsp_loader.py
│   │   ├── optionmetrics_loader.py
│   │   ├── links.py
│   │   └── audit.py
│   │
│   ├── signals/
│   │   ├── equity.py
│   │   ├── options.py
│   │   └── normalization.py
│   │
│   ├── models/
│   │   ├── volatility_forecast.py
│   │   ├── cross_sectional.py
│   │   └── validation.py
│   │
│   ├── portfolio/
│   │   ├── backtest.py
│   │   ├── costs.py
│   │   └── attribution.py
│   │
│   └── utils/
│       ├── dates.py
│       ├── math.py
│       └── plotting.py
│
├── notebooks/
│   ├── 00_project_walkthrough.ipynb
│   ├── 01_pricing_basics.ipynb
│   ├── 02_stochastic_simulation.ipynb
│   ├── 03_greeks_and_hedging.ipynb
│   ├── 04_implied_vol_solver.ipynb
│   ├── 05_optionmetrics_iv_validation.ipynb
│   ├── 06_smile_and_surface.ipynb
│   ├── 07_feature_engineering.ipynb
│   ├── 08_volatility_forecasting.ipynb
│   ├── 09_equity_options_model_comparison.ipynb
│   ├── 10_backtest_attribution_robustness.ipynb
│   └── 11_final_report_figures.ipynb
│
├── tests/
│   ├── test_black_scholes.py
│   ├── test_binomial.py
│   ├── test_greeks.py
│   ├── test_gbm.py
│   ├── test_jump_diffusion.py
│   ├── test_delta_hedge.py
│   ├── test_implied_vol.py
│   ├── test_option_filters.py
│   ├── test_signals.py
│   └── test_backtest_timing.py
│
└── reports/
    ├── figures/
    ├── tables/
    ├── final_research_report.md
    └── interview_summary.md
```

---

# 7. Data Sources

## 7.1 Required Data

The feasible version requires only:

```text
CRSP
OptionMetrics IvyDB US
```

CRSP provides:

```text
daily prices
daily returns
volume
shares outstanding
market capitalization
share codes
exchange codes
delisting returns
```

OptionMetrics provides:

```text
option prices
strikes
expiries
calls and puts
implied volatility where available
Greeks where available
option volume
open interest
underlying security identifiers
interest rate / zero-curve inputs where available
dividend information where available
```

---

## 7.2 Optional Data

Add these later only after the CRSP + OptionMetrics pipeline works:

```text
Compustat
I/B/E/S
FTSE Russell
Eventus
Datastream
Factiva / Nexis
S&P Capital IQ Transcripts
```

For the feasible version, Compustat and I/B/E/S are useful but not required immediately.

---

## 7.3 Publication Rule

Do not publish raw licensed data.

The public repo may include:

```text
source code
synthetic data
schema examples
query templates
data dictionaries
generated plots
research report
```

The public repo should not include:

```text
raw CRSP data
raw OptionMetrics data
raw Compustat data
raw I/B/E/S data
full option-chain extracts
```

---

# 8. Build Philosophy

Every stage should have four outputs:

```text
1. Code
2. Tests
3. Notebook
4. Written explanation
```

That means every module should answer:

```text
What did I build?
Why does it matter?
How did I test it?
What can go wrong?
```

This will make the project much easier to defend in interviews.

---

# 9. Phase 0: Orientation and Setup

## Goal

Create the environment, repository, and mental map.

This phase is very guided. Do not try to be clever yet.

---

## 9.1 Tasks

Create the repo:

```text
vol-surface-alpha-lab/
```

Create the folders:

```text
src/
notebooks/
tests/
configs/
data/
reports/
docs/
```

Create the first files:

```text
README.md
research_charter.md
project_plan.md
theory_notes.md
limitations.md
requirements.txt
.gitignore
```

---

## 9.2 Minimum Dependencies

Start with:

```text
numpy
pandas
scipy
matplotlib
scikit-learn
pytest
pyarrow
jupyter
```

Optional later:

```text
cvxpy
statsmodels
polars
wrds
```

---

## 9.3 First README Structure

Your first README should contain:

```text
Project title
One-sentence summary
Research question
What is currently implemented
What is not implemented yet
Data licensing note
How to run tests
How to run notebooks
```

---

## 9.4 Done Criteria

This phase is done when:

```text
the repo exists
the folder structure exists
pytest runs successfully
the README explains the project clearly
the project plan is committed
```

---

## 9.5 Training Wheels

At this point, do not worry about real data.

Only focus on:

```text
clean structure
small examples
running tests
clear documentation
```

---

# 10. Phase 1: Synthetic Data and Toy Pipeline

## Goal

Build a fake miniature world where the whole project can run without WRDS data.

This is your sandbox.

---

## 10.1 Why This Matters

Real option data is messy. If the first version of your code only works on real data, debugging will be painful.

Synthetic data lets you ask:

```text
Does my code work when I control the answer?
```

---

## 10.2 Synthetic Stock Data

Create:

```text
data/synthetic/synthetic_prices.csv
```

Columns:

```text
date
ticker
price
return
volume
shares_outstanding
```

Use 5 fake tickers:

```text
AAA
BBB
CCC
DDD
EEE
```

Use 1 to 2 years of daily business dates.

---

## 10.3 Synthetic Option Chain

Create:

```text
data/synthetic/synthetic_option_chain.csv
```

Columns:

```text
date
ticker
expiry
strike
option_type
bid
ask
mid
volume
open_interest
underlying_price
risk_free_rate
dividend_yield
true_vol
```

Create options using your own Black-Scholes function once it exists.

At first, it is acceptable to create placeholder option prices manually.

---

## 10.4 Toy Pipeline

Build one notebook:

```text
notebooks/00_project_walkthrough.ipynb
```

It should:

```text
load synthetic prices
load synthetic option chain
compute simple returns
compute one simple option feature
merge into one table
print the final toy panel
```

Final toy panel:

```text
date | ticker | return | price | volume | atm_iv | forward_return_21d
```

---

## 10.5 Done Criteria

This phase is done when:

```text
you can create synthetic prices
you can create a synthetic option chain
you can merge them into one toy research panel
you understand the shape of the final dataset
```

---

## 10.6 Training Wheels

Use tiny data.

Print everything.

Use obvious numbers.

Do not optimize.

Do not vectorize too early.

Your goal is understanding, not speed.

---

# 11. Phase 2: Black-Scholes, Binomial Pricing, and Greeks

## Goal

Build the first mathematical finance core.

---

## 11.1 What to Build

Files:

```text
src/pricing/black_scholes.py
src/pricing/binomial.py
src/pricing/greeks.py
tests/test_black_scholes.py
tests/test_binomial.py
tests/test_greeks.py
notebooks/01_pricing_basics.ipynb
```

---

## 11.2 Black-Scholes Functions

Implement:

```text
black_scholes_call_price
black_scholes_put_price
```

Inputs:

```text
spot
strike
time_to_expiry
risk_free_rate
dividend_yield
volatility
```

Outputs:

```text
option price
```

---

## 11.3 Greeks

Implement:

```text
delta
gamma
vega
theta
rho
```

Start with analytic Greeks for European calls and puts.

Then implement finite-difference checks.

---

## 11.4 Binomial Tree

Implement:

```text
binomial_european_call
binomial_european_put
```

Optional:

```text
binomial_american_call
binomial_american_put
```

For the feasible version, American options are optional.

---

## 11.5 Tests

Required tests:

```text
call price is positive
put price is positive
put-call parity approximately holds
binomial European price converges to Black-Scholes as steps increase
finite-difference delta approximately matches analytic delta
finite-difference gamma approximately matches analytic gamma
```

---

## 11.6 Notebook

In `01_pricing_basics.ipynb`, show:

```text
call and put prices for simple examples
put-call parity check
binomial convergence plot
delta curve against spot
gamma curve against spot
vega curve against spot
```

---

## 11.7 Done Criteria

This phase is done when:

```text
the pricing functions work
the tests pass
you can explain put-call parity
you can explain why binomial converges to Black-Scholes
you can explain what delta, gamma, and vega mean
```

---

## 11.8 Training Wheels

Use one simple example repeatedly:

```text
spot = 100
strike = 100
time_to_expiry = 1
risk_free_rate = 0.05
dividend_yield = 0.00
volatility = 0.20
```

Do not move on until you understand the output.

---

# 12. Phase 3: Stochastic Simulation

## Goal

Build the simulation layer.

---

## 12.1 What to Build

Files:

```text
src/stochastics/brownian.py
src/stochastics/gbm.py
src/stochastics/jump_diffusion.py
tests/test_gbm.py
tests/test_jump_diffusion.py
notebooks/02_stochastic_simulation.ipynb
```

---

## 12.2 Brownian Motion

Implement:

```text
simulate_brownian_motion
```

Outputs:

```text
time grid
paths
```

Test:

```text
increments have mean close to 0
increments have variance close to dt
```

---

## 12.3 GBM

Implement:

```text
simulate_gbm
```

Model:

```text
dS_t = μS_tdt + σS_tdW_t
```

Test:

```text
log returns have approximately correct mean
log returns have approximately correct variance
prices remain positive
```

---

## 12.4 Jump Diffusion

Implement a simple Merton-style jump diffusion.

You do not need a perfect industrial model.

The purpose is to show what happens when jumps break Black-Scholes assumptions.

Test:

```text
jump diffusion produces fatter tails than GBM
jump diffusion creates larger hedging errors than GBM
```

---

## 12.5 Notebook

In `02_stochastic_simulation.ipynb`, show:

```text
Brownian paths
GBM paths
jump diffusion paths
histogram of returns
comparison of GBM vs jump diffusion tails
```

---

## 12.6 Done Criteria

This phase is done when:

```text
you can simulate GBM paths
you can simulate jump-diffusion paths
you can explain why jumps create tail risk
you can connect simulation to option pricing and hedging
```

---

## 12.7 Training Wheels

Keep the simulation small at first:

```text
10 paths
252 steps
1 year
```

Then increase:

```text
10,000 paths
252 steps
```

Only scale after you trust the small version.

---

# 13. Phase 4: Monte Carlo Pricing

## Goal

Use the simulation layer to price options.

---

## 13.1 What to Build

Files:

```text
src/pricing/monte_carlo.py
tests/test_monte_carlo.py
notebooks/01_pricing_basics.ipynb
```

---

## 13.2 European Option Monte Carlo

Implement:

```text
monte_carlo_european_call
monte_carlo_european_put
```

Steps:

```text
simulate terminal stock prices under risk-neutral GBM
compute payoff
discount average payoff
return price
```

---

## 13.3 Validation

Compare:

```text
Monte Carlo price vs Black-Scholes price
```

Show convergence as paths increase:

```text
1,000 paths
5,000 paths
10,000 paths
50,000 paths
```

---

## 13.4 Done Criteria

This phase is done when:

```text
Monte Carlo prices converge toward Black-Scholes
you can explain why Monte Carlo has sampling error
you can explain why risk-neutral drift is used for pricing
```

---

# 14. Phase 5: Delta Hedging Error

## Goal

Show that option pricing and option risk management are different.

---

## 14.1 What to Build

Files:

```text
src/hedging/delta_hedge.py
src/hedging/hedging_costs.py
tests/test_delta_hedge.py
notebooks/03_greeks_and_hedging.ipynb
```

---

## 14.2 Hedging Simulator

Simulate selling or buying one option and delta hedging over time.

At each hedge date:

```text
compute option delta
hold delta shares
rebalance
record stock trades
record cash account
record final P&L
```

---

## 14.3 Experiments

Run four experiments:

```text
1. GBM world, correct volatility, no costs
2. GBM world, wrong volatility, no costs
3. jump-diffusion world, Black-Scholes hedge
4. GBM world, correct volatility, transaction costs
```

Optional fifth experiment:

```text
different hedge frequencies: daily, weekly, monthly
```

---

## 14.4 Outputs

Produce:

```text
hedging P&L distribution
mean hedging error
standard deviation of hedging error
worst 5 percent hedging errors
effect of transaction costs
effect of jump risk
```

---

## 14.5 Done Criteria

This phase is done when:

```text
you can explain why discrete hedging creates error
you can explain why jumps hurt delta hedging
you can explain why wrong volatility matters
you can explain how transaction costs change the tradeoff
```

---

## 14.6 Training Wheels

Start with one path.

Print:

```text
date
stock price
option price
delta
stock position
cash
portfolio value
P&L
```

Only after one path works should you simulate thousands of paths.

---

# 15. Phase 6: Implied Volatility Solver on Synthetic Data

## Goal

Build your own implied-volatility solver before touching real option data.

---

## 15.1 What to Build

Files:

```text
src/volatility/implied_vol.py
tests/test_implied_vol.py
notebooks/04_implied_vol_solver.ipynb
```

---

## 15.2 Solver Methods

Implement:

```text
bisection_iv
newton_raphson_iv
hybrid_iv
```

The hybrid method should:

```text
try Newton-Raphson
fall back to bisection if Newton fails
return failure flags instead of crashing
```

---

## 15.3 Failure Flags

Use explicit statuses:

```text
success
failed_no_arbitrage_bounds
failed_no_convergence
failed_low_vega
failed_bad_input
```

---

## 15.4 Synthetic Validation

Generate synthetic option prices using Black-Scholes:

```text
true volatility = 20%
price = Black-Scholes price using 20%
solver should recover approximately 20%
```

Test across:

```text
different strikes
different maturities
different volatilities
calls and puts
```

---

## 15.5 Done Criteria

This phase is done when:

```text
the solver recovers known synthetic volatility
the solver handles bad inputs safely
the solver works for calls and puts
the solver returns clear diagnostic flags
```

---

## 15.6 Training Wheels

Do not start with real data.

Real data has bad quotes, stale prices, and weird edge cases.

The synthetic solver must work first.

---

# 16. Phase 7: Real Data Access and Small Extract

## Goal

Pull a tiny CRSP + OptionMetrics sample and validate the pipeline.

---

## 16.1 What to Build

Files:

```text
src/data/crsp_loader.py
src/data/optionmetrics_loader.py
src/data/links.py
src/data/audit.py
notebooks/05_optionmetrics_iv_validation.ipynb
```

---

## 16.2 Tiny First Extract

Start with:

```text
5 to 10 tickers
1 to 3 months of data
liquid large-cap names
only 30-day to 90-day options
```

Suggested ticker type:

```text
large liquid US names with active options
```

Do not start with 1,000 stocks.

---

## 16.3 CRSP Fields

Pull:

```text
date
permno
ticker or historical name field
price
return
volume
shares outstanding
exchange code
share code
```

---

## 16.4 OptionMetrics Fields

Pull:

```text
date
underlying identifier
option identifier
expiry
strike
call_put
bid
ask
mid
volume
open_interest
implied_volatility if available
delta if available
underlying_price if available
```

---

## 16.5 Linking

Create a small link table:

```text
date
ticker
permno
optionmetrics_underlying_id
```

For the first extract, manual verification is acceptable.

Later, automate it.

---

## 16.6 Data Audit

Check:

```text
missing prices
missing returns
missing option quotes
bid > ask
negative bid
zero ask
zero midpoint
duplicate rows
coverage by ticker
coverage by date
```

---

## 16.7 Done Criteria

This phase is done when:

```text
you can load a small CRSP sample
you can load a small OptionMetrics sample
you can link them by date and security
you can audit obvious data problems
you can save clean parquet files
```

---

## 16.8 Training Wheels

Keep the first real extract tiny.

The objective is not statistical power.

The objective is learning how the data behaves.

---

# 17. Phase 8: Option Chain Cleaning

## Goal

Turn raw option quotes into usable option chains.

---

## 17.1 What to Build

Files:

```text
src/volatility/option_filters.py
tests/test_option_filters.py
notebooks/05_optionmetrics_iv_validation.ipynb
```

---

## 17.2 Filters

Apply:

```text
drop missing bid or ask
drop bid < 0
drop ask < bid
drop midpoint <= 0
drop missing strike
drop missing expiry
drop time_to_expiry <= 0
drop extreme implied volatility
keep reasonable maturity window
keep reasonable moneyness window
require minimum open interest or volume for research features
```

Suggested first maturity range:

```text
21 to 120 calendar days
```

Suggested first moneyness range:

```text
0.80 <= K / S <= 1.20
```

---

## 17.3 Done Criteria

This phase is done when:

```text
raw option chain goes in
clean option chain comes out
you can report how many options were removed by each filter
you can explain why each filter exists
```

---

## 17.4 Training Wheels

Make a filter report like:

```text
rows before filtering
rows after filtering
removed due to missing quotes
removed due to bad bid/ask
removed due to maturity
removed due to moneyness
removed due to liquidity
```

This makes debugging much easier.

---

# 18. Phase 9: IV Validation on Real Data

## Goal

Compare your implied-volatility solver against OptionMetrics.

---

## 18.1 What to Build

Use:

```text
src/volatility/implied_vol.py
src/volatility/option_filters.py
notebooks/05_optionmetrics_iv_validation.ipynb
```

---

## 18.2 Process

For each clean option:

```text
compute midpoint price
compute time to expiry
compute self-derived IV
compare against vendor IV
record error
```

---

## 18.3 Analysis

Analyze IV error by:

```text
moneyness bucket
maturity bucket
option type
liquidity bucket
ticker
date
```

---

## 18.4 Outputs

Produce:

```text
mean absolute IV error
median absolute IV error
error histogram
scatter plot: my IV vs vendor IV
error by moneyness
error by maturity
failure rate
```

---

## 18.5 Done Criteria

This phase is done when:

```text
your synthetic IV solver works
your real-data IV solver runs without crashing
your IV estimates broadly agree with vendor IV on clean liquid options
you can explain where and why they differ
```

---

## 18.6 Training Wheels Start Coming Off

At this stage, start writing research notes.

For every surprising result, write:

```text
What did I expect?
What happened?
Why might this happen?
What test should I run next?
```

This is how you begin acting like a researcher.

---

# 19. Phase 10: Simple Volatility Smile and Surface

## Goal

Convert option chains into interpretable features.

---

## 19.1 What to Build

Files:

```text
src/volatility/smile.py
src/volatility/surface.py
notebooks/06_smile_and_surface.ipynb
```

---

## 19.2 Smile Construction

For each ticker-date-maturity bucket:

```text
compute moneyness = K / S
select clean options
sort by moneyness
plot implied volatility against moneyness
```

---

## 19.3 Surface Construction

For each ticker-date:

```text
bucket options into maturities
compute ATM IV for each maturity
compute skew for each maturity
compute term structure slope
compute simple surface quality score
```

---

## 19.4 Required Features

Create:

```text
atm_iv_30d
atm_iv_60d
atm_iv_91d
iv_term_slope_91d_30d
put_call_skew_30d
smile_slope_30d
smile_curvature_30d
option_liquidity_score
surface_coverage_score
```

---

## 19.5 Done Criteria

This phase is done when:

```text
you can plot a smile for a stock-date
you can build simple features for many stock-dates
you can flag low-quality surfaces
you can explain how each feature is calculated
```

---

## 19.6 Less Hand-Holding

From here onward, do not expect every feature to be perfect.

Your job is to make defensible choices and document them.

---

# 20. Phase 11: Equity and Option Feature Engineering

## Goal

Build the final modelling panel.

---

## 20.1 What to Build

Files:

```text
src/signals/equity.py
src/signals/options.py
src/signals/normalization.py
notebooks/07_feature_engineering.ipynb
```

---

## 20.2 Equity Features

Start with CRSP-only features:

```text
momentum_12_1
short_term_reversal_1m
realized_vol_21d
realized_vol_63d
size
dollar_volume
market_beta
```

Optional later:

```text
book_to_market
profitability
leverage
analyst_revisions
```

---

## 20.3 Option Features

Vendor features:

```text
vendor_atm_iv
vendor_skew
option_volume
open_interest
```

Self-derived features:

```text
my_atm_iv
my_skew
my_term_structure
my_vrp
option_liquidity_score
surface_coverage_score
```

---

## 20.4 Target Variables

Create:

```text
forward_return_21d
forward_return_63d
future_realized_vol_21d
future_realized_vol_63d
future_min_return_21d
future_min_return_63d
```

---

## 20.5 Master Panel

Final table:

```text
date
ticker
permno
forward_return_21d
future_realized_vol_21d
momentum_12_1
realized_vol_21d
size
dollar_volume
vendor_atm_iv
my_atm_iv
my_skew
my_term_structure
my_vrp
option_liquidity_score
surface_coverage_score
```

---

## 20.6 Signal Normalization

For cross-sectional features:

```text
winsorize
z-score
rank
track missingness
```

Optional:

```text
sector-neutralize
beta-neutralize
size-neutralize
```

---

## 20.7 Done Criteria

This phase is done when:

```text
you have a clean modelling panel
every feature is lagged correctly
every target is forward-looking
you can explain what each column means
you can confirm no obvious lookahead bias
```

---

## 20.8 Research Mode Begins

At this point, you should stop thinking like:

```text
What do I code next?
```

Start thinking like:

```text
What hypothesis am I testing?
What result would falsify it?
What would make this result untrustworthy?
```

---

# 21. Phase 12: Volatility Forecasting Study

## Goal

Test the most natural use of options data: forecasting future realized volatility.

---

## 21.1 Models

Compare:

```text
Model V0: historical realized volatility only
Model V1: vendor ATM IV
Model V2: self-derived ATM IV
Model V3: self-derived IV + skew + term structure + VRP
```

---

## 21.2 Target

Use:

```text
future_realized_vol_21d
future_realized_vol_63d
```

---

## 21.3 Evaluation Metrics

Use:

```text
RMSE
MAE
rank IC
bucket accuracy
top-volatility bucket hit rate
out-of-sample performance
```

---

## 21.4 Outputs

Produce:

```text
model comparison table
predicted vs realized volatility plot
rank IC over time
error by volatility regime
error by liquidity bucket
```

---

## 21.5 Done Criteria

This phase is done when:

```text
you know whether vendor IV beats historical realized volatility
you know whether your self-derived IV behaves similarly to vendor IV
you know whether skew, term structure, and VRP improve the model
you can explain why the result makes economic sense or why it does not
```

---

# 22. Phase 13: Equity Return Prediction Study

## Goal

Test whether option features improve cross-sectional equity prediction.

---

## 22.1 Models

Compare:

```text
Model E0: equity-only
Model E1: equity + vendor option features
Model E2: equity + self-derived option features
Model E3: equity + vendor + self-derived option features
```

---

## 22.2 Equity Features

Use:

```text
momentum_12_1
short_term_reversal_1m
realized_vol_21d
size
dollar_volume
```

Optional:

```text
value
quality
analyst revisions
```

---

## 22.3 Option Features

Use:

```text
vendor_atm_iv
my_atm_iv
my_skew
my_term_structure
my_vrp
option_liquidity_score
```

---

## 22.4 Target

Use:

```text
forward_return_21d
forward_return_63d
```

---

## 22.5 Evaluation Metrics

Use:

```text
rank IC
mean IC
IC t-stat
quintile return spread
decile return spread
long-short return
hit rate
turnover
```

---

## 22.6 Important Interpretation Rule

Do not expect option features to magically predict returns.

A strong result could be:

```text
Options features do not materially improve raw return prediction, but they help identify high-risk names where equity signals perform poorly.
```

That is still useful.

---

## 22.7 Done Criteria

This phase is done when:

```text
you have compared equity-only vs equity+options models
you know whether option features improve IC or quintile spreads
you know whether self-derived features add anything beyond vendor features
you can explain the economic interpretation
```

---

# 23. Phase 14: Tail-Risk Filter

## Goal

Use options data as a risk filter rather than pure alpha.

---

## 23.1 Motivation

Option features may be better at identifying risk than forecasting returns.

So test:

```text
Can option-implied risk features help avoid bad downside names?
```

---

## 23.2 Filter Rules

Example filters:

```text
exclude top 10 percent highest skew names
exclude top 10 percent highest IV names
exclude names with poor surface quality
reduce weight when VRP is extreme
```

---

## 23.3 Compare

```text
base equity strategy
base equity strategy + IV filter
base equity strategy + skew filter
base equity strategy + VRP filter
```

---

## 23.4 Evaluation

Use:

```text
average return
Sharpe ratio
max drawdown
worst month
CVaR 5%
turnover
return sacrificed
```

---

## 23.5 Done Criteria

This phase is done when:

```text
you know whether options features help reduce drawdowns
you know how much return is sacrificed
you can explain whether the filter is useful
```

---

# 24. Phase 15: Basic Backtest

## Goal

Turn signals into a basic implementable strategy.

---

## 24.1 Backtest Type

Use a monthly calendar-driven backtest.

Timing rule:

```text
signal date < rebalance date < return realization date
```

---

## 24.2 Strategy Variants

Compare:

```text
Strategy S0: equity-only long-short
Strategy S1: equity + vendor options
Strategy S2: equity + self-derived options
Strategy S3: equity-only with option risk filter
```

---

## 24.3 Portfolio Construction

Start simple:

```text
long top quintile
short bottom quintile
equal weight
monthly rebalance
```

Then improve:

```text
dollar-neutral long-short
max position cap
liquidity filter
turnover tracking
```

Optional:

```text
basic beta-neutralization
basic sector-neutralization
```

---

## 24.4 Transaction Costs

Apply simple costs first:

```text
0 bps
5 bps
10 bps
25 bps
```

Then optional impact model:

```text
cost_i = fixed_bps + impact_coeff * volatility_i * sqrt(order_size_i / ADV_i)
```

---

## 24.5 Outputs

Produce:

```text
gross return
net return
annualized return
annualized volatility
Sharpe ratio
max drawdown
turnover
cost drag
long book return
short book return
```

---

## 24.6 Done Criteria

This phase is done when:

```text
you can run the full backtest
you can compare gross vs net results
you can explain whether option features helped
you can explain whether costs killed the edge
```

---

# 25. Phase 16: Attribution and Robustness

## Goal

Make the project defensible.

---

## 25.1 Attribution

Break down:

```text
long book contribution
short book contribution
equity-only contribution
option-feature contribution
cost drag
turnover drag
volatility exposure
market beta exposure
```

---

## 25.2 Robustness Tests

Run:

```text
different liquidity thresholds
different option filters
different moneyness windows
different maturity buckets
different transaction costs
different rebalance frequencies
different train/test periods
large-cap only universe
```

---

## 25.3 Placebo Tests

Run:

```text
shuffle option features across stocks
lag option features incorrectly as a negative control
replace option features with random noise
compare against random portfolio with same turnover
```

---

## 25.4 Done Criteria

This phase is done when:

```text
you can identify what results survive
you can identify what fails
you can explain why the result is or is not credible
you are not relying on one lucky backtest
```

---

# 26. Phase 17: Final Report

## Goal

Package the project like serious research.

---

## 26.1 Final Report Structure

Write:

```text
reports/final_research_report.md
```

Structure:

```text
1. Abstract
2. Research question
3. Motivation
4. Data sources
5. Universe construction
6. Mathematical finance engine
7. Implied volatility validation
8. Volatility smile and surface construction
9. Feature engineering
10. Volatility forecasting results
11. Equity return prediction results
12. Backtest results
13. Transaction costs
14. Attribution
15. Robustness tests
16. Limitations
17. Conclusion
18. Extensions
```

---

## 26.2 Theory Notes

Write:

```text
theory_notes.md
```

Include:

```text
Black-Scholes
risk-neutral pricing
binomial tree intuition
Greeks
GBM
jump diffusion
delta hedging
implied volatility
volatility smile
volatility risk premium
```

---

## 26.3 Interview Summary

Write:

```text
reports/interview_summary.md
```

Include:

```text
30-second explanation
2-minute explanation
main technical challenges
what failed
what surprised me
what I would add next
questions I expect in interviews
```

---

## 26.4 Done Criteria

The project is done when:

```text
the code runs
the tests pass
the notebooks reproduce the key figures
the final report explains the research clearly
the limitations are honest
the extension path is obvious
```

---

# 27. Suggested Timeline

This is a realistic build plan if you are learning while building.

---

## Week 1: Setup and Synthetic Data

Goal:

```text
create the project skeleton and toy data
```

Deliverables:

```text
repo structure
README.md
research_charter.md
project_plan.md
synthetic prices
synthetic option chain
toy research panel
```

Training wheels:

```text
tiny data
lots of print statements
notebooks over abstraction
```

---

## Week 2: Black-Scholes, Binomial, Greeks

Goal:

```text
build the first pricing engine
```

Deliverables:

```text
black_scholes.py
binomial.py
greeks.py
pricing tests
pricing notebook
```

Training wheels:

```text
single example
manual checks
clear plots
```

---

## Week 3: Simulation and Monte Carlo

Goal:

```text
simulate stock paths and price options by Monte Carlo
```

Deliverables:

```text
brownian.py
gbm.py
jump_diffusion.py
monte_carlo.py
simulation notebook
Monte Carlo convergence plot
```

Training wheels:

```text
start with 10 paths
then 1,000
then 10,000
```

---

## Week 4: Delta Hedging

Goal:

```text
show hedging error under different worlds
```

Deliverables:

```text
delta_hedge.py
hedging_costs.py
hedging notebook
P&L distributions
```

Training wheels:

```text
debug one path first
then simulate many paths
```

---

## Week 5: Implied Volatility Solver

Goal:

```text
recover volatility from option prices
```

Deliverables:

```text
implied_vol.py
IV solver tests
synthetic IV validation notebook
```

Training wheels:

```text
synthetic Black-Scholes prices only
no real data yet
```

---

## Week 6: Small Real Data Extract

Goal:

```text
load a tiny CRSP + OptionMetrics sample
```

Deliverables:

```text
crsp_loader.py
optionmetrics_loader.py
links.py
audit.py
small clean dataset
data audit notebook
```

Training wheels:

```text
5 to 10 tickers
1 to 3 months
manual sanity checks allowed
```

---

## Week 7: Real-Data IV Validation

Goal:

```text
compare self-derived IV against vendor IV
```

Deliverables:

```text
option_filters.py
IV validation report
my IV vs vendor IV plots
error by moneyness and maturity
```

Training wheels reduced:

```text
start making research notes
document weird results
```

---

## Week 8: Smile and Surface Features

Goal:

```text
build simple option-surface features
```

Deliverables:

```text
smile.py
surface.py
surface diagnostics notebook
ATM IV, skew, term structure, VRP features
```

Less hand-holding:

```text
you now choose sensible filters and justify them
```

---

## Week 9: Feature Engineering Panel

Goal:

```text
build the final modelling panel
```

Deliverables:

```text
equity.py
options.py
normalization.py
master modelling panel
feature coverage report
```

Research mode:

```text
focus on data quality, leakage, and interpretation
```

---

## Week 10: Volatility Forecasting

Goal:

```text
test whether option features forecast realized volatility
```

Deliverables:

```text
volatility_forecast.py
vol forecasting notebook
model comparison table
forecast error plots
```

Research mode:

```text
compare hypotheses, not just metrics
```

---

## Week 11: Equity Return Prediction

Goal:

```text
test equity-only vs equity+options models
```

Deliverables:

```text
cross_sectional.py
IC analysis
quintile spread analysis
equity/options model comparison
```

Research mode:

```text
interpret whether options help alpha or risk filtering
```

---

## Week 12: Backtest, Costs, and Attribution

Goal:

```text
convert research signals into a portfolio comparison
```

Deliverables:

```text
backtest.py
costs.py
attribution.py
gross vs net returns
turnover and cost drag
basic attribution
```

Research mode:

```text
be skeptical of good-looking results
```

---

## Week 13: Robustness

Goal:

```text
attack your own results
```

Deliverables:

```text
validation.py
robustness tables
placebo tests
filter sensitivity tests
cost sensitivity tests
```

Independent mode:

```text
you decide which tests are necessary based on what the results show
```

---

## Week 14: Final Report

Goal:

```text
turn the project into a portfolio-ready research artifact
```

Deliverables:

```text
final_research_report.md
theory_notes.md
limitations.md
interview_summary.md
clean README
```

Independent mode:

```text
you now own the interpretation
```

---

# 28. Checkpoints

Use these checkpoints to prevent scope explosion.

---

## Checkpoint 1: End of Week 2

You should be able to say:

```text
I can price European options using Black-Scholes and binomial trees, and I can explain the Greeks.
```

Do not move to real data before this.

---

## Checkpoint 2: End of Week 5

You should be able to say:

```text
I can simulate paths, price options, hedge options, and recover implied volatility on synthetic data.
```

Do not move to OptionMetrics before this.

---

## Checkpoint 3: End of Week 7

You should be able to say:

```text
I can load real option data, clean it, compute implied volatility, and compare it against vendor IV.
```

Do not build alpha models before this.

---

## Checkpoint 4: End of Week 9

You should be able to say:

```text
I have a clean modelling panel with equity features, option features, and forward targets.
```

Do not backtest before this.

---

## Checkpoint 5: End of Week 12

You should be able to say:

```text
I have compared equity-only, vendor-option, and self-derived-option models with costs.
```

Do not write final conclusions before this.

---

## Checkpoint 6: End of Week 14

You should be able to say:

```text
I have a standalone project with code, tests, notebooks, results, limitations, and extension paths.
```

That is the minimum impressive finish line.

---

# 29. Extraordinary Extension Path

Once the feasible version is complete, add extensions in this order.

---

## Extension 1: SABR Calibration

Add:

```text
src/volatility/sabr.py
```

Use it to estimate:

```text
alpha
rho
nu
fit error
parameter stability
```

Then compare:

```text
simple skew features
vs
SABR rho / nu features
```

---

## Extension 2: Breeden-Litzenberger Density

Add:

```text
src/volatility/density.py
```

Estimate:

```text
risk-neutral skewness
risk-neutral kurtosis
left-tail probability
crash-risk proxy
```

Then test:

```text
Do density features improve drawdown filtering?
```

---

## Extension 3: Markov Volatility Regimes

Add:

```text
src/models/regime.py
```

States:

```text
calm
implied-risk rising
realized stress
normalization
```

Test:

```text
Do equity and option signals behave differently by regime?
```

---

## Extension 4: Full Factor Risk Model

Add:

```text
src/risk/factor_model.py
```

Decompose returns into:

```text
market
sector
size
value
momentum
volatility
residual
```

Test:

```text
Was the options model adding alpha or just changing factor exposure?
```

---

## Extension 5: Cost-Aware Optimizer

Add:

```text
src/portfolio/optimizer.py
```

Objective:

```text
maximize alpha - risk penalty - cost penalty - tail-risk penalty
```

This becomes the more institutional version.

---

# 30. What to Do When You Get Stuck

Use this debugging ladder.

---

## Step 1: Translate the problem into English

Example:

```text
I need to compute implied volatility.
```

Means:

```text
I have a market option price, and I need to find the volatility that makes Black-Scholes output that price.
```

---

## Step 2: Make a tiny example

Use:

```text
spot = 100
strike = 100
time = 1
rate = 0.05
vol = 0.20
```

---

## Step 3: Write the input/output contract

Example:

```text
input: option price, spot, strike, time, rate, dividend yield, option type
output: implied volatility and status flag
```

---

## Step 4: Write the dumb version

No vectorization.

No classes.

No clever abstractions.

Just make it work.

---

## Step 5: Test it

Ask:

```text
Does it work on the tiny example?
Does it fail gracefully?
Does it match a known result?
```

---

## Step 6: Generalize it

Only after the dumb version works.

---

## Step 7: Document the assumption

Every important choice should be documented.

Examples:

```text
why this maturity window?
why this moneyness range?
why this liquidity filter?
why this rebalance frequency?
why this cost assumption?
```

---

# 31. Final Definition of Done

The feasible version is complete when you have:

```text
a working repo
a clear README
a research charter
a project plan
pricing functions
simulation functions
Greeks
hedging simulator
IV solver
real-data IV validation
simple smile/surface features
equity and option feature panel
volatility forecasting results
equity-only vs equity+options comparison
basic backtest
transaction cost analysis
attribution
robustness tests
final report
interview summary
```

The project does not need to produce a profitable strategy.

It needs to produce a credible research process.

---

# 32. Final Positioning

At the end, you should be able to say:

```text
I built a feasible version of a volatility-surface research lab. It starts from first-principles option pricing and stochastic simulation, validates implied volatility against real OptionMetrics data, constructs simple volatility-surface features, and tests whether those features improve volatility forecasting, equity selection, and portfolio risk control using CRSP and OptionMetrics data.
```

That is the standalone version.

The extraordinary version is not a different project.

It is the next layer on top of this one.
