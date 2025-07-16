"""
Task 1: Prime Number Checker
Flowchart and Pseudocode Implementation

A prime number is a natural number greater than 1 that can only be divided by 1 and itself.
"""

def is_prime(number):
    """
    Check if a given number is prime.
    
    Pseudocode:
    1. If number < 2, return False (not prime)
    2. If number == 2, return True (2 is prime)
    3. If number is even (except 2), return False
    4. Check odd numbers from 3 to sqrt(number)
    5. If any number divides evenly, return False
    6. If no divisors found, return True
    """
    
    # Step 1: Check if number is less than 2
    if number < 2:
        return False
    
    # Step 2: Check if number is 2 (special case)
    if number == 2:
        return True
    
    # Step 3: Check if number is even (except 2)
    if number % 2 == 0:
        return False
    
    # Step 4: Check odd numbers from 3 to sqrt(number)
    import math
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    
    # Step 5: If no divisors found, it's prime
    return True

# Test the function
def test_prime_checker():
    """Test the prime number checker with various numbers."""
    
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 20, 23, 25, 29, 31]
    
    print("Prime Number Checker Test Results:")
    print("=" * 40)
    
    for num in test_numbers:
        result = is_prime(num)
        status = "PRIME" if result else "NOT PRIME"
        print(f"Number {num:2d}: {status}")
    
    print("\n" + "=" * 40)
    print("Flowchart Logic:")
    print("1. Start")
    print("2. Input number")
    print("3. Is number < 2? → Yes: Return 'Not Prime'")
    print("4. Is number == 2? → Yes: Return 'Prime'")
    print("5. Is number even? → Yes: Return 'Not Prime'")
    print("6. Check odd divisors from 3 to √number")
    print("7. Found divisor? → Yes: Return 'Not Prime'")
    print("8. No divisors found → Return 'Prime'")
    print("9. End")

if __name__ == "__main__":
    test_prime_checker() 