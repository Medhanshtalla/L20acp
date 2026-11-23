print("========== Grocery Comparsion Tool ==========")
rice_price = 234
milk_price = 46
fruit_price = 56
number_of_baskets = 34
family_members = 6

# Part 1
cost_per_person = ((rice_price + milk_price + fruit_price) * number_of_baskets) / family_members

# Part 2
total_items = int(input("Enter total items: "))
people = int(input("Enter number of people: "))
if total_items % people == 0:
    print("Items can be shared equally.")
else:
    print("Not equal, leftover:", total_items % people)

# Part 3
weekly_average = 72.7
store_a_average = 78
store_b_average = 71
store_c_average = 83

if weekly_average < store_a_average and weekly_average < store_b_average and weekly_average < store_c_average:
    verdict = "cheaper than all three stores"
elif weekly_average > store_a_average and weekly_average > store_b_average and weekly_average > store_c_average:
    verdict = "more expensive than all three stores"
else:
    verdict = "somewhere in between the three stores"

print("\n=== SUMMARY ===")
print("Cost per person this week:", cost_per_person)
print("Weekly average           :", weekly_average)
print("Verdict                  :", verdict)