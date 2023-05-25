from ROI import Income,Expense,Cash_flow,Cash_on_cash_ROI

print("welcome to the ROI calculator")
print ("please answer questions regarding monthly income")
rental = input("Enter your monthly rental income: ")
laundry = input("Enter your monthly laundry income: ")
storage = input("Enter your monthly storage income: ")
misc = input("Enter your monthly misc income: ")
i=Income(int(rental),int(laundry),int(storage),int(misc)).calculate_total_income()

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
e=Expense(int(taxes),int(insurance),int(util),int(hoa),int(vacancy),int(repairs),int(capex),int(mortgage),int(propertymgt)).calculate_total_expense()

c=Cash_flow(int(i),int(e)).calculate_cash_flow()

print ("please answer questions regarding investments cost")
down = input("Enter your down payment: ")
closing = input("Enter your closing costs: ")
rehab = input("Enter your rehab budget: ")
misc_other = input("Enter your any other misc costs: ")
r=Cash_on_cash_ROI(int(c),int(down),int(closing),int(rehab),int(misc_other)).calculate_ROI()
print("your cash on cash ROI is")
print (r*100)