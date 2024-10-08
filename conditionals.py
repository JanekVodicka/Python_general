# If/Else statements
# For restriction, validation user input
	# We want to avoid or handle values:
		# - which does not make sense
		# - that could crash our program
		# - could even be a security risk
# Concept of conditionals
	# Expression that evaluate to either true or false
	# Comparison Operators
		# Equals: a == b
		# Not Equals: a != b
		# Less than: a < b
		# Less than or equal to: a <= b
		# Greater than: a < b
		# Greater than or equal to: a >= b
# V PROGRAMOVÁNÍ SE PODMÍNKY VE VĚTŠINĚ PŘÍPADŮ DÁVAJÍ DO FUNKCÍ!!!


# K příkladu - podmínka, že číslo je větší než nula:
	# Uživatel nám dá hodnotu, my převedeme na číslo, které vložíme do funkce. Ve funkci zavedeme kontrolní podmínku
calculation_to_units = 24
name_of_units = "hours"


def days_to_units(num_of_days):
	print(num_of_days > 0)
	# or
	condition_check = num_of_days > 0
	print(type(condition_check))

	if num_of_days > 0:			# num_of_days > 0 ... Conditional can be TRUE or FALSE ... Boolean Type
		return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"
	elif num_of_days == 0:
		return "You entered a 0, please enter a valid positive number"
	else:
		return "You entered a negative value, so no conversion for you!"


def validate_and_execute():
	if user_input.isdigit():	# Is digit je funkce, používá syntax: Parametr.funkce()
		user_input_number = int(user_input)
		calculated_value = days_to_units(user_input_number)
		print(calculated_value)
	else:
		print("Your input is not a valid number. Don´t ruin my program!")
		# ... díky této podmínce bychom mohli vynechat else podmínku záporného čísla v podmínce if num_of_days > 0

user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
validate_and_execute()


# UČESÁNÍ PROGRAMU:
def days_to_units_2(num_of_days):
	return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"


def validate_and_execute_2():
	if user_input_2.isdigit():
		user_input_number = int(user_input_2)
		if user_input_number > 0:
			calculated_value = days_to_units_2(user_input_number)
			print(calculated_value)
		elif user_input_number == 0:
			print("You entered a 0, please enter a valid positive number")
	else:
		print("Your input is not a valid number. Don´t ruin my program!")

user_input_2 = input("Hey user, enter a number of days and I will convert it to hours!\n")
validate_and_execute_2()


