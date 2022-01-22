age=int(input("what is your current age ? "))

year_remaining = 90 - age
days_remaining = year_remaining*365
week_remaining=year_remaining*52
month_reamining= year_remaining*12
result= f"you have {days_remaining} days,{week_remaining} week,{month_reamining} month"
print(result)