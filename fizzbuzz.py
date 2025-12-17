#!/usr/bin/env python3
"""
FizzBuzz Implementation

This script implements the classic FizzBuzz algorithm.
For numbers from 1 to 100:
- If divisible by 3, print "Fizz"
- If divisible by 5, print "Buzz"
- If divisible by both, print "FizzBuzz"
- Otherwise, print the number
"""

def fizzbuzz(n):
    """
    Determine the FizzBuzz output for a given number.

    Args:
        n (int): The number to check

    Returns:
        str: "Fizz", "Buzz", "FizzBuzz", or str(n)
    """
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

def main():
    """Main function to run FizzBuzz for numbers 1 to 100."""
    for i in range(1, 101):
        print(fizzbuzz(i))

if __name__ == "__main__":
    main()