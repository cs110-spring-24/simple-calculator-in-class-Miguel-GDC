num 1 = input(input: ("your num 1: "))
op = input(input: ("your operator: "))
num 2 = input(input: "your operator: ")

if operator == "+":
	total = num 1 + num 2
	print (f"{num 1} + {num 2} = {total}")
#the "if" statement makes the code which operation to carry out

if operator == "-":
	total = num 1 - num 2
	print (f"{num 1} - {num 2} = {total}")

if operator == "*":
	total = num 1 * num 2
	print (f"{num 1} * {num 2} = {total}")

if operator == "/":
	total = num 1 * num 2
	print ({f"{num 1} / {num 2} = {total}"})

if operator == "**":
	total = num 1 ** num 2
	print ({f"{num 1} ** {num 2} = {total}"})

if operator == "//":
	total = num 1 // num 2
	print ({f"{num 1} // {num 2} = {total}"})

if operator == "%":
	total = num 1 ** num 2
	print ({f"{num 1} % {num 2} = {total}"}) 

else:
	print ("Invalid operator")
	print ("Valid operators include: +, -, *, /, **, //, %")
