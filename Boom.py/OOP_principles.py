def d():
    print('-' * 75)

class BudgetCategory:
    def __init__(self, name, budget):
        self.__budget = budget
        self.__name = name
        self.__expenses = []

    def get_name(self):
        return self.__name

    def add_expense(self, amount, expenses):
        if isinstance(amount, (int, float)) and amount > 0:
            self.__expenses.append(amount)
        else:
            print("Expense amount must be a positive number")
    
    def get_budget(self):
        total_expenses = sum(self.expenses)
        return self.__budget - total_expenses   
    
    def set_name(self, name):
        if isinstance(name, str) and name:
            self.__name = name
        else:
            print("Category name must be a non-empty string")

    def set_budget(self, budget):
        if isinstance(budget, (int, float)) and budget >= 0:
            self.__budget = budget
        else:
            print("Budget must be a positive number")

    def amount_left(self):   #Amount left over after budget?
        total_amount = sum(self.__expenses)
        return self.__budget - total_amount


    def display_category_summary(self):
        total_expenses = sum(self.__expenses)
        print(f"Category: {self.__name}")
        print(f"Budget: ${self.__budget}")
        print(f"Total Expenses: ${total_expenses}")
        print(f"Amount Left: ${self.amount_left()}")  
    


food_category = BudgetCategory("Food", 500)
food_category.add_expense(100, 'expenses')
food_category.add_expense(50, 'expenses')
food_category.display_category_summary()
d()
food_category.set_name("Groceries")
food_category.set_budget(600)
food_category.add_expense(200, 'expenses')
food_category.display_category_summary()
d()
bills_category = BudgetCategory("Internet", 100)
bills_category.set_name('Internet')
bills_category.set_budget(100)
bills_category.add_expense(50, 'expenses')
bills_category.add_expense(50, 'expenses')
bills_category.display_category_summary()
d()
phone = BudgetCategory('bills', 50)
phone.set_name('Phone Bill')
phone.set_budget(100)
phone.add_expense(25, 'expenses')
phone.add_expense(25, 'expenses')
phone.display_category_summary()