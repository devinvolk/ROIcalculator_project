class FourSquareMethod():
    def __init__(self):
        self.properties = {} #key = property name, value = dicitonary of income,$ expenses,$ cashflow,$ and ROI,$
        self.name = ""
    
    def addProp(self):
        #adds a property to the dictionary with default attributes
        while True:
            answer1 = input("What would you like to name this property? ").lower()
            confirmation = input(f'Does property name {answer1.title()} look correct? <yes or no> ').lower()
            if confirmation == 'quit' or confirmation == 'q':
                break
            elif confirmation == 'yes':
                self.properties[answer1.title()] = {'Total Monthly Income': 0, 'Income': {'Rental Income': 0, 'Laundry': 0,
                 'Storage': 0, 'Misc': 0}, 
                 'Total Monthly Expenses': 0, 'Expenses': {'Taxes': 0, 'Insurance': 0, 'Utilities': 0,
                  'HOA Fees': 0, 'Yead Work': 0, 'Vacancy': 0, 'Maintanence': 0, 'Capitol Expenditures': 0,
                   'Property Management': 0,'Mortage': 0}, 'Cash On Cash Return': {'Down Payment': 0,
                    'Closing Costs': 0, 'Repair Costs': 0, 'Misc': 0}, 'Annual Cash Flow': 0, 'Total Investment': 0, 'ROI': 0}
                print(f'Property {answer1.title()} was added')
                answer2 = input("Would you like to add another property? <yes or no> ").lower()
                if answer2 == 'quit' or answer2 == 'q':
                    break
                elif answer2 == 'yes':
                    continue
                elif answer2 == 'no':
                    break
                else:
                    print("Your response was not recognized. Please try again")
            elif confirmation == 'no':
                    print(f'Property {answer1.title()} was not added')
                    continue
            else:
                print("Your response was not recognized. Please try again")

    def removeProp(self):
        #removes a property from the dictionary
        while True:
            print(self.properties.keys())
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
        #Updates the dicitonary monthly income for the property and calculates total monthy income for that property
        while True:
            print(self.properties[self.name]['Income'])
            answer2 = input("Which property income catagory would you like to update? ").lower()
            if answer2 == 'quit' or answer2 == 'q':
                break
            elif answer2.title() in self.properties[self.name]['Income'].keys():
                print(f'{self.name.title()}\'s propteries {answer2.title()} amount is currently\
 ${self.properties[self.name]["Income"][answer2.title()]}')
                try:
                    answer3 = float(input(f"What would like like to set the {answer2.title()} to? "))
                except ValueError:
                    print('Please enter a number.')
                else:
                    self.properties[self.name]['Income'][answer2.title()] = answer3
                    print(f'Your new {answer2.title()} for {self.name.title()} is\
 ${self.properties[self.name]["Income"][answer2.title()]}')
                    answer4 = input("Would you like to update another income catagory? <yes or no> ").lower()
                    if answer4 == 'quit' or answer4 == 'q':
                        break
                    elif answer4 == 'yes':
                        continue
                    elif answer4 == 'no':
                        break
                    else:
                        print("Your response was not recognized. Please try again")
                        continue
            else:
                print("Your response was not recognized. Please try again")
                continue
        for amount in self.properties[self.name]['Income'].values():
            self.properties[self.name]['Total Monthly Income'] += amount
        print(f'Your new Total Monthly Income for {self.name.title()} is\
 ${self.properties[self.name]["Total Monthly Income"]}')

    def propExpenses(self):
        #Calculates the total monthly expenses and sets the value in the dicitonary
        print(f'Your Total Monthly Expenses for {self.name.title()} are\
 ${self.properties[self.name]["Total Monthly Expenses"]}')
        while True:
            print(self.properties[self.name]['Expenses'])
            answer2 = input("Which property expenses catagory would you like to update? ").lower()
            if answer2 == 'quit' or answer2 == 'q':
                break
            elif answer2.title() in self.properties[self.name]['Expenses'].keys():
                print(f'{self.name.title()}\'s propteries {answer2.title()} amount is currently\
 ${self.properties[self.name]["Expenses"][answer2.title()]}')
                try:
                    answer3 = float(input(f"What would like like to set the {answer2.title()} to? "))
                except ValueError:
                    print('Please enter a number.')
                else:
                    self.properties[self.name]['Expenses'][answer2.title()] = answer3
                    print(f'Your new {answer2.title()} for {self.name.title()} is\
 ${self.properties[self.name]["Expenses"][answer2.title()]}')
                    answer4 = input("Would you like to update another expenses catagory? <yes or no> ").lower()
                    if answer4 == 'quit' or answer4 == 'q':
                        break
                    elif answer4 == 'yes':
                        continue
                    elif answer4 == 'no':
                        break
                    else:
                        print("Your response was not recognized. Please try again")
                        continue
            else:
                print("Your response was not recognized. Please try again")
        for amount in self.properties[self.name]['Expenses'].values():
            self.properties[self.name]['Total Monthly Expenses'] += amount
        print(f'Your new Total Monthly Expenses for {self.name.title()} are\
 ${self.properties[self.name]["Total Monthly Expenses"]}')

    def propCashFlow(self):
        #Calculates annual cash flow and sets value in the dicitonary
        cash_flow = 12 * (self.properties[self.name]['Total Monthly Income'] - self.properties[self.name]['Total Monthly Expenses'])
        print(f'Your {self.name} properties annual cash flow is ${cash_flow}')
        self.properties[self.name]['Annual Cash Flow'] = cash_flow

    def propCashOnCashReturn(self):
        #Calculates total investment and ROI as a percentage and sets value in the dicitonary
        print(f'{self.name.title()}\'s Return On Investment is currently ${self.properties[self.name]["ROI"]}')
        while True:
            print(self.properties[self.name]['Cash On Cash Return'])
            answer2 = input("Which property Cash On Cash Return catagory would you like to update? ").lower()
            if answer2 == 'quit' or answer2 == 'q':
                break
            elif answer2.title() in self.properties[self.name]['Cash On Cash Return'].keys():
                print(f'{self.name.title()}\'s propteries {answer2.title()} amount is currently\
 ${self.properties[self.name]["Cash On Cash Return"][answer2.title()]}')
                try:
                    answer3 = float(input(f"What would like to set the {answer2.title()} to? "))
                except ValueError:
                    print('Please enter a number.')
                else:
                    self.properties[self.name]['Cash On Cash Return'][answer2.title()] = answer3
                    print(f'Your new {answer2.title()} for {self.name.title()} is\
 ${self.properties[self.name]["Cash On Cash Return"][answer2.title()]}')
                    answer4 = input("Would you like to update another Cash On Cash Return catagory? <yes or no> ").lower()
                    if answer4 == 'quit' or answer4 == 'q':
                        break
                    elif answer4 == 'yes':
                        continue
                    elif answer4 == 'no':
                        break
                    else:
                        print("Your response was not recognized. Please try again")
                        continue
            else:
                print("Your response was not recognized. Please try again")
        for amount in self.properties[self.name]['Cash On Cash Return'].values():
            self.properties[self.name]['Total Investment'] += amount
        self.properties[self.name]['ROI'] = 100 * (self.properties[self.name]['Annual Cash Flow']/self.properties[self.name]['Total Investment'])
        print(f'{self.name.title()}\'s new Return On Investment is currently {self.properties[self.name]["ROI"]}%')

    def runner(self):
        while True:
            print("Enter 'quit' at any time to exit")
            answer = input("What would you like to do? Enter: <add new property, see existing properties, or remove a property> ").lower()
            if answer == 'quit' or answer == 'q':
                break
            elif answer == 'add new property':
                self.addProp()
            elif answer == 'see existing properties':
                while True:
                    print(self.properties.keys())
                    answer = input("What property would you like to view? ").lower()
                    if answer == 'quit' or answer == 'q':
                        break
                    elif answer.title() in self.properties.keys():
                        print(f'Total Monthly Income: ${self.properties[answer.title()]["Total Monthly Income"]}', f'\nTotal Monthly Expenses: ${self.properties[answer.title()]["Total Monthly Expenses"]}',
                        f'\nAnnual Cash Flow: ${self.properties[answer.title()]["Annual Cash Flow"]}', f'\nTotal Investment: ${self.properties[answer.title()]["Total Investment"]}', f'\nROI: ${self.properties[answer.title()]["ROI"]}')
                        self.name = answer.title()
                        while True:
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
                    else:
                        print("Your input was not recognized. Please try again")
            elif answer == 'remove a property':
                self.removeProp()
            else:
                print("Your input was not recognized. Please try again")

user1 = FourSquareMethod()
user1.runner()