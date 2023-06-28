
        
class ROI:
    def __init__(self):
        self.income=0
        self.expenses=0
        self.cashflow=0
        self.investmentscost=0
    def calculate_total_income(self,rental,laundry,storage,misc):
        self.income=(rental+laundry+storage+misc)
    def calculate_total_expense(self,taxes,insurance,utilites,hoa,vacancy,repairs,capex,mortgage,propertymgt):
        self.expenses= taxes+insurance+utilites+hoa+vacancy+repairs+capex+mortgage+propertymgt
    def calculate_cash_flow(self): 
        self.cashflow= self.income-self.expenses
    def calculate_total_investment(self,down_payment,closing_cost,rehab_budget,misc_other):
        self.investmentscost= down_payment+closing_cost+rehab_budget+misc_other
    def calculate_ROI(self):
        a=self.cashflow*12
        b=self.investmentscost
        return a/b
        
roi=ROI()
print("welcome to the ROI calculator")
print ("please answer questions regarding monthly income")
rental = input("Enter your monthly rental income: ")
laundry = input("Enter your monthly laundry income: ")
storage = input("Enter your monthly storage income: ")
misc = input("Enter your monthly misc income: ")
roi.calculate_total_income(int(rental),int(laundry),int(storage),int(misc))

print ("please answer questions regarding monthly expenses")
taxes = input("Enter your monthly tax expense: ")
insurance = input("Enter your monthly insurance expense: ")
util = input("Enter your monthly utilities expense (including electric, water, sewer, trash, gas, and landscape): ")
hoa = input("Enter your monthly HOA expense: ")
vacancy = input("Enter your monthly vacancy expense: ")
repairs = input("Enter your monthly repairs expense: ")
capex = input("Enter your monthly capital expense: ")
mortgage = input("Enter your monthly mortgage expense: ")
propertymgt = input("Enter your monthly property management expense: ")
roi.calculate_total_expense(int(taxes),int(insurance),int(util),int(hoa),int(vacancy),int(repairs),int(capex),int(mortgage),int(propertymgt))

roi.calculate_cash_flow()
    
print ("please answer questions regarding investments cost")
down = input("Enter your down payment: ")
closing = input("Enter your closing costs: ")
rehab = input("Enter your rehab budget: ")
misc_other = input("Enter your any other misc costs: ")
roi.calculate_total_investment(int(down),int(closing),int(rehab),int(misc_other))
r=roi.calculate_ROI()
print("your cash on cash ROI is")
print (r*100)     
            