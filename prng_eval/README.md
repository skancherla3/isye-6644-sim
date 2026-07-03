This is a tool to verify whether python's PRNG in random package
is a good modeler of a fair 6-sided dice. It uses Chi-square
goodness-of-fit metric to evaluate the PRNG.

# How to run the tool.

```console
$ python run.py
--- Chi-Squared Goodness-of-Fit Test ---
Total Rolls: 600000
Expected Frequency per Face: 100000.0
----------------------------------------
Face 1: Observed = 99764, Expected = 100000.0
Face 2: Observed = 99811, Expected = 100000.0
Face 3: Observed = 99991, Expected = 100000.0
Face 4: Observed = 100589, Expected = 100000.0
Face 5: Observed = 99730, Expected = 100000.0
Face 6: Observed = 100115, Expected = 100000.0
----------------------------------------
Chi-square: 5.2454
alpha: 0.0500
p-value: 0.3867

Result: FAIL TO REJECT (or ACCEPT) null hypothesis that random PRNG is a good modeler of 6-sided dice. The PRNG acts like a fair 6-sided dice.
```

NOTE: Try evaluating the PRNG by changing the seed, sample size and alpha value in the tool.

