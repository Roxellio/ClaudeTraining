def greeting():
  print("Hi there")


def calculate_pi(digits=5):
    """
    Calculate pi to the specified number of decimal digits using the Leibniz formula.
    For better accuracy with fewer iterations, we use the Machin formula:
    pi/4 = 4*arctan(1/5) - arctan(1/239)
    
    Args:
        digits: Number of decimal places to calculate (default=5)
    
    Returns:
        float: Approximation of pi to the specified digits
    """
    def arctan(x, num_terms):
        """Calculate arctan using Taylor series expansion"""
        result = 0
        x_squared = x * x
        x_power = x
        for n in range(num_terms):
            sign = (-1) ** n
            result += sign * x_power / (2 * n + 1)
            x_power *= x_squared
        return result
    
    # Number of terms needed for accuracy (empirically determined)
    num_terms = 100 + digits * 10
    
    # Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    pi = 4 * (4 * arctan(1/5, num_terms) - arctan(1/239, num_terms))
    
    # Round to specified digits
    return round(pi, digits)