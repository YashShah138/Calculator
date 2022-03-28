### Program make a simple calculator ###

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function raises x to the power of y
def exponents(x, y):
		return x ** y

# This function divides x by by and gives the first integer
def floor_division(x, y):
		return x // y

def mod(x, y):
	return x % y
	
# menu
print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponents")
print("6. Floor Division")
print("7. Modular")

while True:
	# take input from the user
	choice = input("Enter choice(1, 2, 3, 4, 5, 6, 7): ")

	# check if choice is one of the four options
	if choice in ('1', '2', '3', '4', '5', '6', '7'):
		num1 = int(input("Enter first number: "))
		num2 = int(input("Enter second number: "))

		if choice == '1':
			print(num1, "+", num2, "=", add(num1, num2))

		elif choice == '2':
			print(num1, "-", num2, "=", subtract(num1, num2))

		elif choice == '3':
			print(num1, "*", num2, "=", multiply(num1, num2))

		elif choice == '4':
			print(num1, "/", num2, "=", divide(num1, num2))

		elif choice =='5':
			print(num1, "^", num2, "=", exponents(num1, num2))

		elif choice == '6':
			print(num1, "//", num2, "=", floor_division(num1, num2))

		elif choice == '7':
			print(num1, "%", num2, "=", mod(num1, num2))

		else:
			print("Invalid Input")
		# check if user wants another calculation
		# break the while loop if answer is no
		next_calculation = input("Let's do next calculation? (yes/no): ")
		if next_calculation.lower() == "no":
			break
		elif next_calculation.lower() == "n":
			break
	else:
		print("Invalid Input")