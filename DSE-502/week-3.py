# 1.16
# user_name = input()
# print("Hey", user_name)
# print("Welcome to zyBooks!")

# 2.1
# y = 6
# x = y + 1
# y = 14
# print(x, y)

# x = 2
# y = 3
#
# x = x * y
# x = x * y
# print(x)

# x = 4
# y = x
# x = 6
# print(x, y)

# num_pies = int(input())
#
# num_pies *= 4
#
# print(num_pies)


# gas_mileage = float(input())
# gas_cost = float(input())
# value1 = (20 / gas_mileage) * gas_cost
# value2 = (75 / gas_mileage) * gas_cost
# value3 = (500 / gas_mileage) * gas_cost
#
# print(f"{value1:.2f} {value2:.2f} {value3:.2f}")

# age = int(input())
# weight = int(input())
# heart_rate = int(input())
# time = int(input())
#
# calories = (((age * 0.2757) + (weight * 0.03295) + (heart_rate * 1.0781) - 75.4991) * time) / 8.368
#
# print(f"Calories: {calories:.2f} calories")


# user_int = int(input("Enter integer (32 - 126):\n"))
# user_float = float(input("Enter float:\n"))
# user_char = input("Enter character:\n")
# user_str = input("Enter string:\n")
#
# print(user_int, user_float, user_char, user_str)
# print(user_str, user_char, user_float, user_int)
# print(f"{user_int} converted to a character is {chr(user_int)}")

item_name = input("Enter food item name:\n")
item1_price = float(input("Enter item price:\n"))
item1_quantity = int(input("Enter item quantity:\n"))
item1_total = item1_price * item1_quantity
print("")
print(f"RECEIPT\n"
      f"{item1_quantity} {item_name} @ ${item1_price:.2f} = ${item1_total:.2f}\n"
      f"Total cost: ${item1_total:.2f}\n\n")

item2_name = input("Enter second food item name:\n")
item2_price = float(input("Enter item price:\n"))
item2_quantity = int(input("Enter item quantity:\n"))
item2_total = item2_price * item2_quantity
print("")
print(f"RECEIPT\n"
      f"{item1_quantity} {item_name} @ ${item1_price:.2f} = ${item1_total:.2f}\n"
      f"{item2_quantity} {item2_name} @ ${item2_price:.2f} = ${item2_total:.2f}\n"
      f"Total cost: ${item1_total + item2_total:.2f}")
print("")
gratuity = ((item1_total + item2_total) * 0.15)
tot_plus_tip = ((item1_total + item2_total) * 1.15)
print(f"15% gratuity: ${gratuity:.2f}\n"
      f"Total with tips: ${tot_plus_tip:.2f}")