
        
class ROI:
    def __init__(self):
        self.income=0
        self.expenses=0
        self.cashflow=0
        self.investmentscost=0
    def calculate_total_income(self):
        rental = input("Enter your monthly rental income: ")
        laundry = input("Enter your monthly laundry income: ")
        storage = input("Enter your monthly storage income: ")
        misc = input("Enter your monthly misc income: ")
        self.income=int(rental)+int(laundry)+int(storage)+int(misc)
    def calculate_total_expense(self):
        
        taxes = input("Enter your monthly tax expense: ")
        insurance = input("Enter your monthly insurance expense: ")
        utilites = input("Enter your monthly utilities expense (including electric, water, sewer, trash, gas, and landscape): ")
        hoa = input("Enter your monthly HOA expense: ")
        vacancy = input("Enter your monthly vacancy expense: ")
        repairs = input("Enter your monthly repairs expense: ")
        capex = input("Enter your monthly capital expense: ")
        mortgage = input("Enter your monthly mortgage expense: ")
        propertymgt = input("Enter your monthly property management expense: ")
        self.expenses= int(taxes)+int(insurance)+int(utilites)+int(hoa)+int(vacancy)+int(repairs)+int(capex)+int(mortgage)+int(propertymgt)
    def calculate_cash_flow(self): 
        self.cashflow= self.income-self.expenses
    def calculate_total_investment(self):
        down = input("Enter your down payment: ")
        closing = input("Enter your closing costs: ")
        rehab = input("Enter your rehab budget: ")
        misc_other = input("Enter your any other misc costs: ")
        self.investmentscost= int(down)+int(closing)+int(rehab)+int(misc_other)
    def calculate_ROI(self):
        a=self.cashflow*12
        b=self.investmentscost
        return a/b
        
roi=ROI()
print("welcome to the ROI calculator")
print ("please answer questions regarding monthly income")

roi.calculate_total_income()

print ("please answer questions regarding monthly expenses")

roi.calculate_total_expense()

roi.calculate_cash_flow()
    
print ("please answer questions regarding investments cost")

roi.calculate_total_investment()
r=roi.calculate_ROI()
print("your cash on cash ROI is")
print (r*100)     
            