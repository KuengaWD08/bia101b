import pyttsx3
engine = pyttsx3.init()

def speak(text):# setting for speaking some of  the users input and questions
    engine.setProperty('rate',300)
    voices= engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()

print("Welcome to KuenTech, this application is used to calculate your Personal income tax. To begin, your information will be completely confidential. Note that all information given should be on annual basis")
speak("Welcome to KuenTech, this application is used to calculate your Personal income tax. your information will be completely confidential. Note that all information given should be on annual basis")
   

class Employee:
    def __init__(self, name, age,position,Organization_type):# this class will get the information of the user
        self.name = name
        self.age = age
        self.position = position
        self.Organization_type = Organization_type

class SalaryIncome:
    def __init__(self, basic_salary, bonus, commission, leave_encashment, allowances=0):# this class is uesd to collect information on users salary including other income related to salary
        self.basic_salary = basic_salary
        self.bonus = bonus
        self.commission = commission
        self.leave_encashment = leave_encashment
        self.allowances = allowances
        self.total_salary_income = basic_salary + bonus + commission + leave_encashment + allowances

class Dividendincome:
    def __init__(self,dividend_income):#records dividend income
        self.dividend_income = dividend_income

class other_income: #records other incomes
    def __init__(self,Other_income):
        self.Other_income = Other_income
               
def get_user_input():
    # this function will ask user for their information upon personal detail and salary base information
    speak("Please enter your name: ")
    name = str(input("Please enter your name: "))
    
    speak("Please type in your age: ")
    age = int(input("Please type in your age: "))
    
    speak("Enter your employee type")
    position = input("Enter your employee type (Regular or Contract):").lower()
    
    speak("Enter your organization's type")
    Organization_type = input("Enter your organization's type: (Government or Private):").lower()
    
    speak("Enter your basic salary:")
    basic_salary = float(input("Enter your basic salary: "))
    
    speak("Did you receive bonus?")
    get_bonus = input("Did you receive bonus? (yes/no): ").lower()
    speak("Enter your  bonus amount:") if get_bonus == "yes" else 0 # this code will run only if user type "yes"
    bonus = float(input("Enter your  bonus amount: ")) if get_bonus == "yes" else 0
    
    speak("Did you  receive commission?")
    get_commission = input("Did you  receive commission? (yes/no): ").lower()
    speak("Enter your  commission amount: ") if get_commission == "yes" else 0 # this code will run only if user type "yes"
    commission = float(input("Enter your  commission amount: ")) if get_commission == "yes" else 0
    
    speak("Did you  receive leave encashment?")
    get_leave_encashment = input("Did you  receive leave encashment? (yes/no): ").lower()
    speak("Enter your leave encashment amount : ") if get_leave_encashment == "yes" else 0 # this code will run only if user type "yes"
    leave_encashment = float(input("Enter your leave encashment amount : ")) if get_leave_encashment == "yes" else 0
    
    speak("Did you receive allowances?")
    get_allowances = input("Did you receive allowances? (yes/no): ").lower()
    speak("Enter your allowances amount : ") if get_allowances == "yes" else 0 # this code will run only if user type "yes"
    allowances = float(input("Enter your allowances amount : ")) if get_allowances == "yes" else 0
    
    return Employee(name, age,position,Organization_type), SalaryIncome(basic_salary, bonus, commission, leave_encashment, allowances)

Employee, salary_income = get_user_input()

class RentalIncome: # this class is used to get information about rental based income
    def __init__(self,land,building,house,factory_building,warehouse,other_structures):
        self.land = land
        self.building = building
        self.house = house
        self.factory_building = factory_building
        self.warehouse = warehouse
        self.other_structures = other_structures
        self.total_rental_income = land + building + house + factory_building + warehouse + other_structures

def get_rental_input(): # this function gets input from user about rental information
    speak("Did you  receive income from land if you happen to own?")
    get_land = input("Did you  receive income from land that you own?(yes/no): ").lower()
    speak("Enter the amount: ")if get_land == "yes" else 0
    land = float(input("Enter the amount: ")) if get_land == "yes" else 0 # this code will run only if user type "yes"
    
    speak("Did you receive income from building if you happen to own ?")
    get_building = input("Did you receive income from buildings if you happen to own? (yes/no): ").lower()
    speak('Enter the amount: ')if get_building == "yes" else 0 # this code will run only if user type "yes"
    buildiing= float(input(" Enter the amount: ")) if get_building == "yes" else 0
    
    speak("Did you receive income from house if you happen to own ")
    get_house= input("Did you  receive income from house if happen to own  (yes/no): ").lower()
    speak('Enter the amount: ')if get_house == "yes" else 0 # this code will run only if user type "yes"
    house = float(input("Enter the amount: ")) if get_house == "yes" else 0
    
    speak('Did you receive income from factories if you happen to own')
    get_factory_building = input("Did you receive income from factories if you happen to own? (yes/no): ").lower()
    speak("Enter the amount") if get_factory_building == "yes" else 0 # this code will run only if user type "yes"
    factory_building = float(input("Enter the amount: ")) if get_factory_building == "yes" else 0

    speak("Did you receive income from warehouse if you happen to own")
    get_warehouse= input("Did you  receive income from warehouse  if you happen own? (yes/no): ").lower()
    speak("Enter the amount") if get_warehouse == "yes" else 0 # this code will run only if user type "yes"
    warehouse = float(input("Enter the amount: ")) if get_warehouse == "yes" else 0
    
    speak("Did you receive income from other structures if you happen to own")
    get_other_structures = input("Do you  receive income from other structures if you own? (yes/no): ").lower()
    speak("Enter the amount") if get_other_structures == "yes" else 0 # this code will run only if user type "yes"
    other_structures  = float(input("Enter the amount:")) if get_other_structures == "yes" else 0

    return RentalIncome(land,buildiing,house,factory_building,warehouse,other_structures)

