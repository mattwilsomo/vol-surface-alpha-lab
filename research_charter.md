# Research Charter: Options-Informed Systematic Equity Research Platform

## 1. Core Hypothesis

This project tests whether traditional cross-sectional equity alpha factors — value, momentum, quality, short-term reversal, and analyst revisions — achieve stronger out-of-sample risk-adjusted performance, lower drawdowns, and improved tail-risk profiles when conditioned on forward-looking option-implied risk characteristics.

The central research question is:

> Do options-implied variables such as volatility risk premium, put-call skew, implied volatility level, and implied volatility term structure improve the robustness of systematic equity signals?

This project does not assume that options data will improve performance. The options-informed layer will be evaluated against clearly defined equity-only baselines and may be formally rejected if it fails out of sample.

---

## 2. Investment Universe and Boundaries

### Asset Class

US liquid common equities.

### Equity Universe

The base equity universe will consist of CRSP common stocks with share codes 10 and 11.

### Optionable Universe

The final tradable universe will be restricted to underlying securities with active and sufficiently liquid option chains available in OptionMetrics IvyDB US.

### Liquidity Screens

Securities will be excluded if they meet any of the following conditions:

- Price below `$5`.
- Rolling 21-day average daily dollar volume below the 20th percentile of the eligible universe.
- Missing or unreliable CRSP return data.
- Insufficient price history for signal construction.

### Option Liquidity Screens

Underlying securities will be excluded if their corresponding option chains fail liquidity or quality checks, including:

- Zero open interest in the relevant front expiries.
- Missing implied volatility.
- Invalid bid/ask quotes.
- Average bid-ask spread wider than a predefined threshold.
- Insufficient contracts near target maturity or moneyness/delta buckets.

### Rebalancing Frequency

Monthly.

Signals are formed using data available after the close of the final trading day of month `t`.

Portfolio trades are executed on the next trading day to avoid same-close lookahead bias.

---

## 3. Data Sources

The project will use institutional datasets available through WRDS and university subscriptions.

### Primary Datasets

#### CRSP

Daily and monthly stock prices, returns, volume, shares outstanding, delisting returns, and identifiers.

#### Compustat

Fundamental accounting variables for value, quality, profitability, leverage, and size-related features.

#### I/B/E/S

Analyst forecast data, consensus EPS estimates, forecast revisions, and recommendation-related variables where available.

#### OptionMetrics IvyDB US

Historical option prices, implied volatility, Greeks, volume, open interest, option identifiers, and underlying security links.

### Optional Datasets

#### FTSE Russell / Index Holdings

Benchmark or index membership analysis.

#### Eventus

Event-study validation using CRSP-linked event windows.

#### Capital IQ Transcripts / Factiva / Nexis

Possible later-stage event or text-based extensions. These are not part of the core project.

---

## 4. Point-in-Time and Lookahead Policy

All features must be constructed using only information that would have been observable before portfolio formation.

### Timing Rules

#### CRSP Price, Return, and Volume Data

Available after market close on the observation date.

#### OptionMetrics Data

Option-implied variables are constructed only from option quotes available at or before the signal formation date.

#### Compustat Fundamentals

Lagged by at least 3 to 6 months after fiscal period end to reduce publication and restatement lookahead bias.

#### I/B/E/S Forecasts

Only forecast snapshots available before the rebalance date may be used.

#### Portfolio Execution

Signals formed after month-end close are traded on the next trading day.

### Survivorship Policy

The historical universe must be formed using securities available at each point in time, not today’s surviving securities.

CRSP delisting returns will be included where available.

---

## 5. Data Splits and Regime Testing

To reduce lookahead bias, data snooping, and repeated tuning on the test set, the historical panel will be divided into distinct research periods.

### In-Sample Estimation / Training Window

Example:

- January 2005 to December 2016.

Purpose:

- Signal engineering.
- Data cleaning rules.
- Baseline model fitting.
- Neutralisation calibration.
- Initial feature selection.
- Cost model calibration.

### Out-of-Sample Test Window

Example:

- January 2017 to December 2025.

Purpose:

- Isolated walk-forward testing.
- Final model comparison.
- No parameter tuning using this period.
- Evaluation across multiple market regimes.

### Regime Periods to Examine

The out-of-sample period should include distinct stress regimes where possible:

- 2018 volatility spike.
- 2020 COVID crash.
- 2021 speculative / low-rate environment.
- 2022 rate-hike and inflation shock.
- 2023 to 2025 post-hike / AI-led market regime.

If the final dataset begins earlier than 2005, additional crisis periods such as 2008 may be used for regime testing.

---

## 6. Signal Architecture

The project separates the physical equity world from the risk-neutral options-implied world.

---

## A. Equity Baseline Features: Physical-World Signals

