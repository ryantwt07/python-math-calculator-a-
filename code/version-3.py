try:
    # Take Input Command
    cmd = int(input("""
Enter 1 for Area of Square
Enter 2 for Perimeter of Square
Enter 3 for Area of Rectangle
Enter 4 for Perimeter of Rectangle
Enter 5 for Area of Circle (pi will be 3.14)
Enter 6 for Diameter of Circle (pi will be 3.14)
Enter 7 for Circumference of Circle (pi will be 3.14)
Enter 8 for Area of Triangle
Enter 9 for Perimeter of Triangle
Enter 10 for Area of Trapezium
Enter 11 for Addition of Two 2x2 Matrix
Enter 12 for Usual Addition Calculations
Enter 13 for Usual Subtraction Calculations
Enter 14 for Usual Multiplication Calculations
Enter 15 for Usual Division Calculations
>>> """))
except ValueError:
    print("You have entered an invalid input. Please try again.")
else:
    # Newline
    print()
    # For Command Lines 1 and 2
    if cmd in [1, 2]:
        length = float(input("Enter length of sides of Square: "))
        # For Command 1
        if cmd == 1:
            print(length * length)
        # For Command 2
        else:
            print(4 * length)
    elif cmd in [3, 4]:
        length = float(input("Enter length of Rectangle: "))
        breath = float(input("Enter width of Rectangle: "))
        # For Command 3
        if cmd == 3:
            print(length * breath)
        # For Command 4
        else:
            print(2 * (length + breath))
    # For Command 5,6,7
    elif cmd in [5, 6, 7]:
        radius = float(input("Enter radius of circle: "))
        # For Command 5
        if cmd == 5:
            print(3.14 * (radius * radius))
        # For Command 6
        elif cmd == 6:
            print(2 * radius)
        # For Command 7
        else:
            print(3.14 * (radius * 2))
    # For Command 8
    elif cmd == 8:
        base = float(input("Enter base of triangle: "))
        height = float(input("Enter height of triangle: "))
        print(0.5 * base * height)
    # For Command 9
    elif cmd == 9:
        side = float(input("Enter side of triangle: "))
        side2 = float(input("Enter second side of triangle: "))
        side3 = float(input("Enter third side of triangle: "))
        print(side + side2 + side3)
    # For Command 10
    elif cmd == 10:
        a = float(input("Enter base of trapezium: "))
        b = float(input("Enter top length of trapezium: "))
        height = float(input("Enter height of trapezium: "))       
        if cmd == 10:
            print(0.5 * (a + b) * height)        
        else:
            width = float(input("Enter width of trapezium: "))
            print((0.5 * (a + b) * height) * width)
    # For Command 11
    elif cmd == 11:

        n11 = float(input("Enter the element of 1st column and 1st row of 1st matrix :"))
        n12 = float(input("Enter the element of 2nd column and 1st row of 1st matrix :"))
        n21 = float(input("Enter the element of 1st column and 2nd row of 1st matrix :"))
        n22 = float(input("Enter the element of 2nd column and 2nd row of 1st matrix :"))
        m11 = float(input("Enter the element of 1st column and 1st row of 2nd matrix :"))
        m12 = float(input("Enter the element of 2nd column and 1st row of 2nd matrix :"))
        m21 = float(input("Enter the element of 1st column and 2nd row of 2nd matrix :"))
        m22 = float(input("Enter the element of 2nd column and 2nd row of 2nd matrix :"))  

        X = [[n11, n12], [n21, n22]]
        Y = [[m11, m12], [m21, m22]]
        result = [[0, 0],[0, 0]]
        # Iterate Through Rows
        for i in range(len(X)):
            # iterate through columns
            for j in range(len(X[0])):
                result[i][j] = X[i][j] + Y[i][j]
        for r in result:
            print(r)
    elif cmd in [12, 13, 14, 15]:
        if cmd == 12:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            print(num1 + num2)
        elif cmd == 13:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            print(num1 - num2)
        elif cmd == 14:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            print(num1 * num2)
        else:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            print(num1 / num2)
    # Invalid Input Statement
    else:
        print("You have entered in an invalid input. Please try again.")
