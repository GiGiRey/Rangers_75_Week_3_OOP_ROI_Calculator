import os
os.system('cls' if os.name == 'nt' else 'clear')

# Calculation = 
# ((income - expenses)*12) / Investment
# 
# Investment 

class Cart():
  
    def __init__(self, investment = 0, income = 0, expenses = 0, roi = 0.0):
        self.investment = investment
        self.income = income
        self.expenses = expenses
        self.roi = roi
   
    def addInvestment(self):

        investment = input("What is your investment in this property (in whole numbers)? ")
        if investment.isalpha():
            investment = input("Please enter a valid dollar amount: ")
        if int(investment) < 0:
            investment = input("Please enter a valid dollar amount: ")
        else:
            self.investment = investment
            print(f"The following investment amount was added: {self.investment}")
            print()

        income = input("What is your anticipated monthly income from this property? ")
        if income.isalpha():
            income = input("Please enter a valid dollar amount: ")
        if int(income) < 0:
            income = input("Please enter a valid dollar amount: ")
        else:
            self.income = income
            print(f"The following income amount was added: {self.income}")
            print()


        expenses = input("What are your anticipated monthly expenses for this property? ")
        if expenses.isalpha():
            expenses = input("Please enter a valid dollar amount: ")
        if int(expenses) < 0:
            expenses = input("Please enter a valid dollar amount: ")
        else:
            self.expenses = expenses
            print(f"The following expense amount was added: {self.expenses}")
        
        
        if int(self.investment) <=0:
            print("Investment is $0")
            self.roi = ((int(self.income) - int(self.expenses)) * 12) / .01
            print(f"The projected ROI for this property is {self.roi}%")
            print()

        elif int(self.investment) > 0 and int(self.income) >= 0 and int(self.expenses) >= 0: 
            roi = ((int(self.income) - int(self.expenses)) * 12) / int(self.investment)
            print(f"The projected ROI for this property is {self.roi}%")
            print()
            
        print("Thank you for using the Wealth Builder app!")
        print("What would you like to do next?")

def run():

    my_portfolio = Cart({})
    
    print("Welcome to Real Estate Wealth Builder!")
    print("What would you like to do today?")
    
    while True:        
        print('''
        C: Calculate property ROI
        Q: Quit
        ''')
        response = input("Enter choice here: ")
        
        if response.lower() not in ["c","q"]: #membership check
            response = input('Please enter a VALID choice: ')     
        
        if response.lower() == "q":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        
        elif response.lower() == 'c':
               my_portfolio.addInvestment()
               
run()

