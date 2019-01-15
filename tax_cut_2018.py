filing_status = int(input("What is your filing status? (Choose single (1) or married (2)) "))
income = int(input("What is your net taxable income per pay period? "))
payperiods = int(input("How many pay periods do you have? "))

def single_filer(income, payperiods):
  old1 = .1
  old2 = .15
  old3 = .25
  old4 = .28
  old5 = .33
  old6 = .35
  old7 = .396
  new1 = .18
  new2 = .12
  new3 = .22
  new4 = .24
  new5 = .32
  new6 = .35
  new7 = .37
  total_income = income * payperiods
  if total_income <= 9525:
    return "No change"
  
  elif total_income <=82500:
    yr_tax_savings = (total_income - 9525)* (old3 - new3)
    period_tax_savings = yr_tax_savings/payperiods
    x = str(round(yr_tax_savings))
    y = str(round(period_tax_savings, 2))
    return "Under the new tax plan, your yearly income will change by $" + x + " and $" + y + " per pay period" 
  
  elif total_income <=93700:
    yr_tax_savings = (82500 - 9525)* (old3 - new3) + (total_income - 82500)*(old3 - new4)
    period_tax_savings = yr_tax_savings/payperiods
    x = str(round(yr_tax_savings))
    y = str(round(period_tax_savings, 2))
    return "Under the new tax plan, your yearly income will change by $" + x + " and $" + y + " per pay period" 
  
  elif total_income <=157000:
    yr_tax_savings = (82500 - 9525)* (old3 - new3) + (93700 - 82500)*(old3 - new4) + (total_income - 93700)*(old4 - new4)
    period_tax_savings = yr_tax_savings/payperiods
    x = str(round(yr_tax_savings))
    y = str(round(period_tax_savings, 2))
    return "Under the new tax plan, your yearly income will change by $" + x + " and $" + y + " per pay period" 
  
  elif total_income <=195450:
    yr_tax_savings = (82500 - 9525)* (old3 - new3) + (93700 - 82500)*(old3 - new4) + (157000 - 93700)*(old4 - new4) + (total_income - 157000)*(old4 - new5)
    period_tax_savings = yr_tax_savings/payperiods
    x = str(round(yr_tax_savings))
    y = str(round(period_tax_savings, 2))
    return "Under the new tax plan, your yearly income will change by $" + x + " and $" + y + " per pay period" 

  elif total_income <=200000:
    yr_tax_savings = (82500 - 9525)* (old3 - new3) + (93700 - 82500)*(old3 - new4) + (157000 - 93700)*(old4 - new4) + (195450 - 157000)*(old4 - new5) + (total_income - 195450)*(old5 - new5)
    period_tax_savings = yr_tax_savings/payperiods
    x = str(round(yr_tax_savings))
    y = str(round(period_tax_savings, 2))
    return "Under the new tax plan, your yearly income will change by $" + x + " and $" + y + " per pay period" 

  elif total_income <= 424950:
    yr_tax_savings = (82500 - 9525)* (old3 - new3) + (93700 - 82500)*(old3 - new4) + (157000 - 93700)*(old4 - new4) + (195450 - 157000)*(old4 - new5) + (200000 - 195450)*(old5 - new5) + (total_income - 200000) * (old5 - new6)
    period_tax_savings = yr_tax_savings/payperiods
    x = str(round(yr_tax_savings))
    y = str(round(period_tax_savings, 2))
    return "Under the new tax plan, your yearly income will change by $" + x + " and $" + y + " per pay period" 

  elif total_income <= 426700:
    yr_tax_savings = (82500 - 9525)* (old3 - new3) + (93700 - 82500)*(old3 - new4) + (157000 - 93700)*(old4 - new4) + (195450 - 157000)*(old4 - new5) + (200000 - 195450)*(old5 - new5) + (424950 - 200000) * (old5 - new6) + (total_income - 424950) * (old6 - new6)
    period_tax_savings = yr_tax_savings/payperiods
    x = str(round(yr_tax_savings))
    y = str(round(period_tax_savings, 2))
    return "Under the new tax plan, your yearly income will change by $" + x + " and $" + y + " per pay period" 

  elif total_income <= 50000:
    yr_tax_savings = (82500 - 9525)* (old3 - new3) + (93700 - 82500)*(old3 - new4) + (157000 - 93700)*(old4 - new4) + (195450 - 157000)*(old4 - new5) + (200000 - 195450)*(old5 - new5) + (424950 - 200000) * (old5 - new6) + (426700 - 424950) * (old6 - new6) + (total_income - 426700) *(old7 - new6)
    period_tax_savings = yr_tax_savings/payperiods
    x = str(round(yr_tax_savings))
    y = str(round(period_tax_savings, 2))
    return "Under the new tax plan, your yearly income will change by $" + x + " and $" + y + " per pay period" 

  else:
    yr_tax_savings = (82500 - 9525)* (old3 - new3) + (93700 - 82500)*(old3 - new4) + (157000 - 93700)*(old4 - new4) + (195450 - 157000)*(old4 - new5) + (200000 - 195450)*(old5 - new5) + (424950 - 200000) * (old5 - new6) + (426700 - 424950) * (old6 - new6) + (500000 - 426700) *(old7 - new6) + (total_income - 500000) *(old7 - new7)
    period_tax_savings = yr_tax_savings/payperiods
    x = str(round(yr_tax_savings))
    y = str(round(period_tax_savings, 2))
    return "Under the new tax plan, your yearly income will change by $" + x + " and $" + y + " per pay period" 
    
