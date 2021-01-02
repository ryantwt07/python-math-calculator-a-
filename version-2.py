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
    # Just giving a newline
    print()
    # For square
    if cmd in [1, 2]:
        length = float(input("Enter length of sides of Square: "))

        # For area of square.
        if cmd == 1:
            print(length * length)
        # For perimeter of square.
        else:
            print(4 * length)
    elif cmd in [3, 4]:
        length = float(input("Enter length of Rectangle: "))
        breath = float(input("Enter width of Rectangle: "))
        # For area of Rectangle
        if cmd == 3:
            print(length * breath)
        # For perimeter of Rectangle
        else:
            print(2 * (length + breath))
    elif cmd in [5, 6, 7]:
        radius = float(input("Enter radius of circle: "))
        if cmd == 5:
            print(3.14 * (radius * radius))
        elif cmd == 6:
            print(3.14 * radius)
        elif cmd == 7:
            print(3.14 * (radius * 2))
    elif cmd == 8:
        base = float(input("Enter base of triangle: "))
        height = float(input("Enter height of triangle: "))
        print(0.5 * base * height)
    elif cmd == 9:
        base = float(input("Enter base of triangle: "))
        base2 = float(input("Enter base 2 of triangle: "))
        base3 = float(input("Enter base 3 of triangle: "))
        print(base1 + base2 + base3)
    elif cmd in [10,11]:
        a = float(input("Enter base of trapezium: "))
        b = float(input("Enter top length of trapezium: "))
        height = float(input("Enter height of trapezim: "))]
        if cmd == 10:
            print(0.5 * (a + b) * height)
        elif cmd == 11:
            width = float(input("Enter width of trapezium: "))
            print((0.5 * (a + b) * height) * width)
    else:
        print("You have entered in an invalid input. Please try again.")