These features are built from historical realized returns, accounting data, and analyst expectations.

### Momentum

Source: CRSP.

Definition:

- 12-minus-1 month cumulative log return.
- Cumulative return from month `t-12` to month `t-1`, skipping the most recent month.

Purpose:

- Captures medium-term trend continuation while reducing short-term reversal contamination.

### Short-Term Reversal

Source: CRSP.

Definition:

- Negative previous 5-day or 21-day log return.

Purpose:

- Captures short-horizon reversal effects.

### Value

Source: Compustat.

Possible definitions:

- Book-to-market.
- Earnings yield.
- Sales-to-price.
- Cash-flow-to-price.

All fundamental variables must be lagged by at least 3 to 6 months.

### Quality

Source: Compustat.

Possible definitions:

- Return on equity.
- Gross profitability.
- Earnings stability.
- Low leverage.
- Accruals quality.

Initial proxy:

- ROE residualised against leverage or combined with leverage controls.

### Analyst Revisions

Source: I/B/E/S.

Possible definitions:

- 30-day change in consensus forward EPS estimate.
- Change in number of upward vs downward revisions.
- Forecast dispersion.
- Recommendation changes.

Purpose:

- Captures changing analyst expectations and information diffusion.

---

## B. Options Conditioning Features: Risk-Neutral / Forward-Looking Signals

These features are built from option-market prices and implied quantities.

### At-the-Money Implied Volatility

Source: OptionMetrics IvyDB US.

Definitions:

- 30-day ATM implied volatility.
- 91-day ATM implied volatility.

Purpose:

- Measures the options market’s forward-looking uncertainty estimate.

### Realized Volatility

Source: CRSP.

Definition:

- Rolling 21-day or 63-day historical realized volatility.

Purpose:

- Measures the stock’s recent physical-world volatility.

### Volatility Risk Premium

Source: OptionMetrics and CRSP.

Initial definition:

- `VRP = 30-day ATM implied volatility - rolling 21-day realized volatility`

Alternative variance-based definition:

- `VRP = implied variance - realized variance`

Purpose:

- Captures the gap between option-implied risk and recently realized risk.

### Put-Call Skew

Source: OptionMetrics.

Initial definition:

- `IV of 25-delta put - IV of 25-delta call`

Purpose:

- Captures market pricing of downside protection relative to upside exposure.

### Implied Volatility Term Structure

Source: OptionMetrics.

Definition:

- `91-day ATM implied volatility - 30-day ATM implied volatility`

Purpose:

- Captures whether near-term uncertainty is elevated or suppressed relative to longer-term uncertainty.

### Option Liquidity and Activity

Source: OptionMetrics.

Possible features:

- Option volume.
- Open interest.
- Put-call volume ratio.
- Option bid-ask spread.
- Option volume relative to stock volume.

Purpose:

- Distinguishes usable option-implied information from noisy or illiquid option quotes.

---

## 7. Target Variable

The primary prediction target is:

> 21-trading-day forward excess return relative to the cap-weighted eligible-universe benchmark.

Formula:

```text
target_i,t = R_i,t→t+21 - R_benchmark,t→t+21
```

Returns should include delisting returns where available.

### Alternative Targets for Robustness

- Next-month raw return.
- Next-month sector-relative return.
- Next-month residual return after market, sector, and style factor adjustment.
- Next-month downside-adjusted return.
- Future realized volatility.
- Future drawdown indicator.

---

## 8. Baseline Models

The project will compare multiple models to avoid evaluating the options-informed model against a weak strawman.

### Model 0: Naive Benchmark

Definition:

- Equal-weight or cap-weight eligible-universe benchmark.

Purpose:

- Measures whether active modelling adds anything beyond passive exposure.

### Model 1: Equity-Only Model

Uses only physical-world equity features:

- Momentum.
- Reversal.
- Value.
- Quality.
- Analyst revisions.
- Size and liquidity controls.

Purpose:

- Establishes the baseline systematic equity alpha model.

### Model 2: Options-Only Model

Uses only option-derived features:

- Implied volatility.
- Volatility risk premium.
- Put-call skew.
- Term structure.
- Option liquidity and activity.

Purpose:

- Tests whether options-implied variables have standalone cross-sectional predictive content.

### Model 3: Options-Informed Equity Model

Uses both equity and options features.

Purpose:

- Tests whether options-implied information improves or conditions traditional equity alpha signals.

Potential interaction terms:

- Momentum × implied volatility.
- Momentum × skew.
- Value × skew.
- Quality × volatility risk premium.
- Revisions × implied volatility term structure.


## 9. Modelling Methodology

The first modelling layer will remain interpretable before any complex machine learning is added.

### Initial Models

