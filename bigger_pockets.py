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
                self.properties[answer1] = {'Totale Monthly Income': 1, 'Income': {'Rental Income': 1, 'Laundry': 1,
                 'Storage': 1, 'Misc': 1}, 
                 'Total Monthly Income': 1, 'Expenses': {'Taxes': 1, 'Insurance': 1, 'Utilities': 1,
                  'HOA Fees': 1, 'Yead Work': 1, 'Vacancy': 1, 'Maintanence': 1, 'Capitol Expenditures': 1,
                   'Property Management': 1,'Mortage': 1}, 'Cash On Cash Return': {'Down Payment': 1,
                    'Closing Costs': 1, 'Repair Costs': 1, 'Misc': 1}, 'Annual Cash Flow': 1, 'ROI': 1}
                print(f'Property {answer1.title()} was added')
                answer2 = input("Would you like to add another propety? <yes or no> ").lower()
                if answer2 == 'quit' or answer2 == 'q':
                    break
                elif answer2 == 'yes':
                    continue
                elif answer2 == 'no':
                    break
                else:
                    print("Your response was not recognized. Please try again")
            elif confirmation == 'no':
                    print(f'Property {answer2} was not added')
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
            elif answer2 == 'rental income':
                print(f'{self.name.title()}\'s propteries {answer2.title()} amount is currently\
 ${self.properties[self.name]["Income"][answer2.title()]}')
                try:
                    answer3 = float(input(f"What would like like to set the {answer2.title()} to? "))
                except ValueError:
                    print('Please enter a number.')
                else:
                    self.properties[self.name][answer2.title()] = answer3
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
            elif answer2 == 'laundry':
                print(f'{self.name.title()}\'s propteries {answer2.title()} amount is currently\
                        ${self.properties[self.name]["Income"][answer2.title()]}')
                try:
                    answer3 = float(input(f"What would like like to set the {answer2.title()} to? "))
                except ValueError:
                    print('Please enter a number.')
                else:
                    self.properties[self.name][answer2.title()] = answer3
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
            elif answer2 == 'storage':
                print(f'{self.name.title()}\'s propteries {answer2.title()} amount is currently\
                        ${self.properties[self.name]["Income"][answer2.title()]}')
                try:
                    answer3 = float(input(f"What would like like to set the {answer2.title()} to? "))
                except ValueError:
                    print('Please enter a number.')
                else:
                    self.properties[self.name][answer2.title()] = answer3
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
            elif answer2 == 'misc':
                print(f'{self.name.title()}\'s propteries {answer2.title()} amount is currently\
                        ${self.properties[self.name]["Income"][answer2.title()]}')
                try:
                    answer3 = float(input(f"What would like like to set the {answer2.title()} to? "))
                except ValueError:
                    print('Please enter a number.')
                else:
                    self.properties[self.name][answer2.title()] = answer3
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
        for value in self.properties[self.name]['Income'].values():
            self.properties['Total Monthly Income'] += value
        print(f'Your new Total Monthly Income for {self.name.title()} is\
 ${self.properties[self.name]["Total Monthly Income"]}')

    def propExpenses(self):
        #Calculates the total monthly expenses and sets the value in the dicitonary
        while True:
            print(self.properties[self.name]['Expenses'])
            answer2 = input("Which property expenses catagory would you like to update? ").lower()
            if answer2 == 'quit' or answer2 == 'q':
                break
            elif answer2 == 'taxes':
                print(f'{self.name.title()}\'s propteries monthly {answer2.title()} amount is currently\
 ${self.properties[self.name]["Expenses"][answer2.title()]}')
                try:
                    answer3 = int(input(f'What would like like to set the {answer2.title()} amount to? '))
                except ValueError:
                    print('Please enter a number.')
                else:
                    self.properties[self.name][answer2.title()] = answer3
                    print(f'Your new {answer2.title()} for {self.name.title()} is\
 ${self.properties[self.name][answer2.title()]}')
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
            elif answer2 == 'insurance':
                print(f'{self.name.title()}\'s propteries monthly {answer2.title()} amount is currently\
 ${self.properties[self.name]["Expenses"][answer2.title()]}')
                try:
                    answer3 = int(input(f'What would like like to set the {answer2.title()} amount to? '))
                except ValueError:
                    print('Please enter a number.')
                else:
                    self.properties[self.name][answer2.title()] = answer3
                    print(f'Your new {answer2.title()} for {self.name.title()} is\
 ${self.properties[self.name][answer2.title()]}')
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
            elif answer2 == 'utilities':
                print(f'{self.name.title()}\'s propteries monthly {answer2.title()} amount is currently\
 ${self.properties[self.name]["Expenses"][answer2.title()]}')
                try:
                    answer3 = int(input(f'What would like like to set the {answer2.title()} amount to? '))
                except ValueError:
                    print('Please enter a number.')
                else:
                    self.properties[self.name][answer2.title()] = answer3
                    print(f'Your new {answer2.title()} for {self.name.title()} is\
 ${self.properties[self.name][answer2.title()]}')
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
            elif answer2 == 'hoa fees':
                print(f'{self.name.title()}\'s propteries monthly {answer2.title()} amount is currently\
 ${self.properties[self.name]["Expenses"][answer2.title()]}')
                try:
                    answer3 = int(input(f'What would like like to set the {answer2.title()} amount to? '))
                except ValueError:
                    print('Please enter a number.')
                else:
                    self.properties[self.name][answer2.title()] = answer3
                    print(f'Your new {answer2.title()} for {self.name.title()} is\
 ${self.properties[self.name][answer2.title()]}')
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
            elif answer2 == 'yard work':
                print(f'{self.name.title()}\'s propteries monthly {answer2.title()} amount is currently\
 ${self.properties[self.name]["Expenses"][answer2.title()]}')
                try:
                    answer3 = int(input(f'What would like like to set the {answer2.title()} amount to? '))
                except ValueError:
                    print('Please enter a number.')
                else:
                    self.properties[self.name][answer2.title()] = answer3
                    print(f'Your new {answer2.title()} for {self.name.title()} is\
 ${self.properties[self.name][answer2.title()]}')
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
            elif answer2 == 'vacancy':
                print(f'{self.name.title()}\'s propteries monthly {answer2.title()} amount is currently\
 ${self.properties[self.name]["Expenses"][answer2.title()]}')
                try:
                    answer3 = int(input(f'What would like like to set the {answer2.title()} amount to? '))
                except ValueError:
                    print('Please enter a number.')
                else:
                    self.properties[self.name][answer2.title()] = answer3
                    print(f'Your new {answer2.title()} for {self.name.title()} is\
 ${self.properties[self.name][answer2.title()]}')
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
            elif answer2 == 'maintenance':
                print(f'{self.name.title()}\'s propteries monthly {answer2.title()} amount is currently\
 ${self.properties[self.name]["Expenses"][answer2.title()]}')
                try:
                    answer3 = int(input(f'What would like like to set the {answer2.title()} amount to? '))
                except ValueError:
                    print('Please enter a number.')
                else:
                    self.properties[self.name][answer2.title()] = answer3
                    print(f'Your new {answer2.title()} for {self.name.title()} is\
 ${self.properties[self.name][answer2.title()]}')
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
            elif answer2 == 'capitol expenditures':
                print(f'{self.name.title()}\'s propteries monthly {answer2.title()} amount is currently\
 ${self.properties[self.name]["Expenses"][answer2.title()]}')
                try:
                    answer3 = int(input(f'What would like like to set the {answer2.title()} amount to? '))
                except ValueError:
                    print('Please enter a number.')
                else:
                    self.properties[self.name][answer2.title()] = answer3
                    print(f'Your new {answer2.title()} for {self.name.title()} is\
 ${self.properties[self.name][answer2.title()]}')
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
            elif answer2 == 'property management':
                print(f'{self.name.title()}\'s propteries monthly {answer2.title()} amount is currently\
 ${self.properties[self.name]["Expenses"][answer2.title()]}')
                try:
                    answer3 = int(input(f'What would like like to set the {answer2.title()} amount to? '))
                except ValueError:
                    print('Please enter a number.')
                else:
                    self.properties[self.name][answer2.title()] = answer3
                    print(f'Your new {answer2.title()} for {self.name.title()} is\
 ${self.properties[self.name][answer2.title()]}')
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
            elif answer2 == 'mortgage':
                print(f'{self.name.title()}\'s propteries monthly {answer2.title()} amount is currently\
 ${self.properties[self.name]["Expenses"][answer2.title()]}')
                try:
                    answer3 = int(input(f'What would like like to set the {answer2.title()} amount to? '))
                except ValueError:
                    print('Please enter a number.')
                else:
                    self.properties[self.name][answer2.title()] = answer3
                    print(f'Your new {answer2.title()} for {self.name.title()} is\
 ${self.properties[self.name][answer2.title()]}')
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
        for value in self.properties[self.name]['Expenses'].values():
            self.properties['Total Monthly Expenses'] += value
        print(f'Your new Total Monthly Expenses for {self.name.title()} are\
 ${self.properties[self.name]["Total Monthly Expenses"]}')

    def propCashFlow(self):
        #Calculates annual cash flow and sets value in the dicitonary
        cash_flow = 12 * (self.properties[self.name]['Total Monthly Income'] - self.properties[self.name]['Totale Monthly Expenses'])
        print(f'Your {self.name} properties annual cash flow is ${cash_flow}')
        self.properties[self.name]['Annual Cash Flow'] = cash_flow

    def propCashOnCashReturn(self):
        #Calculates total investment and ROI as a percentage and sets value in the dicitonary
        while True:
            print(self.properties[self.name]['Cash On Cash Return'])
            answer2 = input("Which property Cash On Cash Return catagory would you like to update? ").lower()
            if answer2 == 'quit' or answer2 == 'q':
                break
            elif answer2 == 'down payment':
                print(f'{self.name.title()}\'s propteries {answer2.title()} amount is currently\
 ${self.properties[self.name]["Cash On Cash Return"][answer2.title()]}')
                try:
                    answer3 = float(input(f'What would like like to set the {answer2.title()} amount to? '))
                except ValueError:
                    print('Please enter a number.')
                else:
                    self.properties[self.name][answer2.title()] = answer3
                    print(f'Your new {answer2.title()} for {self.name.title()} is\
 ${self.properties[self.name][answer2.title()]}')
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
            elif answer2 == 'closing costs':
                print(f'{self.name.title()}\'s propteries {answer2.title()} amount is currently\
 ${self.properties[self.name]["Cash On Cash Return"][answer2.title()]}')
                try:
                    answer3 = float(input(f'What would like like to set the {answer2.title()} amount to? '))
                except ValueError:
                    print('Please enter a number.')
                else:
                    self.properties[self.name][answer2.title()] = answer3
                    print(f'Your new {answer2.title()} for {self.name.title()} is\
 ${self.properties[self.name][answer2.title()]}')
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
            elif answer2 == 'repair budget':
                print(f'{self.name.title()}\'s propteries {answer2.title()} amount is currently\
 ${self.properties[self.name]["Cash On Cash Return"][answer2.title()]}')
                try:
                    answer3 = float(input(f'What would like like to set the {answer2.title()} amount to? '))
                except ValueError:
                    print('Please enter a number.')
                else:
                    self.properties[self.name][answer2.title()] = answer3
                    print(f'Your new {answer2.title()} for {self.name.title()} is\
 ${self.properties[self.name][answer2.title()]}')
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
            elif answer2 == 'misc':
                print(f'{self.name.title()}\'s propteries {answer2.title()} amount is currently\
 ${self.properties[self.name]["Cash On Cash Return"][answer2.title()]}')
                try:
                    answer3 = float(input(f'What would like like to set the {answer2.title()} amount to? '))
                except ValueError:
                    print('Please enter a number.')
                else:
                    self.properties[self.name][answer2.title()] = answer3
                    print(f'Your new {answer2.title()} for {self.name.title()} is\
 ${self.properties[self.name][answer2.title()]}')
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
        self.properties[self.name]['ROI'] = 100 * (self.properties[self.name]['Annual Cash Flow']/self.properties[self.name]['Total Investment'])

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
                    elif answer in self.properties.keys():
                        print(self.properties[answer])
                        self.name = answer
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