import random
import scipy.stats as stats

def evaluate_dice_prng(num_rolls, seed, alpha):
    """
    Evaluates if Python's random package PRNG models a 6-sided dice roll
    correctly. Eval metric is Chi-squared.
    
    Parameters:
    - num_rolls (int): Number of times to 'roll' the dice.
    - seed (int): PRNG seed (for reproducibility).
    - alpha (float): Alpha value to compare p-value against.
    """

    random.seed(seed)

    # Roll the dice num_rolls times.
    rolls = [random.randint(1, 6) for _ in range(num_rolls)]
    
    # Observed frequencies for each face 1..6.
    observed_frequencies = [rolls.count(face) for face in range(1, 7)]
    
    # Expected frequencies for each face 1..6.
    expected_value = num_rolls / 6
    expected_frequencies = [expected_value] * 6
    
    # Chi-Squared Goodness-of-Fit.
    chisquare, p_val = stats.chisquare(f_obs=observed_frequencies, f_exp=expected_frequencies)
    
    # Results
    print("--- Chi-Squared Goodness-of-Fit Test ---")
    print(f"Total Rolls: {num_rolls}")
    print(f"Expected Frequency per Face: {expected_value}")
    print("-" * 40)
    for face, obs in enumerate(observed_frequencies, 1):
        print(f"Face {face}: Observed = {obs}, Expected = {expected_value}")
    print("-" * 40)
    print(f"Chi-square: {chisquare:.4f}")
    print(f"alpha: {alpha:.4f}")
    print(f"p-value: {p_val:.4f}")
    if p_val < alpha:
        print(f"\nResult: REJECT null hypothesis that random PRNG is a good modeler of 6-sided dice. The PRNG shows statistically significant bias.")
    else:
        print(f"\nResult: FAIL TO REJECT (or ACCEPT) null hypothesis that random PRNG is a good modeler of 6-sided dice. The PRNG acts like a fair 6-sided dice.")

# Run the evaluation
if __name__ == "__main__":
    evaluate_dice_prng(num_rolls=600000, seed=708, alpha=.05)

