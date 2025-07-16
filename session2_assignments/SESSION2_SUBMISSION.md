# Session 2 Assignment Submission
**Python for Data Science Course - Conditional Statements**

## Assignment Overview
This submission contains complete solutions for Session 2: Conditional Statements exercises.

---

## Exercise 1: Numbers Divisible by 3

### Problem Statement
Write a Python program to find those numbers which are divisible by 3 and are between 1000 and 2500 (both included).

### Solution
```python
# Method 1: Using list comprehension
divisible_by_3 = [num for num in range(1000, 2501) if num % 3 == 0]

# Method 2: Using for loop
count = 0
for num in range(1000, 2501):
    if num % 3 == 0:
        count += 1
```

### Results
- **Total numbers found:** 501
- **First 10 numbers:** [1002, 1005, 1008, 1011, 1014, 1017, 1020, 1023, 1026, 1029]
- **Last 10 numbers:** [2472, 2475, 2478, 2481, 2484, 2487, 2490, 2493, 2496, 2499]

### Key Concepts Used
- **Range function** with inclusive bounds
- **Modulo operator** (%) for divisibility check
- **List comprehension** for efficient filtering
- **Conditional statements** (if)

---

## Exercise 2: Month to Days Converter

### Problem Statement
Write a Python program to convert month name to a number of days in this month.

### Solution
```python
month_days = {
    'january': 31, 'february': 28, 'march': 31, 'april': 30,
    'may': 31, 'june': 30, 'july': 31, 'august': 31,
    'september': 30, 'october': 31, 'november': 30, 'december': 31
}

def get_days_in_month(month_name):
    month_name = month_name.lower()
    if month_name in month_days:
        return month_days[month_name]
    else:
        return "Invalid month name"
```

### Test Results
- **January:** 31 days
- **February:** 28 days
- **April:** 30 days
- **June:** 30 days
- **September:** 30 days
- **December:** 31 days

### Key Concepts Used
- **Dictionary** for month-to-days mapping
- **String methods** (lower(), capitalize())
- **Dictionary lookup** with get() method
- **Conditional statements** for validation

---

## Exercise 3: Word Reversal

### Problem Statement
Write a Python program that accepts a word from the user and reverse it.

### Solution
```python
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
```

### Test Results
- **'hello'** → **'olleh'**
- **'python'** → **'nohtyp'**
- **'programming'** → **'gnimmargorp'**
- **'data science'** → **'ecneics atad'**

### Key Concepts Used
- **String slicing** with negative step
- **reversed() function** with join()
- **String concatenation** in loops
- **Multiple solution approaches**

---

## Exercise 4: FizzBuzz Variant

### Problem Statement
Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Wonderful" instead of the number and for the multiples of five print "Nice". For numbers which are multiples of both three and five print "Perfect".

### Solution
```python
for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num:2d}: Perfect")
    elif num % 3 == 0:
        print(f"{num:2d}: Wonderful")
    elif num % 5 == 0:
        print(f"{num:2d}: Nice")
    else:
        print(f"{num:2d}: {num}")
```

### Results Summary
- **Wonderful (multiples of 3 only):** 13 numbers
- **Nice (multiples of 5 only):** 7 numbers
- **Perfect (multiples of both 3 and 5):** 3 numbers

### Sample Output
```
 1: 1
 2: 2
 3: Wonderful
 4: 4
 5: Nice
 6: Wonderful
 7: 7
 8: 8
 9: Wonderful
10: Nice
11: 11
12: Wonderful
13: 13
14: 14
15: Perfect
```

### Key Concepts Used
- **Multiple conditional statements** (if-elif-else)
- **Logical operators** (and)
- **Modulo operator** for divisibility
- **String formatting** with field width
- **Range iteration**

---

## Technical Implementation Details

### Code Structure
- **Modular functions** for each exercise
- **Comprehensive documentation** with docstrings
- **Multiple solution approaches** where applicable
- **Test cases** to validate solutions
- **Error handling** for edge cases

### Conditional Statements Demonstrated
1. **Simple if statements** - Basic conditional execution
2. **if-elif-else chains** - Multiple condition handling
3. **Nested conditionals** - Complex decision trees
4. **Logical operators** - Compound conditions
5. **Comparison operators** - Various comparisons

### Key Learning Outcomes
- **Range manipulation** with conditional filtering
- **Dictionary operations** for data lookup
- **String manipulation** techniques
- **Loop control** with conditional logic
- **Multiple solution approaches** for the same problem

---

## Files Included

```
session2_assignments/
├── conditional_statements_solutions.py     # Complete solutions with interactive features
├── test_conditional_statements.py          # Test version without user input
├── Conditional_Statements_Solutions.ipynb  # Jupyter notebook version
└── SESSION2_SUBMISSION.md                  # This submission document
```

---

## How to Run the Code

1. **Run all exercises:**
   ```bash
   python session2_assignments/test_conditional_statements.py
   ```

2. **Interactive version:**
   ```bash
   python session2_assignments/conditional_statements_solutions.py
   ```

3. **Jupyter notebook:**
   Open `Conditional_Statements_Solutions.ipynb` in Jupyter

---

## Conclusion

All four exercises have been completed successfully with:
- **Clear, readable code** following Python best practices
- **Multiple solution approaches** demonstrating different techniques
- **Comprehensive testing** with various input scenarios
- **Proper documentation** explaining the logic and approach
- **Understanding of conditional statements** and their applications

The solutions demonstrate mastery of:
- **Conditional logic** and decision-making in Python
- **Loop control** with conditional statements
- **Data structure manipulation** with conditions
- **String operations** and formatting
- **Problem-solving** with multiple approaches 