- Equal-weight composite score.
- Linear cross-sectional regression.
- Ridge regression.
- Lasso / elastic net.

### Optional Later Models

- Gradient boosted trees.
- Random forests.
- Classification model for top-quintile membership.

Nonlinear models may only be added after the linear baseline is fully implemented, documented, and evaluated.

### Validation Approach

- Rolling-window validation.
- Expanding-window validation.
- Walk-forward out-of-sample testing.
- No random train/test splits.
- No tuning on the final out-of-sample period.

### Evaluation Metrics

- Information coefficient.
- Rank information coefficient.
- IC t-statistic.
- Quintile spread returns.
- Out-of-sample R².
- Hit rate.
- Sharpe ratio.
- Information ratio.
- Max drawdown.
- Sortino ratio.
- 5% CVaR.
- Turnover-adjusted return.

---

## 10. Portfolio Construction Rules

The project will evaluate signals both before and after portfolio construction.

### Diagnostic Portfolios

- Quintile portfolios.
- Top-minus-bottom long-short portfolios.
- Equal-weight top-N / bottom-N portfolios.

Purpose:

- Understand signal behaviour before optimization.

### Implementable Portfolios

The final portfolio construction layer will convert expected returns into weights under realistic constraints.

Possible optimization objective:

- Maximize expected alpha.
- Penalize predicted portfolio risk.
- Penalize transaction costs.
- Penalize excessive exposure to option-implied risk.

Conceptual objective:

- Maximize: alphaᵀw - λwᵀΣw - cost(w - w_prev) - γ(option_risk_penalty)

### Portfolio Types to Compare

- Equity-only long-short portfolio.
- Options-informed long-short portfolio.
- Long-only constrained version, if time allows.

---

## 11. Risk Controls

The portfolio must be evaluated not just by return, but by the risks taken to earn that return.

### Required Controls

- Market beta exposure bounded close to zero for long-short portfolios.
- Sector exposure bounded relative to benchmark.
- Single-name maximum weight.
- Gross exposure limit.
- Net exposure limit.
- Monthly turnover limit.
- Minimum equity liquidity threshold.
- Minimum option liquidity threshold.

### Risk Model

A basic factor risk model will decompose stock returns into:

- Market factor.
- Sector or industry factors.
- Size factor.
- Value factor.
- Momentum factor.
- Volatility factor.
- Idiosyncratic residual.

The risk model will be used to measure:

- Portfolio beta.
- Sector exposures.
- Style exposures.
- Predicted volatility.
- Specific risk.
- Factor contribution to risk.

---

## 12. Realism and Transaction Cost Constraints

### Base Transaction Cost Model

Initial assumption:

- 5 bps one-way equity transaction cost.

This accounts for simplified execution slippage, bid-ask spread, and commissions.

### Robustness Cost Scenarios

The strategy must be tested under:

- 0 bps.
- 5 bps.
- 10 bps.
- 25 bps.

Later versions may use a liquidity-scaled cost model based on:

- Bid-ask spread proxy.
- Average daily dollar volume.
- Trade size as percentage of ADV.
- Realized volatility.
- Turnover.

### Turnover Policy

The strategy must report:

- Monthly turnover.
- Annualized turnover.
- Transaction cost drag.
- Gross return.
- Net return.
- Percentage of gross alpha absorbed by costs.

If transaction costs fully absorb the gross outperformance, the strategy fails.

---

## 13. Option Data Quality Rules

Option observations will be excluded if any of the following hold:

- Bid is less than or equal to zero.
- Ask is less than or equal to bid.
- Implied volatility is missing.
- Delta is missing where delta-based buckets are required.
- Open interest equals zero in target contracts.
- Bid-ask spread exceeds the chosen threshold.
- Time to maturity is outside the target interpolation range.
- Moneyness or delta is too far from the target bucket.
- Implied volatility is extreme or clearly erroneous.

Where practical, the project will include sanity checks for:

- Put-call parity violations.
- Implausible implied volatility jumps.
- Missing option chains.
- Stale quotes.
- Coverage changes over time.

---

## 14. Attribution Plan

Performance will be decomposed to identify whether the options-informed layer adds genuine value or merely changes risk exposure.

### Attribution Dimensions

- Equity-signal contribution.
- Options-signal contribution.
- Market beta contribution.
- Sector contribution.
- Style factor contribution.
- Volatility exposure contribution.
- Long book contribution.
- Short book contribution.
- Transaction cost drag.
- Turnover drag.
- Drawdown contribution.

### Specific Questions

- Did options information improve returns?
- Did options information reduce drawdowns?
- Did options information reduce exposure to crash-prone names?
- Did options information simply proxy for volatility, size, or liquidity?
- Did the improvement survive after factor neutralisation?
- Was performance concentrated in a small number of names, sectors, or regimes?

