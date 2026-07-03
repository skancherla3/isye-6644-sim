import random
import numpy as np
from scipy import stats

def evaluate_prng(n, k, seed):
    """
    Evaluates Python's random package PRNG uniformity using a Chi-Squared test.
    
    Parameters:
    - n (int): Number of random samples to generate.
    - k (int): Number of intervals.
    - seed (int): PRNG seed (for reproducibility).
    """

    random.seed(seed) 
    samples = [random.random() for _ in range(n)]
    
    # Define intervals. Note that k+1 interval 'edges' are required for k intervals.
    intervals = np.linspace(0.0, 1.0, k + 1)

    # Observed frequencies.
    O, _ = np.histogram(samples, bins=intervals)
    
    # Expected frequencies for a UNIF distro.
    exp_freq = n / k
    E = np.full(k, exp_freq)
    
    # Chi-squared Goodness-of-Fit.
    diff = O - E
    sq_diff = diff ** 2
    chisquared = np.sum(sq_diff) / exp_freq

    # Degrees of freedom
    df = k - 1

    # z and p-val
    z = (chisquared - df) / np.sqrt(2 * df)
    pval = stats.norm.sf(z)

    print(f"--- PRNG Evaluation Results ---")
    print(f"Seed used:          {seed}")
    print(f"Sample Size (n):    {n}")
    print(f"Number of Bins (k): {k}")
    print(f"Expected per Bin:   {exp_freq}")
    print(f"Chi-square:         {chisquared:.4f}")
    print(f"Z-score:            {z:.4f}")
    print(f"P-value:            {pval:.4f}")
    print(f"-------------------------------")
    
    # alpha = 0.05 seems standard.
    alpha = 0.05
    if pval < alpha:
        print(f"Result: REJECT the null hypothesis (p < {alpha}).")
        print("The sample distribution significantly deviates from a uniform distribution.")
    else:
        print(f"Result: FAIL TO REJECT (or ACCEPT) the null hypothesis (p >= {alpha}).")
        print("The PRNG behaves consistently with a uniform distribution.")

# Run the evaluation
if __name__ == "__main__":
    evaluate_prng(n=10000, k=100, seed=708)

