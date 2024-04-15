# objective: The aim of this assignment is to reinforce the understanding of encapsulation in Python, focusing on the use of private attributes and getters and setters. Students will apply these concepts to create a Personal Budget Management system.

# Problem Statement: You are required to build a Personal Budget Management application. The application will manage budget categories like food, entertainment, utilities, etc., ensuring that budget details remain private and are accessed or modified through public methods.

# Task 1: Define Budget Category Class

# Create a class BudgetCategory with private attributes for category name and allocated budget.
# Initialize these attributes in the constructor.
# Expected Outcome: A BudgetCategory class capable of storing category details securely.
# Task 2: Implement Getters and Setters

# Write getter and setter methods for both the category name and the allocated budget.
# Ensure that the setter methods include validation (e.g., budget should be a positive number).
# Expected Outcome: Methods that allow controlled access and modification of the private attributes, with validation checks in place.
# Task 3: Add Budget Functionality

# Implement a method to add expenses to a category and adjust the budget accordingly.
# Validate the expense amount before making deductions from the budget.
# Expected Outcome: Ability to track expenses per category and update the remaining budget safely.
# Task 4: Display Budget Details

# Create a method to display the details of a budget category, including the name, allocated budget, and remaining budget after expenses.
# Expected Outcome: Users can view a summary of each budget category, showcasing encapsulation in action.

class BudgetCategory:
    def __init__(self, name, budget):
        self.__name = name  
        self.__budget = budget  
        self.__expenses = 0  

class BudgetCategory:
    def __init__(self, name, budget):
        self.__name = name
        self.__budget = budget
        self.__expenses = 0

    
    def get_name(self):
        return self.__name

    
    def set_name(self, name):
        self.__name = name

    
    def get_budget(self):
        return self.__budget

    
    def set_budget(self, budget):
        if budget < 0:
            print("Error: Budget cannot be negative.")
        else:
            self.__budget = budget

    
    def get_remaining_budget(self):
        return self.__budget - self.__expenses

class BudgetCategory:
    
    
    def add_expense(self, amount):
        if amount < 0:
            print("Error: Expense cannot be negative.")
        elif amount > self.get_remaining_budget():
            print("Error: Expense exceeds the remaining budget.")
        else:
            self.__expenses += amount
class BudgetCategory:
 
    
    def display_category_summary(self):
        print(f"Category: {self.get_name()}")
        print(f"Allocated Budget: ${self.get_budget()}")
        print(f"Expenses: ${self.__expenses}")
        print(f"Remaining Budget: ${self.get_remaining_budget()}")
