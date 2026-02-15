"""
PERSONAL EXPENSE TRACKER - SIMPLE VERSION
All code in ONE file for easy understanding
"""

import json
import os
from datetime import datetime
 
# ============================================================================
# CLASS 1: EXPENSE
# ============================================================================

class Expense:
    """Represents a single expense"""
    
    def __init__(self, amount, category, description, date=None):
        """
        Create a new expense
        
        amount: How much money (example: 100, 500.50)
        category: Type of expense (Food, Transport, etc.)
        description: What you bought (example: "Lunch")
        date: When you bought it (optional - uses today if not given)
        """
        self.amount = amount
        self.category = category
        self.description = description
        
        # If no date given, use today's date
        if date is None:
            self.date = datetime.now().strftime("%Y-%m-%d")  # Format: 2026-02-13
        else:
            self.date = date


# ============================================================================
# CLASS 2: BUDGET
# ============================================================================

class Budget:
    """Manages monthly budget"""
    
    def __init__(self, monthly_limit=50000):
        """
        Create budget with a limit
        
        monthly_limit: How much you can spend per month (default: 50000)
        """
        self.monthly_limit = monthly_limit
        self.current_spending = 0  # How much spent so far
    
    def update_spending(self, total):
        """Update how much has been spent"""
        self.current_spending = total
    
    def get_remaining(self):
        """Calculate how much money is left"""
        return self.monthly_limit - self.current_spending
    
    def get_percentage_used(self):
        """Calculate what percentage of budget is used"""
        if self.monthly_limit == 0:
            return 0
        return (self.current_spending / self.monthly_limit) * 100
    
    def is_over_budget(self):
        """Check if we spent more than the limit"""
        return self.current_spending > self.monthly_limit


# ============================================================================
# CLASS 3: EXPENSE TRACKER
# ============================================================================

