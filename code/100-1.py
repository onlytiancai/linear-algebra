def bayes_theorem(p_d, p_t_given_d, p_t_given_not_d):
    """
    Calculate P(D|T+) using Bayes' Theorem.
    
    Parameters:
    p_d: P(D), probability of having the disease
    p_t_given_d: P(T+|D), probability of testing positive given disease
    p_t_given_not_d: P(T+|D'), probability of testing positive given no disease
    
    Returns:
    P(D|T+), probability of having the disease given a positive test
    """
    p_not_d = 1 - p_d
    p_t = p_t_given_d * p_d + p_t_given_not_d * p_not_d
    p_d_given_t = (p_t_given_d * p_d) / p_t
    return p_d_given_t

# Example usage
p_d = 0.01  # 1% of population has the disease
p_t_given_d = 0.99  # Test is 99% sensitive
p_t_given_not_d = 0.02  # Test has 2% false positive rate
result = bayes_theorem(p_d, p_t_given_d, p_t_given_not_d) 
print(f"P(D|T+) = {result:.4f}")  # Output: P(D|T+) = 0.3333 