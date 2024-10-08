# FUNKCE
# To avoid repeating the same logic in code
# A Function is defined using the def keyword
    # def name_of_function(parameters):
# Whatever is inside the function is called Function Body
# Block of code which only returns when it is called
    # Calling function = executing code
    # Jakmile použiji return, k zavolání funkce používám print()
# Function parameters
    # Information can be passed into functions as parameters
    # Parameters are also called arguments
# SCOPE
    # A variable is only available from inside the region it is created
        # Global scope = variables available from within any scope
        # Local scope = variable created inside function
# CO MUSÍM VĚDĚT
    # Účel funkce
    # Jméno funkce
    # Vstup(x)
    # Výstup(y)
    # Výjimky
# Functions with return value
    # A function can return data as a result
    # When we want a value as a result of function execution

# Příklad 1
def my_function():
    print("Příklad 1: Hello from a function")
# Zavolání funkce
my_function()


# Příklad 2
def cube(x):    # Jmeno(input)
    print("Příklad 2: Povrch krychle o straně a je roven:")
    return x**3
# Zavolání funkce
print(cube(3))


# Příklad 3
fruits = ["apple", "banana", "cherry"]
def my_function(food):
    print("Příklad 3: Ovoce")
    for x in food:
        print(x)
# Zavolání funkce
my_function(fruits)


# Příklad 4
print("Příklad 4: Input")
x = int(input("x = "))
def y(x):
    return x**2 + 2*x + x
# Zavolání funkce
print("y =", y(x))


# Příklad 5
calculation_to_units = 24
name_of_units = "hours"
def days_to_units(num_of_days, custom_message):
    print("Příklad 5: Multiple arguments and combination variables + fc arguments")
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}")
    return(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}")
    print(custom_message)
    return custom_message
# Zavolání funkce
days_to_units(20, "Ahoj - Custom message")

my_var = days_to_units(20, "Ahoj - Custom message")
print(my_var)