class ExpenseTracker:
    """Main class that manages everything"""
    
    # These are the allowed categories
    CATEGORIES = ['Food', 'Transport', 'Utilities', 'Entertainment', 'Health', 'Other']
    
    def __init__(self):
        """Start the tracker"""
        self.expenses = []  # Empty list to store all expenses
        self.budget = Budget()  # Create a budget object
        self.data_file = 'expenses_data.json'  # File to save data
        self.load_expenses()  # Load any previously saved expenses
    
    # ------------------------------------------------------------------------
    # ADD EXPENSE
    # ------------------------------------------------------------------------
    
    def add_expense(self, amount, category, description):
        """Add a new expense"""
        
        # Check if amount is positive
        if amount <= 0:
            print(" Amount must be positive!")
            return False
        
        # Check if category is valid
        if category not in self.CATEGORIES:
            print(f" Invalid category! Choose from: {', '.join(self.CATEGORIES)}")
            return False
        
        # Create new expense and add to list
        new_expense = Expense(amount, category, description)
        self.expenses.append(new_expense)
        
        # Save to file
        self.save_expenses()
        
        # Update budget
        total = self.calculate_total()
        self.budget.update_spending(total)
        
        print(f" Expense added successfully!")
        return True
    
    # ------------------------------------------------------------------------
    # VIEW EXPENSES
    # ------------------------------------------------------------------------
    
    def view_all_expenses(self):
        """Show all expenses"""
        
        if len(self.expenses) == 0:
            print("\n📭 No expenses recorded yet!")
            return
        
        print("\n" + "="*80)
        print("ALL EXPENSES")
        print("="*80)
        print(f"{'Date':<12} | {'Category':<15} | {'Amount':>10} | Description")
        print("-"*80)
        
        # Loop through each expense and print it
        for exp in self.expenses:
            print(f"{exp.date:<12} | {exp.category:<15} | ₹{exp.amount:>9.2f} | {exp.description}")
        
        print("-"*80)
        print(f"TOTAL SPENT: ₹{self.calculate_total():.2f}")
        print("="*80)
    
    def view_by_category(self, category):
        """Show expenses for one category"""
        
        # Create empty list for this category
        category_expenses = []
        
        # Loop through all expenses
        for exp in self.expenses:
            if exp.category == category:
                category_expenses.append(exp)
        
        # If no expenses in this category
        if len(category_expenses) == 0:
            print(f"\n📭 No expenses in {category} category")
            return
        
        # Print expenses in this category
        print(f"\n--- {category} Expenses ---")
        total = 0
        for exp in category_expenses:
            print(f"{exp.date} | ₹{exp.amount:.2f} | {exp.description}")
            total = total + exp.amount
        
        print(f"\nTotal for {category}: ₹{total:.2f}")
    
    # ------------------------------------------------------------------------
    # CALCULATE TOTALS
    # ------------------------------------------------------------------------
    
    def calculate_total(self):
        """Calculate total money spent"""
        total = 0
        for exp in self.expenses:
            total = total + exp.amount
        return total
    
    def calculate_category_totals(self):
        """Calculate total for each category"""
        
        # Create empty dictionary
        totals = {}
        
        # For each category
        for category in self.CATEGORIES:
            category_total = 0
            
            # Add up all expenses in this category
            for exp in self.expenses:
                if exp.category == category:
                    category_total = category_total + exp.amount
            
            # Store in dictionary
            totals[category] = category_total
        
        return totals
    
    # ------------------------------------------------------------------------
    # BUDGET STATUS
    # ------------------------------------------------------------------------
    
    def show_budget_status(self):
        """Display budget information"""
        
        print("\n" + "="*50)
        print("BUDGET STATUS")
        print("="*50)
        print(f"Monthly Budget:  ₹{self.budget.monthly_limit:.2f}")
        print(f"Total Spent:     ₹{self.budget.current_spending:.2f}")
        print(f"Remaining:       ₹{self.budget.get_remaining():.2f}")
        print(f"Percentage Used: {self.budget.get_percentage_used():.1f}%")
        
        # Show warning or alert
        if self.budget.is_over_budget():
            over_amount = self.budget.current_spending - self.budget.monthly_limit
            print(f"\n BUDGET EXCEEDED! You're over by ₹{over_amount:.2f}")
        elif self.budget.get_percentage_used() >= 80:
            print(f"\n WARNING: You've used {self.budget.get_percentage_used():.1f}% of your budget!")
        else:
            print("\n Budget is on track")
        
        print("="*50)
        
        # Show category breakdown
        print("\n--- Spending by Category ---")
        category_totals = self.calculate_category_totals()
        
        for category, amount in category_totals.items():
            if amount > 0:
                print(f"{category:<15}: ₹{amount:>8.2f}")
    
    def set_budget(self, new_limit):
        """Change the monthly budget limit"""
        if new_limit <= 0:
            print("❌ Budget must be positive!")
            return False
        
        self.budget.monthly_limit = new_limit
        self.save_expenses()  # Save the new budget
        print(f" Budget set to ₹{new_limit:.2f}")
        return True
    
    # ------------------------------------------------------------------------
    # SAVE AND LOAD DATA
    # ------------------------------------------------------------------------
    
    def save_expenses(self):
        """Save all expenses to a JSON file"""
        
        # Create a dictionary to save
        data = {
            'budget_limit': self.budget.monthly_limit,
            'expenses': []
        }
        
        # Convert each expense to a dictionary
        for exp in self.expenses:
            expense_dict = {
                'amount': exp.amount,
                'category': exp.category,
                'description': exp.description,
                'date': exp.date
            }
            data['expenses'].append(expense_dict)
        
        # Write to file
        with open(self.data_file, 'w') as file:
            json.dump(data, file, indent=4)
    
    def load_expenses(self):
        """Load expenses from JSON file"""
        
        # Check if file exists
        if not os.path.exists(self.data_file):
            print("No previous data found. Starting fresh!")
            return
        
        try:
            # Open and read file
            with open(self.data_file, 'r') as file:
                data = json.load(file)
            
            # Load budget
            if 'budget_limit' in data:
                self.budget.monthly_limit = data['budget_limit']
            
            # Load expenses
            if 'expenses' in data:
                for exp_dict in data['expenses']:
                    expense = Expense(
                        amount=exp_dict['amount'],
                        category=exp_dict['category'],
                        description=exp_dict['description'],
                        date=exp_dict['date']
                    )
                    self.expenses.append(expense)
            
            # Update budget with loaded expenses
            total = self.calculate_total()
            self.budget.update_spending(total)
            
            print(f" Loaded {len(self.expenses)} expenses from previous session")
            
        except Exception as error:
            print(f" Error loading data: {error}")


