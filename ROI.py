class Income:
    def __init__(self, rental, laundry, storage, misc):
        self.rental = rental
        self.laundry = laundry
        self.storage = storage
        self.misc = misc
        
    def calculate_total_income(self):
        return self.rental+self.laundry+self.storage+self.misc
class Expense:
    def __init__(self, taxes, insurance, util, hoa, vacancy, repairs, capex, mortgage, propertymgt):
        self.taxes = taxes
        self.insurance = insurance
        self.util = util
        self.hoa = hoa
        
        self.vacancy = vacancy
        self.repairs = repairs
        self.capex = capex
        self.mortgage = mortgage
        self.propertymgt = propertymgt
        
    def calculate_total_expense(self):
        return self.taxes+self.insurance+self.util+self.hoa+self.vacancy+self.repairs+self.capex+self.mortgage+self.propertymgt
class Cash_flow:
    def __init__(self,income,expense):
        self.income=income
        self.expense=expense
    def calculate_cash_flow(self): 
        return self.income-self.expense
class Cash_on_cash_ROI:
    def __init__(self, monthly_cash_flow, down_payment, closing_cost, rehab_budget, misc_other):
        self.monthly_cash_flow = monthly_cash_flow
        self.down_payment = down_payment
        self.closing_cost = closing_cost
        self.rehab_budget = rehab_budget
        self.misc_other = misc_other
        
    def calculate_total_investment(self):
        return self.down_payment+self.closing_cost+self.rehab_budget+self.misc_other
    def annual_cash_flow(self):
        return self.monthly_cash_flow*12
    def calculate_ROI(self):
        a=self.annual_cash_flow()
        b=self.calculate_total_investment()
        return a/b
        
        