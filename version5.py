import math
from math import pi

try:	
	maincmd = int(input("""
	Enter 1 for Matrix
	Enter 2 for Normal Calculations
	Enter 3 for Area and Perimeter
	Enter 4 for Circles
	Enter 5 for Theorem
	>>> """))
except ValueError:
	print("You have entered an invalid input. Please try again.")
else:
	print()
	if maincmd == 1:
		try:
			cmd = int(input("""
			Enter 1 for Additon of 2x2 Matrix
			>>> """)) 
		except ValueError:
			print("You have entered an invalid input. Please try again.")
		else:
			print()
			if cmd == 1:
				n11 = float(input("Enter the element of the 1st column and 1st row of the 1st matrix: "))
				n12 = float(input("Enter the element of the 2nd column and the 1st row of the 1st matrix: "))
				n21 = float(input("Enter the element of the 1st column and 2nd row of the 1st matrix: "))
				n22 = float(input("Enter the elemrnt of the 2nd column and the 2nd row of the 1st matrix: "))
				m11 = float(input("Enter the element of the 1st column and 1st row of 2nd matrix: "))
				m12 = float(input("Enter the element of the 2nd column and 1st row of 2nd matrix: "))
				m21 = float(input("Enter the element of the 2nd column and 1st row of 2nd matrix: "))
				m22 = float(input("Enter the element of the 2nd column and 2nd row of 2nd matrix: "))
				X = [[n11, n12], [n21, n12]]
				Y = [[m11, m12], [m21, m22]]
				result = [[0, 0], [0, 0]]
				for i in range(len(X)):
					for j in range(len(X[0])):
						result[i][j] = X[i][j] + Y[i][j]
				for r in result:
					print(r)
	elif maincmd == 2:
		try:
			cmd = int(input("""
			Enter 1 for Addition
			Enter 2 for Subtraction
			Enter 3 for Multiplication
			Enter 4 for Division
			>>> """))
		except ValueError:
			print("You have entered an invalid input. Please try again.")
		else:
			print()
			if cmd in [1, 2, 3, 4]:
				num1 = float(input("Enter the First Number: "))
				num2 = float(input("Enter the Second Number: "))
				if cmd == 1:
					print(num1 + num2)
				elif cmd == 2:
					print(num1 - num2)
				elif cmd == 3:
					print(num1 * num2)
				else:
					print(num1 / num2)
	elif maincmd == 3:
		try:
			cmd = int(input("""
			Enter 1 for Area of Square
			Enter 2 for Perimeter of Square
			Enter 3 for Area of Rectangle
			Enter 4 for Perimeter of Rectangle
			Enter 5 for Area of Triangle
			Enter 6 for Perimeter of Triangle
			Enter 7 for Area of Trapezium
			>>> """))
		except ValueError:
			print("You have entered an invalid input. Please try again.")
		else:
			print()
			if cmd in [1, 2]:
				length = float(input("Enter the length of a side of the square: "))
				if cmd == 1:
					print(length * length)
				else:
					print(length * 4)
			elif cmd in [3, 4]:
				length = float(input("Enter the length of a side of the rectangle: "))
				breath = float(input("Enter the breath of a side of the rectangle: "))
				if cmd == 3:
					print(length * breath)
				else:
					print(2 * (length + breath))
			elif cmd == 5:
				base = float(input("Enter Base of Triangle: "))
				height = float(input("Enter Height of Triangle: "))
				print(0.5 * base * height)
			elif cmd == 6:
				side1 = float(input("Enter 1st side of triangle: "))
				side2 = float(input("Enter the 2nd side of triangle: "))
				side3 = float(input("Enter the 3rd side of triangle: "))
				print(side1 + side2 + side3)
			else:
				a = float(input("Enter 1st side of Trapezium: "))
				b = float(input("Enter 2nd side of Trapezium: "))
				height = float(input("Enter height of Trapezium: "))
				print(0.5 * a * b * height)
	elif maincmd == 4:
		try:
			cmd = int(input("""
			Enter 1 for Area of Circle
			Enter 2 for Circumference of Circle
			Enter 3 for Diameter of Circle
			>>> """))
		except ValueError:
			print("You have entered an invalid input. Please try again.")
		else:
			if cmd in [1, 2]:
				pichoice = input("Please enter prefered choice of Pi: ")
				radius = float(input("Enter the Radius of The Circle: "))
				if pichoice == 3.14:
					if cmd == 1:
						print(3.14 * radius * radius)
					else:
						diameter = radius * 2
						print(3.14 * diameter)
				elif pichoice == "22/7":
					if cmd == 1:
						print(22 / 7 * radius * radius)
					else:
						diameter = radius * 2
						print(22 / 7 * diameter)
				else:
					if cmd == 1:
						print(pi * radius * radius)
					else:
						diameter = radius * 2
						print(pi * diameter)
			else:
				radius = float(input("Enter the Radius of Circle: "))
				print(radius * 2)
	elif maincmd == 5:
		try:
			cmd = int(input("""
			Enter 1 for Pythagoras
			Enter 2 for Converse Pythagoras
			Enter 3 for Trigonometry
			>>> """))
		except ValueError:
			print("You have entered an invalid input. Please try again.")
		else:
			if cmd == 1:
				try:
					subcmd = int(input("""
					Enter 1 to find A
					Enter 2 to find B
					Enter 3 to find C
					>>> """))
				except ValueError:
					print("You have entered an invalid input. Please try again.")
				else:
					if subcmd == 1:
						b = float(input("Enter B: "))
						c = float(input("Enter C: "))
						b2 = b * b
						c2 = c * c
						a2 = c2 - b2
						a = math.sqrt(a2)
						print(a)
					elif subcmd == 2:
						a = float(input("Enter A: "))
						c = float(input("Enter C: "))
						a2 = a * a
						c2 = c * c
						b2 = c2 - a2
						b = math.sqrt(b2)
						print(b)
					elif subcmd == 3:
						a = float(input("Enter A: "))
						b = float(input("Enter B: "))
						a2 = a * a
						b2 = b * b
						c2 = a2 + b2
						c = math.sqrt(c2)
						print(c)
			elif cmd == 3:
					try:
						subcmd = int(input("""
						Enter 1 for Sine (SIN)
						Enter 2 for Cosine (COS)
						Enter 3 for Tangent (TAN)
						>>> """))
					except ValueError:
						print("You have entered an invalid input. Please try again.")
					else:
						if subcmd == 2:
							adjecent = float(input("Enter the Adjecent of Triangle: "))
							hypotenuse = float(input("Enter the Hypotenuse of Triangle: "))
							sine = adjecent / hypotenuse
							print(sine)
						elif subcmd == 1:
							opposite = float(input(" Enter the Opposite of Triangle: "))
							hypotenuse = float(input("Enter the Hypotenuse of Triangle: "))
							cosine = opposite / hypotenuse
							print(cosine)
						elif subcmd == 3:
							opposite = float(input("Enter the Opposite of Triangle: "))
							adjecent = float(input("Enter the Adjecent of Triangle: "))
							tangent = opposite / adjecent
							print(tangent)
