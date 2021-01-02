try:
    # Take Input Command
    cmd = int(input("""
Enter 1 for Area of Square
Enter 2 for Perimeter of Square
Enter 3 for Area of Rectangle
Enter 4 for Perimeter of Rectangle
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
    else:
        print("You have entered in an invalid input. Please try again.")