def married_filer(income, payperiods):
  old1 = .1
  old2 = .15
  old3 = .25
  old4 = .28
  old5 = .33
  old6 = .35
  old7 = .396
  new1 = .18
  new2 = .12
  new3 = .22
  new4 = .24
  new5 = .32
  new6 = .35
  new7 = .37
  total_income = income * payperiods
  if total_income <= 18650:
    return "No change"
  
  elif total_income < 19050:
    yr_tax_savings = (total_income - 18650)* (old2 - new1)
    period_tax_savings = yr_tax_savings/payperiods
    x = str(round(yr_tax_savings))
    y = str(round(period_tax_savings, 2))
    return "Under the new tax plan, your yearly income will change by $" + x + " and $" + y + " per pay period" 
  
  elif total_income <=75900:
    yr_tax_savings = (total_income - 18650)* (old2 - new2) + (19050 - 18650)* (old2 - new1)
    period_tax_savings = yr_tax_savings/payperiods
    x = str(round(yr_tax_savings))
    y = str(round(period_tax_savings, 2))
    return "Under the new tax plan, your yearly income will change by $" + x + " and $" + y + " per pay period" 
  
  elif total_income <=77400:
    yr_tax_savings = (total_income - 75900)*(old3 - new2) + (75900 - 18650)* (old2 - new2) + (19050 - 18650)* (old2 - new1)
    period_tax_savings = yr_tax_savings/payperiods
    x = str(round(yr_tax_savings))
    y = str(round(period_tax_savings, 2))
    return "Under the new tax plan, your yearly income will change by $" + x + " and $" + y + " per pay period" 
  
  elif total_income <=140000:
    yr_tax_savings = (total_income - 77400)*(old3 - new3) + (77400 - 75900)*(old3 - new2) + (75900 - 18650)* (old2 - new2) + (19050 - 18650)* (old2 - new1)
    period_tax_savings = yr_tax_savings/payperiods
    x = str(round(yr_tax_savings))
    y = str(round(period_tax_savings, 2))
    return "Under the new tax plan, your yearly income will change by $" + x + " and $" + y + " per pay period" 
    
  elif total_income <=153100:
    yr_tax_savings =  (total_income - 140000)*(old3 - new4) + (140000 - 77400)*(old3 - new3) + (77400 - 75900)*(old3 - new2) + (75900 - 18650)* (old2 - new2) + (19050 - 18650)* (old2 - new1)
    period_tax_savings = yr_tax_savings/payperiods
    x = str(round(yr_tax_savings))
    y = str(round(period_tax_savings, 2))
    return "Under the new tax plan, your yearly income will change by $" + x + " and $" + y + " per pay period" 
  
  elif total_income <=233350:
    yr_tax_savings =  (total_income - 153100)*(old4 - new4) + (153100 - 140000)*(old3 - new4) + (140000 - 77400)*(old3 - new3) + (77400 - 75900)*(old3 - new2) + (75900 - 18650)* (old2 - new2) + (19050 - 18650)* (old2 - new1)
    period_tax_savings = yr_tax_savings/payperiods
    x = str(round(yr_tax_savings))
    y = str(round(period_tax_savings, 2))
    return "Under the new tax plan, your yearly income will change by $" + x + " and $" + y + " per pay period" 
    
  elif total_income <=320000:
    yr_tax_savings =  (total_income - 233350)*(old5 - new4) + (233350 - 153100)*(old4 - new4) + (153100 - 140000)*(old3 - new4) + (140000 - 77400)*(old3 - new3) + (77400 - 75900)*(old3 - new2) + (75900 - 18650)* (old2 - new2) + (19050 - 18650)* (old2 - new1)
    period_tax_savings = yr_tax_savings/payperiods
    x = str(round(yr_tax_savings))
    y = str(round(period_tax_savings, 2))
    return "Under the new tax plan, your yearly income will change by $" + x + " and $" + y + " per pay period" 
    
  elif total_income <=400000:
    yr_tax_savings =  (total_income - 320000)*(old5 - new5) + (320000 - 233350)*(old5 - new4) + (233350 - 153100)*(old4 - new4) + (153100 - 140000)*(old3 - new4) + (140000 - 77400)*(old3 - new3) + (77400 - 75900)*(old3 - new2) + (75900 - 18650)* (old2 - new2) + (19050 - 18650)* (old2 - new1)
    period_tax_savings = yr_tax_savings/payperiods
    x = str(round(yr_tax_savings))
    y = str(round(period_tax_savings, 2))
    return "Under the new tax plan, your yearly income will change by $" + x + " and $" + y + " per pay period" 
    
  elif total_income <=416700:
    yr_tax_savings =  (total_income - 400000)*(old5 - new6) + (400000 - 320000)*(old5 - new5) + (320000 - 233350)*(old5 - new4) + (233350 - 153100)*(old4 - new4) + (153100 - 140000)*(old3 - new4) + (140000 - 77400)*(old3 - new3) + (77400 - 75900)*(old3 - new2) + (75900 - 18650)* (old2 - new2) + (19050 - 18650)* (old2 - new1)
    period_tax_savings = yr_tax_savings/payperiods
    x = str(round(yr_tax_savings))
    y = str(round(period_tax_savings, 2))
    return "Under the new tax plan, your yearly income will change by $" + x + " and $" + y + " per pay period" 
    
  elif total_income <=470700:
    yr_tax_savings =  (total_income - 416700)*(old6 - new6) + (416700 - 400000)*(old5 - new6) + (400000 - 320000)*(old5 - new5) + (320000 - 233350)*(old5 - new4) + (233350 - 153100)*(old4 - new4) + (153100 - 140000)*(old3 - new4) + (140000 - 77400)*(old3 - new3) + (77400 - 75900)*(old3 - new2) + (75900 - 18650)* (old2 - new2) + (19050 - 18650)* (old2 - new1)
    period_tax_savings = yr_tax_savings/payperiods
    x = str(round(yr_tax_savings))
    y = str(round(period_tax_savings, 2))
    return "Under the new tax plan, your yearly income will change by $" + x + " and $" + y + " per pay period" 
  
  elif total_income <=1000000:
    yr_tax_savings =  (total_income - 470700)*(old7 - new6) + (470700 - 416700)*(old6 - new6) + (416700 - 400000)*(old5 - new6) + (400000 - 320000)*(old5 - new5) + (320000 - 233350)*(old5 - new4) + (233350 - 153100)*(old4 - new4) + (153100 - 140000)*(old3 - new4) + (140000 - 77400)*(old3 - new3) + (77400 - 75900)*(old3 - new2) + (75900 - 18650)* (old2 - new2) + (19050 - 18650)* (old2 - new1)
    period_tax_savings = yr_tax_savings/payperiods
    x = str(round(yr_tax_savings))
    y = str(round(period_tax_savings, 2))
    return "Under the new tax plan, your yearly income will change by $" + x + " and $" + y + " per pay period" 
    
  else:
    yr_tax_savings =  (total_income - 1000000)*(old7 - new7) + (1000000 - 470700)*(old7 - new6) + (470700 - 416700)*(old6 - new6) + (416700 - 400000)*(old5 - new6) + (400000 - 320000)*(old5 - new5) + (320000 - 233350)*(old5 - new4) + (233350 - 153100)*(old4 - new4) + (153100 - 140000)*(old3 - new4) + (140000 - 77400)*(old3 - new3) + (77400 - 75900)*(old3 - new2) + (75900 - 18650)* (old2 - new2) + (19050 - 18650)* (old2 - new1)
    period_tax_savings = yr_tax_savings/payperiods
    x = str(round(yr_tax_savings))
    y = str(round(period_tax_savings, 2))
    return "Under the new tax plan, your yearly income will change by $" + x + " and $" + y + " per pay period" 
    



if filing_status == 1:
  print(single_filer(income, payperiods))
elif filing_status == 2:
  print(married_filer(income,payperiods))
else:
  print("We're still working on other statuses")