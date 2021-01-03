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
    # For Command 10,11
    elif cmd in [10, 11]:
        a = float(input("Enter base of trapezium: "))
        b = float(input("Enter top length of trapezium: "))
        height = float(input("Enter height of trapezim: "))
        # For Command 10
        if cmd == 10:
            print(0.5 * (a + b) * height)
        # For Command 11
        else:
            width = float(input("Enter width of trapezium: "))
            print((0.5 * (a + b) * height) * width)
    # Invalid Input Statement
    else:
        print("You have entered in an invalid input. Please try again.")
