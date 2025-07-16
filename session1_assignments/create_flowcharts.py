"""
Create Flowchart Diagrams for Session 1 Assignments
Using matplotlib to visualize the logic flow
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np

def create_prime_number_flowchart():
    """Create flowchart for Prime Number Checker."""
    
    fig, ax = plt.subplots(1, 1, figsize=(12, 16))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 20)
    ax.axis('off')
    
    # Define colors
    start_color = '#90EE90'  # Light green
    process_color = '#87CEEB'  # Light blue
    decision_color = '#FFD700'  # Gold
    end_color = '#FFB6C1'  # Light pink
    
    # Start
    start_box = FancyBboxPatch((4, 18), 2, 0.8, boxstyle="round,pad=0.1", 
                              facecolor=start_color, edgecolor='black', linewidth=2)
    ax.add_patch(start_box)
    ax.text(5, 18.4, 'START', ha='center', va='center', fontsize=12, fontweight='bold')
    
    # Input
    input_box = FancyBboxPatch((3.5, 16.5), 3, 0.8, boxstyle="round,pad=0.1", 
                              facecolor=process_color, edgecolor='black', linewidth=2)
    ax.add_patch(input_box)
    ax.text(5, 16.9, 'Input number', ha='center', va='center', fontsize=11)
    
    # Decision 1: number < 2
    decision1 = FancyBboxPatch((3, 14.5), 4, 1.2, boxstyle="round,pad=0.1", 
                              facecolor=decision_color, edgecolor='black', linewidth=2)
    ax.add_patch(decision1)
    ax.text(5, 15.1, 'Is number < 2?', ha='center', va='center', fontsize=11)
    
    # Yes path - Not Prime
    not_prime1 = FancyBboxPatch((6.5, 13), 2, 0.8, boxstyle="round,pad=0.1", 
                               facecolor=end_color, edgecolor='black', linewidth=2)
    ax.add_patch(not_prime1)
    ax.text(7.5, 13.4, 'NOT PRIME', ha='center', va='center', fontsize=11, fontweight='bold')
    
    # Decision 2: number == 2
    decision2 = FancyBboxPatch((3, 12), 4, 1.2, boxstyle="round,pad=0.1", 
                              facecolor=decision_color, edgecolor='black', linewidth=2)
    ax.add_patch(decision2)
    ax.text(5, 12.6, 'Is number == 2?', ha='center', va='center', fontsize=11)
    
    # Yes path - Prime
    prime1 = FancyBboxPatch((6.5, 10.5), 2, 0.8, boxstyle="round,pad=0.1", 
                           facecolor=end_color, edgecolor='black', linewidth=2)
    ax.add_patch(prime1)
    ax.text(7.5, 10.9, 'PRIME', ha='center', va='center', fontsize=11, fontweight='bold')
    
    # Decision 3: number even
    decision3 = FancyBboxPatch((3, 9), 4, 1.2, boxstyle="round,pad=0.1", 
                              facecolor=decision_color, edgecolor='black', linewidth=2)
    ax.add_patch(decision3)
    ax.text(5, 9.6, 'Is number even?', ha='center', va='center', fontsize=11)
    
    # Yes path - Not Prime
    not_prime2 = FancyBboxPatch((6.5, 7.5), 2, 0.8, boxstyle="round,pad=0.1", 
                               facecolor=end_color, edgecolor='black', linewidth=2)
    ax.add_patch(not_prime2)
    ax.text(7.5, 7.9, 'NOT PRIME', ha='center', va='center', fontsize=11, fontweight='bold')
    
    # Process: Check odd divisors
    process_box = FancyBboxPatch((2.5, 6), 5, 0.8, boxstyle="round,pad=0.1", 
                                facecolor=process_color, edgecolor='black', linewidth=2)
    ax.add_patch(process_box)
    ax.text(5, 6.4, 'Check odd divisors 3 to √number', ha='center', va='center', fontsize=10)
    
    # Decision 4: Found divisor
    decision4 = FancyBboxPatch((3, 4.5), 4, 1.2, boxstyle="round,pad=0.1", 
                              facecolor=decision_color, edgecolor='black', linewidth=2)
    ax.add_patch(decision4)
    ax.text(5, 5.1, 'Found divisor?', ha='center', va='center', fontsize=11)
    
    # Yes path - Not Prime
    not_prime3 = FancyBboxPatch((6.5, 3), 2, 0.8, boxstyle="round,pad=0.1", 
                               facecolor=end_color, edgecolor='black', linewidth=2)
    ax.add_patch(not_prime3)
    ax.text(7.5, 3.4, 'NOT PRIME', ha='center', va='center', fontsize=11, fontweight='bold')
    
    # No path - Prime
    prime2 = FancyBboxPatch((3, 1.5), 4, 0.8, boxstyle="round,pad=0.1", 
                           facecolor=end_color, edgecolor='black', linewidth=2)
    ax.add_patch(prime2)
    ax.text(5, 1.9, 'PRIME', ha='center', va='center', fontsize=11, fontweight='bold')
    
    # End
    end_box = FancyBboxPatch((4, 0), 2, 0.8, boxstyle="round,pad=0.1", 
                            facecolor=start_color, edgecolor='black', linewidth=2)
    ax.add_patch(end_box)
    ax.text(5, 0.4, 'END', ha='center', va='center', fontsize=12, fontweight='bold')
    
    # Add arrows
    arrows = [
        ((5, 18), (5, 17.3)),  # Start to Input
        ((5, 16.5), (5, 15.7)),  # Input to Decision 1
        ((7, 15.1), (6.5, 13.8)),  # Decision 1 Yes to Not Prime 1
        ((5, 14.5), (5, 13.2)),  # Decision 1 No to Decision 2
        ((7, 12.6), (6.5, 11.3)),  # Decision 2 Yes to Prime 1
        ((5, 12), (5, 10.8)),  # Decision 2 No to Decision 3
        ((7, 9.6), (6.5, 8.3)),  # Decision 3 Yes to Not Prime 2
        ((5, 9), (5, 6.8)),  # Decision 3 No to Process
        ((5, 6), (5, 5.7)),  # Process to Decision 4
        ((7, 5.1), (6.5, 3.8)),  # Decision 4 Yes to Not Prime 3
        ((5, 4.5), (5, 2.3)),  # Decision 4 No to Prime 2
        ((5, 1.5), (5, 0.8)),  # Prime 2 to End
    ]
    
    for start, end in arrows:
        arrow = ConnectionPatch(start, end, "data", "data", 
                              arrowstyle="->", shrinkA=5, shrinkB=5, 
                              mutation_scale=20, fc="black", ec="black", linewidth=2)
        ax.add_patch(arrow)
    
    # Add labels
    ax.text(7.8, 15.1, 'Yes', ha='center', va='center', fontsize=10, fontweight='bold')
    ax.text(7.8, 12.6, 'Yes', ha='center', va='center', fontsize=10, fontweight='bold')
    ax.text(7.8, 9.6, 'Yes', ha='center', va='center', fontsize=10, fontweight='bold')
    ax.text(7.8, 5.1, 'Yes', ha='center', va='center', fontsize=10, fontweight='bold')
    ax.text(2.2, 15.1, 'No', ha='center', va='center', fontsize=10, fontweight='bold')
    ax.text(2.2, 12.6, 'No', ha='center', va='center', fontsize=10, fontweight='bold')
    ax.text(2.2, 9.6, 'No', ha='center', va='center', fontsize=10, fontweight='bold')
    ax.text(2.2, 5.1, 'No', ha='center', va='center', fontsize=10, fontweight='bold')
    
    ax.set_title('Prime Number Checker Flowchart', fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('prime_number_flowchart.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_french_tax_flowchart():
    """Create flowchart for French Tax Deduction System."""
    
    fig, ax = plt.subplots(1, 1, figsize=(14, 18))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 22)
    ax.axis('off')
    
    # Define colors
    start_color = '#90EE90'  # Light green
    process_color = '#87CEEB'  # Light blue
    decision_color = '#FFD700'  # Gold
    end_color = '#FFB6C1'  # Light pink
    
    # Start
    start_box = FancyBboxPatch((5, 20), 2, 0.8, boxstyle="round,pad=0.1", 
                              facecolor=start_color, edgecolor='black', linewidth=2)
    ax.add_patch(start_box)
    ax.text(6, 20.4, 'START', ha='center', va='center', fontsize=12, fontweight='bold')
    
    # Input
    input_box = FancyBboxPatch((3, 18.5), 6, 0.8, boxstyle="round,pad=0.1", 
                              facecolor=process_color, edgecolor='black', linewidth=2)
    ax.add_patch(input_box)
    ax.text(6, 18.9, 'Input: income, threshold, dependents, expenses', ha='center', va='center', fontsize=10)
    
    # Decision: Income threshold
    decision1 = FancyBboxPatch((3, 16.5), 6, 1.2, boxstyle="round,pad=0.1", 
                              facecolor=decision_color, edgecolor='black', linewidth=2)
    ax.add_patch(decision1)
    ax.text(6, 17.1, 'Is income < threshold?', ha='center', va='center', fontsize=11)
    
    # No path - No benefits
    no_benefits = FancyBboxPatch((9, 15), 2, 0.8, boxstyle="round,pad=0.1", 
                                facecolor=end_color, edgecolor='black', linewidth=2)
    ax.add_patch(no_benefits)
    ax.text(10, 15.4, '€0 Benefits', ha='center', va='center', fontsize=11, fontweight='bold')
    
    # Process: Calculate family quotient
    process1 = FancyBboxPatch((2, 14), 8, 0.8, boxstyle="round,pad=0.1", 
                             facecolor=process_color, edgecolor='black', linewidth=2)
    ax.add_patch(process1)
    ax.text(6, 14.4, 'Calculate family quotient reduction', ha='center', va='center', fontsize=10)
    
    # Process: Calculate expense credits
    process2 = FancyBboxPatch((2, 12.5), 8, 0.8, boxstyle="round,pad=0.1", 
                             facecolor=process_color, edgecolor='black', linewidth=2)
    ax.add_patch(process2)
    ax.text(6, 12.9, 'Calculate expense credits', ha='center', va='center', fontsize=10)
    
    # Process: Sum benefits
    process3 = FancyBboxPatch((2, 11), 8, 0.8, boxstyle="round,pad=0.1", 
                             facecolor=process_color, edgecolor='black', linewidth=2)
    ax.add_patch(process3)
    ax.text(6, 11.4, 'Sum all benefits', ha='center', va='center', fontsize=10)
    
    # Output: Total benefits
    output_box = FancyBboxPatch((3, 9.5), 6, 0.8, boxstyle="round,pad=0.1", 
                               facecolor=end_color, edgecolor='black', linewidth=2)
    ax.add_patch(output_box)
    ax.text(6, 9.9, 'Return total benefits', ha='center', va='center', fontsize=11, fontweight='bold')
    
    # End
    end_box = FancyBboxPatch((5, 8), 2, 0.8, boxstyle="round,pad=0.1", 
                            facecolor=start_color, edgecolor='black', linewidth=2)
    ax.add_patch(end_box)
    ax.text(6, 8.4, 'END', ha='center', va='center', fontsize=12, fontweight='bold')
    
    # Add arrows
    arrows = [
        ((6, 20), (6, 19.3)),  # Start to Input
        ((6, 18.5), (6, 17.7)),  # Input to Decision
        ((9, 17.1), (10, 15.8)),  # Decision No to No Benefits
        ((6, 16.5), (6, 14.8)),  # Decision Yes to Process 1
        ((6, 14), (6, 13.3)),  # Process 1 to Process 2
        ((6, 12.5), (6, 10.8)),  # Process 2 to Process 3
        ((6, 11), (6, 10.3)),  # Process 3 to Output
        ((6, 9.5), (6, 8.8)),  # Output to End
    ]
    
    for start, end in arrows:
        arrow = ConnectionPatch(start, end, "data", "data", 
                              arrowstyle="->", shrinkA=5, shrinkB=5, 
                              mutation_scale=20, fc="black", ec="black", linewidth=2)
        ax.add_patch(arrow)
    
    # Add labels
    ax.text(10.5, 17.1, 'No', ha='center', va='center', fontsize=10, fontweight='bold')
    ax.text(1.5, 17.1, 'Yes', ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Add detailed rules
    rules_text = """
    Rules:
    1. Income Threshold: Check if tax reference income < threshold
    2. Family Quotient: Calculate reduction based on dependents
    3. Expense Credits: Apply credits for eligible expenses
       - Home help: 50% credit (up to €12,000)
       - Childcare: 50% credit (up to €3,500)
       - Energy improvements: 30% credit (up to €8,000)
    """
    
    ax.text(0.5, 6, rules_text, ha='left', va='top', fontsize=9, 
            bbox=dict(boxstyle="round,pad=0.5", facecolor='lightgray', alpha=0.8))
    
    ax.set_title('French Tax Deduction System Flowchart', fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('french_tax_flowchart.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    print("Creating Prime Number Checker Flowchart...")
    create_prime_number_flowchart()
    
    print("Creating French Tax System Flowchart...")
    create_french_tax_flowchart()
    
    print("Flowcharts saved as:")
    print("- prime_number_flowchart.png")
    print("- french_tax_flowchart.png") 