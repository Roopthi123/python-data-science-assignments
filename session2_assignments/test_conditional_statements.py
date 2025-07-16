"""
Test version of Session 2 Conditional Statements
Runs all exercises without user input
"""

def exercise_1_divisible_by_3():
    """Exercise 1: Find numbers divisible by 3 between 1000 and 2500"""
    print("Exercise 1: Numbers divisible by 3 between 1000 and 2500")
    print("=" * 60)
    
    # Method 1: Using list comprehension
    divisible_by_3 = [num for num in range(1000, 2501) if num % 3 == 0]
    
    print(f"Total numbers found: {len(divisible_by_3)}")
    print(f"First 10 numbers: {divisible_by_3[:10]}")
    print(f"Last 10 numbers: {divisible_by_3[-10:]}")
    
    # Method 2: Using for loop
    print("\nAlternative method using for loop:")
    count = 0
    for num in range(1000, 2501):
        if num % 3 == 0:
            count += 1
            if count <= 5:
                print(f"  {num} is divisible by 3")
    
    print(f"  ... and {count - 5} more numbers")
    print(f"Total count: {count}")
    
    return divisible_by_3

def exercise_2_month_to_days():
    """Exercise 2: Convert month name to number of days"""
    print("\nExercise 2: Month name to number of days")
    print("=" * 60)
    
    month_days = {
        'january': 31, 'february': 28, 'march': 31, 'april': 30,
        'may': 31, 'june': 30, 'july': 31, 'august': 31,
        'september': 30, 'october': 31, 'november': 30, 'december': 31
    }
    
    test_months = ['january', 'february', 'april', 'june', 'september', 'december']
    
    for month in test_months:
        days = month_days.get(month.lower(), 'Invalid month')
        print(f"{month.capitalize()}: {days} days")
    
    return month_days

def exercise_3_reverse_word():
    """Exercise 3: Reverse a word"""
    print("\nExercise 3: Reverse a word")
    print("=" * 60)
    
    def reverse_word_slicing(word):
        return word[::-1]
    
    def reverse_word_reversed(word):
        return ''.join(reversed(word))
    
    def reverse_word_loop(word):
        reversed_word = ""
        for char in word:
            reversed_word = char + reversed_word
        return reversed_word
    
    test_words = ['hello', 'python', 'programming', 'data science']
    
    print("Testing different methods:")
    for word in test_words:
        print(f"\nOriginal word: '{word}'")
        print(f"Method 1 (slicing): '{reverse_word_slicing(word)}'")
        print(f"Method 2 (reversed): '{reverse_word_reversed(word)}'")
        print(f"Method 3 (loop): '{reverse_word_loop(word)}'")

def exercise_4_fizzbuzz_variant():
    """Exercise 4: FizzBuzz variant (1 to 50)"""
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
    """Run all exercises"""
    print("SESSION 2: CONDITIONAL STATEMENTS SOLUTIONS")
    print("=" * 80)
    
    exercise_1_divisible_by_3()
    exercise_2_month_to_days()
    exercise_3_reverse_word()
    exercise_4_fizzbuzz_variant()
    
    print("\n" + "=" * 80)
    print("All exercises completed!")

if __name__ == "__main__":
    run_all_exercises() 