# Black- Scholes 

## What is the Black-Scholes
Allows us to back out the implied volatility, assuming the asstes have GBM, allow us to compare the pricing apples to apples
If an implied vol is lower ten less turbulence is expected and thereore the contract can be seen as "more expensive"
Implied volatility is only good for that specific moment
It is not predictability it is the current snapshot, 

In the Black-Scholes framework Delta is the probability the contract expires ITM 

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