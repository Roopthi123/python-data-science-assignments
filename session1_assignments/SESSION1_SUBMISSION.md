# Session 1 Assignment Submission
**Python for Data Science Course**

## Assignment Overview
This submission contains the complete solutions for Session 1 assignments:
1. **Task 1:** Prime Number Checker - Flowchart and Pseudocode
2. **Task 2:** French Tax Deduction System - Flowchart and Pseudocode

---

## Task 1: Prime Number Checker

### Problem Statement
Create a flowchart and pseudocode to determine if a given number is prime or not.
- A prime number is a natural number greater than 1 that can only be divided by 1 and itself.

### Pseudocode
```
1. Input: number
2. If number < 2, return "NOT PRIME"
3. If number == 2, return "PRIME"
4. If number is even, return "NOT PRIME"
5. For each odd number i from 3 to √number:
   a. If number % i == 0, return "NOT PRIME"
6. Return "PRIME"
```

### Flowchart Logic
1. **Start**
2. **Input number**
3. **Is number < 2?** → Yes: Return "NOT PRIME"
4. **Is number == 2?** → Yes: Return "PRIME"
5. **Is number even?** → Yes: Return "NOT PRIME"
6. **Check odd divisors from 3 to √number**
7. **Found divisor?** → Yes: Return "NOT PRIME"
8. **No divisors found** → Return "PRIME"
9. **End**

### Implementation Results
The Python implementation correctly identifies prime numbers:
- **Prime numbers:** 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31
- **Non-prime numbers:** 1, 4, 6, 8, 9, 10, 15, 20, 25

### Files Created
- `prime_number_flowchart.py` - Complete implementation with tests
- `prime_number_flowchart.png` - Visual flowchart diagram

---

## Task 2: French Tax Deduction System

### Problem Statement
Create a flowchart and pseudocode for the French tax deduction system with three main rules:

#### Rule 1: Income Threshold Based on Tax Reference Income (RFR)
- To qualify for tax reductions, the taxpayer's tax reference income must fall below specific annual limits.

#### Rule 2: Family Quotient Advantage
- Taxpayers receive reductions based on their family situation through the "quotient familial" system.
- The more dependents, the more parts counted in the household.
- Limit: €1,759 per half-share in 2024.

#### Rule 3: Eligibility Through Deductible Expenses and Credits
- **Home help services:** 50% credit on eligible costs
- **Childcare for children under 6:** 50% credit on up to €3,500 of expenses
- **Energy-saving home improvements:** Eligible for eco-tax benefits

### Pseudocode
```
1. Input: tax_reference_income, threshold, dependents, expenses
2. If tax_reference_income >= threshold, return €0
3. Calculate family quotient reduction:
   a. family_parts = 1 + (dependents * 0.5)
   b. reduced_income = taxable_income / family_parts
   c. reduction = tax_on_original - tax_on_reduced
   d. Apply limit: max_reduction = dependents * €1,759
4. Calculate expense credits:
   a. Home help: min(amount, €12,000) * 50%
   b. Childcare: min(amount, €3,500) * 50%
   c. Energy improvements: min(amount, €8,000) * 30%
5. Return total_benefits = family_reduction + expense_credits
```

### Flowchart Logic
1. **Start**
2. **Input:** tax reference income, threshold, dependents, expenses
3. **Is income < threshold?** → No: Return €0 benefits
4. **Calculate family quotient reduction**
5. **Calculate expense credits**
6. **Sum all benefits**
7. **Return total benefits**
8. **End**

### Implementation Results
The system correctly calculates tax benefits:

**Test Case 1: Single person, low income**
- Tax Reference Income: €25,000
- Income Threshold: €30,000
- Dependents: 0
- Expenses: Home help €5,000, Energy improvements €3,000
- **Total Benefits: €3,400.00**

**Test Case 2: Family with children (income above threshold)**
- Tax Reference Income: €45,000
- Income Threshold: €30,000
- Dependents: 2
- Expenses: Childcare €4,000, Home help €8,000
- **Total Benefits: €0.00** (income above threshold)

### Files Created
- `french_tax_system.py` - Complete implementation with test cases
- `french_tax_flowchart.png` - Visual flowchart diagram

---

## Technical Implementation Details

### Code Structure
Both assignments follow best practices:
- **Modular design** with separate functions for each logical component
- **Comprehensive documentation** with detailed comments explaining the pseudocode
- **Test cases** to validate the implementations
- **Error handling** and edge case consideration

### Key Algorithms

#### Prime Number Checker
- **Optimization:** Only checks odd numbers up to √number
- **Efficiency:** O(√n) time complexity
- **Special cases:** Handles 1, 2, and even numbers efficiently

#### French Tax System
- **Modular approach:** Separate functions for each rule
- **Configurable constants:** Easy to update for different years
- **Comprehensive calculation:** Handles all three rules systematically

### Visual Flowcharts
- **Professional diagrams** created using matplotlib
- **Color-coded elements:** Different colors for start/end, processes, decisions
- **Clear flow direction:** Arrows showing logical progression
- **Detailed annotations:** Labels for decision outcomes

---

## Submission Checklist

- [x] **Task 1:** Prime Number Checker
  - [x] Pseudocode documented
  - [x] Flowchart logic defined
  - [x] Python implementation completed
  - [x] Test cases executed successfully
  - [x] Visual flowchart created

- [x] **Task 2:** French Tax Deduction System
  - [x] All three rules implemented
  - [x] Pseudocode documented
  - [x] Flowchart logic defined
  - [x] Python implementation completed
  - [x] Test cases executed successfully
  - [x] Visual flowchart created

- [x] **Documentation**
  - [x] Comprehensive README
  - [x] Code comments explaining logic
  - [x] Test results included
  - [x] Submission document prepared

---

## Files Included in Submission

```
session1_assignments/
├── prime_number_flowchart.py          # Task 1 implementation
├── french_tax_system.py               # Task 2 implementation
├── create_flowcharts.py               # Flowchart generation script
├── prime_number_flowchart.png         # Task 1 visual flowchart
├── french_tax_flowchart.png           # Task 2 visual flowchart
└── SESSION1_SUBMISSION.md             # This submission document
```

---

## How to Run the Code

1. **Test Prime Number Checker:**
   ```bash
   python session1_assignments/prime_number_flowchart.py
   ```

2. **Test French Tax System:**
   ```bash
   python session1_assignments/french_tax_system.py
   ```

3. **Generate Flowcharts:**
   ```bash
   python session1_assignments/create_flowcharts.py
   ```

---

## Conclusion

Both assignments have been completed successfully with:
- **Clear pseudocode** that follows logical flow
- **Detailed flowcharts** showing decision points and processes
- **Working Python implementations** with comprehensive test cases
- **Professional documentation** explaining the logic and results

The solutions demonstrate understanding of:
- **Algorithm design** and optimization
- **Flowchart creation** and logical flow
- **Python programming** with proper structure
- **Problem-solving** approach for complex systems 