---

## 15. Robustness Tests

The strategy must survive reasonable perturbations.

### Universe Robustness

- All eligible optionable stocks.
- Large-cap only.
- High-equity-liquidity only.
- High-option-liquidity only.
- Sector-neutral universe.
- Excluding microcaps.

### Time Robustness

- Full sample.
- In-sample.
- Out-of-sample.
- High-volatility regimes.
- Low-volatility regimes.
- Crisis periods.
- Post-crisis periods.

### Signal Robustness

- Alternative momentum windows.
- Alternative realized volatility windows.
- Alternative skew definitions.
- Alternative VRP definitions.
- Raw vs sector-neutral signals.
- Raw vs ranked signals.

### Cost Robustness

- 0 bps.
- 5 bps.
- 10 bps.
- 25 bps.
- Liquidity-scaled costs, if implemented.

### Placebo Tests

- Shuffled options signals.
- Lagged wrong-way options signals.
- Random portfolios with same turnover.
- Equity-only model with random option filter.

---

## 16. Hard Rejection Criteria

The options-informed conditioning layer will be formally rejected if any of the following occur out of sample.

### Rejection Rule 1: No Meaningful Improvement

The options-informed model fails to improve the equity-only model on at least two of the following metrics:

- Sharpe ratio.
- Information ratio.
- Max drawdown.
- Sortino ratio.
- 5% CVaR.
- Turnover-adjusted net return.
- Crisis-period drawdown.

A Sharpe improvement smaller than approximately 0.15 will not be treated as economically meaningful unless accompanied by clear drawdown or tail-risk improvement.

### Rejection Rule 2: Alpha Disappears After Risk Adjustment

The apparent out-of-sample alpha disappears after controlling for:

- Market beta.
- Size.
- Value.
- Momentum.
- Volatility.
- Sector or industry exposure.
- Liquidity.

### Rejection Rule 3: Costs Absorb the Edge

The strategy’s turnover increases enough that transaction costs absorb the gross outperformance.

### Rejection Rule 4: Illiquidity Explains the Result

The performance gains are concentrated in illiquid microcap stocks or names with unreliable or illiquid option chains.

### Rejection Rule 5: Fragile Regime Dependence

The strategy only works in one narrow market regime and fails across reasonable subperiods.

### Rejection Rule 6: Data-Mining Concern

The result only appears after repeated parameter tuning, signal modification, or test-period experimentation.

---

## 17. Research Log and Multiple-Testing Policy

All experiments must be logged.

Each experiment entry should record:

- Date run.
- Git commit hash.
- Data version.
- Model configuration.
- Signal definitions.
- Train/test period.
- Transaction cost assumptions.
- Performance metrics.
- Notes on interpretation.
- Whether the result was accepted or rejected.

The final out-of-sample period cannot be repeatedly reused for tuning.

Failed experiments will be documented rather than silently discarded.

---

## 18. Known Limitations

This project will explicitly acknowledge the following limitations:

- OptionMetrics coverage restricts the universe to optionable stocks, likely biasing the sample toward larger and more liquid firms.
- Some Compustat and I/B/E/S fields require careful timestamp validation to avoid lookahead bias.
- The first transaction cost model is simplified and may understate true implementation costs.
- The project uses options data to inform equity selection and risk control; the base project does not directly trade options.
- Option-implied variables may proxy for known risks such as volatility, liquidity, size, or event uncertainty rather than unique alpha.
- Backtested performance may not translate to live trading due to data latency, execution costs, crowding, and regime change.

---

## 19. Final Deliverables

The final project should produce:

- Clean research dataset schema.
- Data audit report.
- Pricing/math finance module.
- Equity signal module.
- Options signal module.
- Model comparison notebook.
- Portfolio backtest notebook.
- Risk and attribution report.
- Robustness test report.
- Final research memo.
- GitHub repository with reproducible code and no proprietary raw data.

Raw WRDS, CRSP, Compustat, I/B/E/S, and OptionMetrics data must not be uploaded publicly.

The public repository may include:

- Source code.
- Synthetic sample data.
- Schemas.
- Configuration files.
- Unit tests.
- Documentation.
- Figures generated from permitted or synthetic outputs.

---

## 20. Final Research Decision

The final report must conclude one of the following.

### Accept Conditionally

The options-informed layer improves the equity-only model after costs, risk adjustment, and robustness testing.

### Reject

The options-informed layer fails to improve the equity-only model or only appears to work due to overfitting, illiquidity, or hidden risk exposure.

### Continue Research

The options layer does not clearly improve returns but shows evidence of useful drawdown control, volatility filtering, or risk management value.

The goal is not to force a profitable strategy. The goal is to determine honestly whether options-implied information adds value to systematic equity research.