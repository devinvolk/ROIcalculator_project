class FourSquareMethod():
    def __init__(self):
        self.properties = {} #key = property name, value = dicitonary of income,$ expenses,$ cashflow,$ and ROI,$
    
    def addProp(self):
        #adds a property to the dictionary
        while True:
            answer1 = input("What would you like to name this property? ").lower()
            confirmation = input(f'Does property name {answer1.title()} look correct? <yes or no> ').lower()
            if confirmation == 'quit' or confirmation == 'q':
                break
            elif confirmation == 'yes':
                self.properties[answer1] = {'Income': None, 'Expenses': None, 'Cash Flow': None, 'ROI': None}
                print(f'Property {answer1.title()} was added')
                answer2 = input("Would you like to delete another propety? <yes or no> ").lower()
                if answer2 == 'quit' or answer2 == 'q':
                    break
                elif answer2 == 'yes':
                    continue
                elif answer2 == 'no':
                    break
                else:
                    print("Your response was not recognized")
            elif confirmation == 'no':
                    print(f'Property {answer2} was not deleted')
                    continue
            else:
                print("Your response was not recognized")

    def removeProp(self):
        #removes a property from the dictionary
        while True:
            print(self.properties.key())
            answer1 = input("Which property would you like to delete? ").lower()
            if answer1 == 'quit' or answer1 == 'q':
                break
            confirmation = input(f'Are you sure you want to delete {answer1}? <yes or no> ').lower()
            if confirmation == 'quit' or confirmation == 'q':
                break
            elif confirmation == 'yes':
                del self.properties[answer1]
                print(f'Property {answer1} was deleted')
                answer2 = input("Would you like to delete another propety? <yes or no> ")
                if answer2 == 'quit' or answer2 == 'q':
                    break
                elif answer2 == 'yes':
                    continue
                elif answer2 == 'no':
                    break
                else:
                    print("Your response was not recognized")
            elif confirmation == 'no':
                print(f'Property {answer1} was not deleted')
                continue
            else:
                print("Your response was not recognized")

    def propIncome(self):
        while True:
            answer1 = input("What would you like to update this properties income? <yes or no> ").lower()
            if answer1 == 'quit' or answer1 == 'q':
                break
            elif answer1 == 'yes':
                return
            elif answer1 == 'no':
                return
            else:
                print("Your response was not recognized")
        #returns total monthly income and sets value in the dicitonary
        #rental income
        #laundry
        #storage
        #misc

    def propExpenses(self):
        #returns total monthly expenses and sets value in the dicitonary
        while True:
            answer1 = input("What would you like to update this properties expenses? <yes or no> ").lower()
            if answer1 == 'quit' or answer1 == 'q':
                break
            elif answer1 == 'yes':
                return
            elif answer1 == 'no':
                return
            else:
                print("Your response was not recognized")
        #taxes
        #insurance
        #water/sewage
        #garbage
        #electric 
        #gas
        #HOA Fees
        #lawn/snow
        #vacancy (5% of rental income)
        #repairs
        #Capitol Expenditures
        #Property Management
        #Mortgage

    def propCashFlow(self):
        #reutrns annual cash flow and sets value in the dicitonary
        while True:
            answer1 = input("What would you like to update this properties cash flow? <yes or no> ").lower()
            if answer1 == 'quit' or answer1 == 'q':
                break
            elif answer1 == 'yes':
                return
            elif answer1 == 'no':
                return
            else:
                print("Your response was not recognized")
        #12*(income() - expenses())

    def propCashOnCashReturn(self):
        #returns ROI as a percentage and sets value in the dicitonary
        while True:
            answer1 = input("What would you like to update this properties cash on cash return? <yes or no> ").lower()
            if answer1 == 'quit' or answer1 == 'q':
                break
            elif answer1 == 'yes':
                return
            elif answer1 == 'no':
                return
            else:
                print("Your response was not recognized")
        #annual cash flow/total investment = ROI
        #calculates the total investment
        #down payment
        #closing costs
        #repair budget
        #misc other

    def runner(self):
        while True:
            print("Enter 'quit' at any time to exit")
            answer = input("What would you like to do? Enter: <add new property, see existing properties> ").lower()
            if answer == 'quit' or answer == 'q':
                break
            elif answer == 'add new property':
                self.addProp()
            elif answer == 'see existing property':
                while True:
                    print(self.properties.keys())
                    answer = input("What property would you like to view? ").lower()
                    if answer == 'quit' or answer == 'q':
                        break
                    elif answer in self.properties.keys():
                        print(self.properties[answer])
                        answer1 = input("What would you like to do? Enter: <update property income, update property expenses,\
                            view property cash flow, or update cash on cash return> ").lower()
                        if answer1 == 'quit' or answer1 == 'q':
                            break
                    elif answer1 == 'update property income':
                        self.propIncome()
                    elif answer1 == 'update property expenses':
                        self.propExpenses()
                    elif answer1 == 'view property cash flow':
                        self.propCashFlow()
                    elif answer1 == 'update cash on cash return':
                        self.propCashOnCashReturn()
                    else:
                        print("Your input was not recognized. Please try again")

user1 = FourSquareMethod()