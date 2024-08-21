import math
from mpmath import mp

def com_pi_digits(start_point, end_point):
    """
    It will give us the digits of π from the decimal point based on the start and endpoint.

    Parameters:
    start_point (int): The starting position of the digits.
    end_point (int): The ending position of the digits.

    Returns:
    list: A list of digits of π from the decimal point in the specified range.
    """
    # Set the precision to ensure we cover the required range
    precision = end_point + 10  # Adding extra digits to ensure accuracy
    mp.dps = precision

    # Get π and convert to string
    pi_str = str(mp.pi)
    
    # Extract the desired segment
    pi_segment = pi_str[start_point + 1:end_point]  # +1 to skip '3.'

    # Convert segment to list of digits
    pi_digits = [int(digit) for digit in pi_segment]

    return pi_digits