try:
    # Take input command
    cmd = int(input("""
Enter 1 for area of Square
Enter 2 for perimeter of Square
Enter 3 for area of Rectangle
Enter 4 for perimeter of Rectangle
>>> """))
except ValueError:
    print("Check input and try again")
else:
    # Just giving a newline
    print()
    # For square
    if cmd in [1, 2]:
        l = float(input("Enter length of sides of Square: "))

        # For area of square.
        if cmd == 1:
            print(l * l)
        # For perimeter of square.
        else:
            print(4 * l)
    elif cmd in [3, 4]:
        l = float(input("Enter length of Rectangle: "))
        b = float(input("Enter width of Rectangle: "))
        # For area of Rectangle
        if cmd == 3:
            print(l * b)
        #For perimeter of Ractangle
        else:
            print(2 * (l + b))
    else:
        print("Check input and try again.")
