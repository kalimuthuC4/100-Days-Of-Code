print("welcome to tip calculater")
bill = float(input("what was the total bill $ "))
tip = int(input("how much tip did you like to give? 10, 12, 15, 20?"))
people = int(input("how many person want to split the bill?"))
bill_with_tip = tip/100*bill+bill
total_amount = bill_with_tip/people
final_amount = "{:.2f}".format(total_amount)
final_bill =f"each person should pay${final_amount}"
print(final_bill)
