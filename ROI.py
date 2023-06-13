
        
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
            