"""
Session 2: Conditional Statements Solutions
Complete solutions for all 4 exercises
"""

def exercise_1_divisible_by_3():
    """
    Exercise 1: Find numbers divisible by 3 between 1000 and 2500 (both included)
    """
    print("Exercise 1: Numbers divisible by 3 between 1000 and 2500")
    print("=" * 60)
    
    # Method 1: Using list comprehension
    divisible_by_3 = [num for num in range(1000, 2501) if num % 3 == 0]
    
    print(f"Total numbers found: {len(divisible_by_3)}")
    print(f"First 10 numbers: {divisible_by_3[:10]}")
    print(f"Last 10 numbers: {divisible_by_3[-10:]}")
    
    # Method 2: Using for loop (alternative approach)
    print("\nAlternative method using for loop:")
    count = 0
    for num in range(1000, 2501):
        if num % 3 == 0:
            count += 1
            if count <= 5:  # Show first 5 numbers
                print(f"  {num} is divisible by 3")
    
    print(f"  ... and {count - 5} more numbers")
    print(f"Total count: {count}")
    
    return divisible_by_3

def exercise_2_month_to_days():
    """
    Exercise 2: Convert month name to number of days
    """
    print("\nExercise 2: Month name to number of days")
    print("=" * 60)
    
    # Dictionary mapping months to days
    month_days = {
        'january': 31, 'february': 28, 'march': 31, 'april': 30,
        'may': 31, 'june': 30, 'july': 31, 'august': 31,
        'september': 30, 'october': 31, 'november': 30, 'december': 31
    }
    
    # Test cases
    test_months = ['january', 'february', 'april', 'june', 'september', 'december']
    
    for month in test_months:
        days = month_days.get(month.lower(), 'Invalid month')
        print(f"{month.capitalize()}: {days} days")
    
    # Interactive version
    print("\nInteractive version:")
    while True:
        month_input = input("Enter month name (or 'quit' to exit): ").lower()
        
        if month_input == 'quit':
            break
        
        if month_input in month_days:
            print(f"{month_input.capitalize()} has {month_days[month_input]} days")
        else:
            print(f"'{month_input}' is not a valid month name")
    
    return month_days

def exercise_3_reverse_word():
    """
    Exercise 3: Accept a word from user and reverse it
    """
    print("\nExercise 3: Reverse a word")
    print("=" * 60)
    
    # Method 1: Using string slicing
    def reverse_word_slicing(word):
        return word[::-1]
    
    # Method 2: Using reversed() function
    def reverse_word_reversed(word):
        return ''.join(reversed(word))
    
    # Method 3: Using for loop
    def reverse_word_loop(word):
        reversed_word = ""
        for char in word:
            reversed_word = char + reversed_word
        return reversed_word
    
    # Test cases
    test_words = ['hello', 'python', 'programming', 'data science']
    
    print("Testing different methods:")
    for word in test_words:
        print(f"\nOriginal word: '{word}'")
        print(f"Method 1 (slicing): '{reverse_word_slicing(word)}'")
        print(f"Method 2 (reversed): '{reverse_word_reversed(word)}'")
        print(f"Method 3 (loop): '{reverse_word_loop(word)}'")
    
    # Interactive version
    print("\nInteractive version:")
    while True:
        user_word = input("Enter a word to reverse (or 'quit' to exit): ")
        
        if user_word.lower() == 'quit':
            break
        
        if user_word.strip():  # Check if word is not empty
            reversed_result = reverse_word_slicing(user_word)
            print(f"'{user_word}' reversed is '{reversed_result}'")
        else:
            print("Please enter a valid word")

def exercise_4_fizzbuzz_variant():
    """
    Exercise 4: Iterate 1 to 50, print "Wonderful" for multiples of 3,
    "Nice" for multiples of 5, "Perfect" for multiples of both
    """
    print("\nExercise 4: FizzBuzz variant (1 to 50)")
    print("=" * 60)
    
    print("Numbers from 1 to 50:")
    print("-" * 30)
    
    for num in range(1, 51):
        if num % 3 == 0 and num % 5 == 0:
            print(f"{num:2d}: Perfect")
        elif num % 3 == 0:
            print(f"{num:2d}: Wonderful")
        elif num % 5 == 0:
            print(f"{num:2d}: Nice")
        else:
            print(f"{num:2d}: {num}")
    
    # Summary
    print("\nSummary:")
    wonderful_count = len([num for num in range(1, 51) if num % 3 == 0 and num % 5 != 0])
    nice_count = len([num for num in range(1, 51) if num % 5 == 0 and num % 3 != 0])
    perfect_count = len([num for num in range(1, 51) if num % 3 == 0 and num % 5 == 0])
    
    print(f"Wonderful (multiples of 3 only): {wonderful_count}")
    print(f"Nice (multiples of 5 only): {nice_count}")
    print(f"Perfect (multiples of both 3 and 5): {perfect_count}")

def run_all_exercises():
    """
    Run all exercises
    """
    print("SESSION 2: CONDITIONAL STATEMENTS SOLUTIONS")
    print("=" * 80)
    
    # Exercise 1
    exercise_1_divisible_by_3()
    
    # Exercise 2
    exercise_2_month_to_days()
    
    # Exercise 3
    exercise_3_reverse_word()
    
    # Exercise 4
    exercise_4_fizzbuzz_variant()
    
    print("\n" + "=" * 80)
    print("All exercises completed!")

if __name__ == "__main__":
    run_all_exercises() 