sales_person = input("Put you name: ")
sales = float(input("Put how much you have sold: "))

won_in_sales = round(sales*0.13)

print(f"Congratulations {sales_person} you sold {won_in_sales:.2f} R$ this month.")
