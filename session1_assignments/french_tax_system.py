"""
Task 2: French Tax Deduction System
Flowchart and Pseudocode Implementation

Rules:
1. Income Threshold Based on Tax Reference Income (RFR)
2. Family Quotient Advantage
3. Eligibility Through Deductible Expenses and Credits
"""

class FrenchTaxSystem:
    def __init__(self):
        # Constants for 2024
        self.FAMILY_QUOTIENT_LIMIT = 1759  # €1,759 limit per half-share
        self.CHILDCARE_CREDIT_LIMIT = 3500  # €3,500 limit for childcare
        self.CREDIT_PERCENTAGE = 0.50  # 50% credit rate
        
    def check_income_threshold(self, tax_reference_income, threshold):
        """
        Rule 1: Check if income is below threshold for tax reductions.
        
        Pseudocode:
        1. Input tax reference income
        2. Input threshold limit
        3. If income < threshold, return True (eligible)
        4. Else return False (not eligible)
        """
        return tax_reference_income < threshold
    
    def calculate_family_quotient(self, dependents):
        """
        Rule 2: Calculate family quotient based on dependents.
        
        Pseudocode:
        1. Input number of dependents
        2. Calculate family parts (1 + dependents * 0.5)
        3. Return family quotient
        """
        # Base: 1 part for the taxpayer
        # Each dependent adds 0.5 parts
        family_parts = 1 + (dependents * 0.5)
        return family_parts
    
    def calculate_family_reduction(self, dependents, taxable_income):
        """
        Calculate tax reduction based on family quotient.
        
        Pseudocode:
        1. Calculate family quotient
        2. Divide taxable income by family quotient
        3. Calculate tax on reduced income
        4. Apply family quotient limit
        5. Return reduction amount
        """
        family_quotient = self.calculate_family_quotient(dependents)
        reduced_income = taxable_income / family_quotient
        
        # Simplified tax calculation (this would be more complex in reality)
        tax_on_reduced = reduced_income * 0.14  # Simplified 14% rate
        tax_on_original = taxable_income * 0.14
        
        reduction = tax_on_original - tax_on_reduced
        
        # Apply limit per half-share
        max_reduction = dependents * self.FAMILY_QUOTIENT_LIMIT
        
        return min(reduction, max_reduction)
    
    def calculate_expense_credits(self, expenses):
        """
        Rule 3: Calculate credits for deductible expenses.
        
        Pseudocode:
        1. Input expense type and amount
        2. Check if expense is eligible
        3. Apply credit percentage
        4. Apply limits if applicable
        5. Return credit amount
        """
        total_credit = 0
        
        # Home help services (50% credit)
        if 'home_help' in expenses:
            home_help_amount = min(expenses['home_help'], 12000)  # €12,000 limit
            total_credit += home_help_amount * self.CREDIT_PERCENTAGE
        
        # Childcare for children under 6 (50% credit, up to €3,500)
        if 'childcare' in expenses:
            childcare_amount = min(expenses['childcare'], self.CHILDCARE_CREDIT_LIMIT)
            total_credit += childcare_amount * self.CREDIT_PERCENTAGE
        
        # Energy-saving improvements (simplified)
        if 'energy_improvements' in expenses:
            energy_amount = min(expenses['energy_improvements'], 8000)  # €8,000 limit
            total_credit += energy_amount * 0.30  # 30% credit
        
        return total_credit
    
    def calculate_total_tax_benefits(self, tax_reference_income, threshold, 
                                   dependents, taxable_income, expenses):
        """
        Main function to calculate total tax benefits.
        
        Pseudocode:
        1. Check income threshold eligibility
        2. If eligible, calculate family reduction
        3. Calculate expense credits
        4. Sum all benefits
        5. Return total benefits
        """
        total_benefits = 0
        
        # Check if eligible based on income threshold
        if self.check_income_threshold(tax_reference_income, threshold):
            # Calculate family quotient reduction
            family_reduction = self.calculate_family_reduction(dependents, taxable_income)
            total_benefits += family_reduction
            
            # Calculate expense credits
            expense_credits = self.calculate_expense_credits(expenses)
            total_benefits += expense_credits
        
        return total_benefits

def test_french_tax_system():
    """Test the French tax deduction system."""
    
    tax_system = FrenchTaxSystem()
    
    print("French Tax Deduction System Test")
    print("=" * 50)
    
    # Test Case 1: Single person, low income
    print("\nTest Case 1: Single person, low income")
    print("-" * 40)
    income_threshold = 30000
    tax_ref_income = 25000
    dependents = 0
    taxable_income = 25000
    expenses = {'home_help': 5000, 'energy_improvements': 3000}
    
    benefits = tax_system.calculate_total_tax_benefits(
        tax_ref_income, income_threshold, dependents, taxable_income, expenses
    )
    
    print(f"Tax Reference Income: €{tax_ref_income:,}")
    print(f"Income Threshold: €{income_threshold:,}")
    print(f"Dependents: {dependents}")
    print(f"Expenses: {expenses}")
    print(f"Total Benefits: €{benefits:,.2f}")
    
    # Test Case 2: Family with children
    print("\nTest Case 2: Family with children")
    print("-" * 40)
    tax_ref_income = 45000
    dependents = 2
    taxable_income = 45000
    expenses = {'childcare': 4000, 'home_help': 8000}
    
    benefits = tax_system.calculate_total_tax_benefits(
        tax_ref_income, income_threshold, dependents, taxable_income, expenses
    )
    
    print(f"Tax Reference Income: €{tax_ref_income:,}")
    print(f"Dependents: {dependents}")
    print(f"Expenses: {expenses}")
    print(f"Total Benefits: €{benefits:,.2f}")
    
    print("\n" + "=" * 50)
    print("Flowchart Logic:")
    print("1. Start")
    print("2. Input tax reference income, threshold, dependents, expenses")
    print("3. Is income < threshold? → No: Return €0 benefits")
    print("4. Calculate family quotient reduction")
    print("5. Calculate expense credits")
    print("6. Sum all benefits")
    print("7. Return total benefits")
    print("8. End")

if __name__ == "__main__":
    test_french_tax_system() 