# ============================================================================
# MENU FUNCTIONS
# ============================================================================

def show_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("   PERSONAL EXPENSE TRACKER")
    print("="*50)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View by Category")
    print("4. Budget Status")
    print("5. Set Monthly Budget")
    print("6. Exit")
    print("="*50)


def get_user_choice():
    """Get menu choice from user"""
    choice = input("\nEnter your choice (1-6): ")
    return choice


def add_expense_menu(tracker):
    """Menu option to add an expense"""
    print("\n--- Add New Expense ---")
    
    try:
        # Get amount
        amount = float(input("Enter amount (₹): "))
        
        # Show categories
        print("\nCategories:")
        for i, cat in enumerate(tracker.CATEGORIES, 1):
            print(f"{i}. {cat}")
        
        # Get category choice
        cat_num = int(input("Select category (1-6): "))
        
        if cat_num < 1 or cat_num > 6:
            print(" Invalid category number!")
            return
        
        category = tracker.CATEGORIES[cat_num - 1]
        
        # Get description
        description = input("Enter description: ")
        
        # Add expense
        tracker.add_expense(amount, category, description)
        
        # Show budget status after adding
        remaining = tracker.budget.get_remaining()
        percentage = tracker.budget.get_percentage_used()
        print(f"\nBudget: {percentage:.1f}% used, ₹{remaining:.2f} remaining")
        
    except ValueError:
        print(" Invalid input! Please enter numbers correctly.")
    except Exception as error:
        print(f" Error: {error}")


def view_by_category_menu(tracker):
    """Menu option to view expenses by category"""
    print("\nCategories:")
    for i, cat in enumerate(tracker.CATEGORIES, 1):
        print(f"{i}. {cat}")
    
    try:
        cat_num = int(input("Select category (1-6): "))
        
        if cat_num < 1 or cat_num > 6:
            print(" Invalid category number!")
            return
        
        category = tracker.CATEGORIES[cat_num - 1]
        tracker.view_by_category(category)
        
    except ValueError:
        print(" Invalid input!")


def set_budget_menu(tracker):
    """Menu option to set budget"""
    try:
        amount = float(input("\nEnter monthly budget (₹): "))
        tracker.set_budget(amount)
    except ValueError:
        print(" Invalid amount!")


# ============================================================================
# MAIN PROGRAM
# ============================================================================

def main():
    """Main program - runs when you start the tracker"""
    
    print("\n Welcome to Personal Expense Tracker!")
    
    # Create tracker object
    tracker = ExpenseTracker()
    
    # Main loop - keeps running until user exits
    while True:
        show_menu()
        choice = get_user_choice()
        
        if choice == '1':
            add_expense_menu(tracker)
        
        elif choice == '2':
            tracker.view_all_expenses()
        
        elif choice == '3':
            view_by_category_menu(tracker)
        
        elif choice == '4':
            tracker.show_budget_status()
        
        elif choice == '5':
            set_budget_menu(tracker)
        
        elif choice == '6':
            print("\nThank you for using Expense Tracker!")
            print("All data has been saved automatically.")
            break
        
        else:
            print(" Invalid choice! Please enter 1-6")


# Start the program
if __name__ == "__main__":
    main()