RentalIncome = get_rental_input()

def get_ot_input(): #gets input from user upon dividend and other income
    speak('Did you recieve Dividend income')
    get_dividend_income = input("Did you  receive  Dividend income? (yes/no): ").lower()
    speak("Enter the amount") if get_dividend_income == "yes" else 0 # this code will run only if user type "yes"
    dividend_income= float(input("Enter the amount:")) if get_dividend_income == "yes" else 0

    speak("Did you receive any other income?")
    get_Other_income = input("Did you  receive any other income ? (yes/no): ").lower()
    speak("Enter the amount") if get_Other_income == "yes" else 0 # this code will run only if user type "yes"
    Other_income  = float(input("Enter the amount:")) if get_Other_income == "yes" else 0

    return Dividendincome(dividend_income), other_income(Other_income)

Dividendincome,other_income = get_ot_input()

total_gross_income = salary_income.total_salary_income + RentalIncome.total_rental_income + Dividendincome.dividend_income + other_income.Other_income
print("Your Gross income is :", total_gross_income) # this show the gross income before considering deductions
text1="Your Gross income is :"+str(total_gross_income)
engine.say(text1)

class Deductibles: #collect deduction information
    def __init__(self, nppf, children_expense, gis):   
        self.nppf = nppf
        self.children_expense = children_expense
        self.gis = gis

    def salary_deductions(self): # deduction for salary income
        total_salary_deductions = self.nppf + self.children_expense + self.gis
        return total_salary_deductions

    def get_salary_input():
        nppf = 0  
        children_expense = 0
        gis = 0
         
        
        if Employee.position == "Contract".lower() and Employee.Organization_type == "Government".lower():
            nppf = 0 # this code will run only if user inputs contract and government since they are not eligible
            print("Since your are contract employee working under government, you are not eligible for pension scheme deduction")
            speak("Since your are contract employee working under government, you are not eligible for pension scheme deduction")
        else: # if they type other input then this will run
            speak("Did you receive NPPF deduction")
            get_nppf = input("Did you receive NPPF deduction? (yes/no): ").lower()
            speak("Enter the amount") if get_nppf == "yes" else 0
            nppf = float(input("Enter the amount:")) if get_nppf == "yes" else 0
        
        speak("Do you have any children who are eligible for an education allowance?")
        get_children_expense = input("Do you have any children who are eligible for an education allowance? (yes/no): ").lower()
        speak("Enter the amount") if get_children_expense == "yes" else 0 # this code will run only if user type "yes"
        children_expense = float(input("Enter the amount (The allowance is provided up to a max of Nu.350000 per child):")) if get_children_expense == "yes" else 0
     
        speak("Are you eligible to receive GIS deduction")
        get_gis = input("Are you eligible to receive GIS deductions? (yes/no): ").lower()
        speak("Enter the amount") if get_gis == "yes" else 0 # this code will run only if user type "yes"
        gis = float(input("Enter the amount:")) if get_gis == "yes" else 0

        return Deductibles(nppf, children_expense, gis)
    
    def rental_deductions(self):
        total_rental_deductions = RentalIncome.total_rental_income * 0.2
        return total_rental_deductions # calculate deduction for rental income(rental income * 20%)
    
    def dividend_deductions(self): #deduction given on dividen income only if they type yes
        if Dividendincome.dividend_income == "yes":
            total_dividend_deductions = 30000
            
        else: # if they dont get dividen income then there will be no deductions
            total_dividend_deductions = 0
        return total_dividend_deductions 
    
         
    
    def other_deductions(self):
        total_other_deductions = other_income.Other_income * 0.3
        return total_other_deductions # calculate deduction for other income(other income * 30%)

deductibles = Deductibles.get_salary_input()
total_deductions = deductibles.salary_deductions()
total_rental_deductions = deductibles.rental_deductions()
total_dividend_deductions = deductibles.dividend_deductions()
total_other_deductions = deductibles.other_deductions()

total_deductions_amount = total_deductions + total_other_deductions + total_rental_deductions + total_other_deductions + total_dividend_deductions
print("you total deduction amount is:",total_deductions_amount) # compile all the deduction and make a total deduction amount
text2= "your total deduction amount is"+ str(total_deductions_amount)
engine.say(text2)

Gross_Taxable_income = total_gross_income - total_deductions_amount # gross income - total deduction(which will give gross taxable income)
print("Your Gross Taxable income:",Gross_Taxable_income) 
text3="Your Gross Taxable  income is :"+str(Gross_Taxable_income)
engine.say(text3)

def calculate_tax_rate(taxable_income): # to calculate your tax rate
        if taxable_income <= 300000:
            return 0
        elif taxable_income <= 400000:
            return 0.10 * taxable_income
        elif taxable_income <= 650000:
            return 0.15 * taxable_income
        elif taxable_income <= 1000000:
            return 0.20 * taxable_income
        elif taxable_income <= 1500000:
            return 0.25 * taxable_income - 1000000
        else:
            return 0.30 * taxable_income 
# Calculate tax payable
tax_payable = calculate_tax_rate(Gross_Taxable_income)
print(" your Taxable income is:", tax_payable) #calculate taxable income
text4="Your Taxable income is :"+str(tax_payable)
engine.say(text4)

Net_taxable_income = Gross_Taxable_income - tax_payable
print("your Net taxable income:", Net_taxable_income) # calculating net taxable income by deducting taxable income from gross taxable income
text5="Your Net taxable income is :"+str(Net_taxable_income)
engine.say(text5)

speak("Thank you for using our services")
print("Thank you for using our services")

exit() # exits the code













  






    
        
        
        


        
        
      