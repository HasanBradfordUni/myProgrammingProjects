import random 
class Employee:
	def __init__(self, hours, rate):
		self.hours = hours
		self.rate = rate
hours = int(input('Enter hours: '))
rate = random.randint(1, 10)
pay = hours * rate
print('Pay:', pay)
hours = 40
error = random.choice([True, False])
if error:
	print("Error")
else:
	print("All Fine")
errorNumber = random.choice([1, 3, 5])
match errorNumber:
	case 1: print("Error Number 1")
	case 3: print("Error Number 3")
	case 5: print("That's a bad miss")

file = open('employees.txt', 'r')

employees = file.readlines()
for employee in employees:
	hours = int(input('Enter hours: '))
	pay = hours * rate
	print('Pay:', pay)
count = 0
Employees = [Employee(i*5, i) for i in range(1,11)]
while count < len(Employees):
	employee = Employees[count]
	count += 1
	hours = employee.hours
	rate = employee.rate
	pay = hours * rate
Employees = [Employee(i*5, i) for i in range(1,11)]
while count < len(Employees):
	employee = Employees[count]
	count += 1
	hours = employee.hours
	rate = employee.rate
	pay = hours * rate
