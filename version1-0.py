# Variables

q1 = True
q2 = False
q3 = False
calculate = False
ask = False
q1a = ""
q2a = ""
square_length = ""
square_area = ""
square_perimeter = ""
rectangle_length = ""
rectangle_breath = ""
rectangle_area = ""
rectangle_perimeter = ""
rectangle_perimeter_1 = ""
rectangle_perimeter_2 = ""

# Systems

if q1:
  q1a = input("What shape would you like to calculate? Enter Here: ")
  q1 = False
  q2 = True
  
if q2:
  if q1a == "Square":
    q2a = input("Area or Perimeter? Enter Here: ")
    q2 = False
    q3 = True
  elif q1a == "Rectangle":
    q2a = input("Area or Perimeter? Enter Here: ")
    q2 = False
    q3 = True
    
if q3:
  if q1a == "Square":
    if q2a == "Area":
      square_length = input("What is the length of the square? Enter Here: ")
      q3 = False
      calculate = True
    elif q2a == "Perimeter":
      square_length = input("What is the length of the square? Enter Here: ")
      q3 = False
      calculate = True
  elif q1a == "Rectangle":
    if q2a == "Area":
      rectangle_length = input("What is the length of the rectangle? Enter Here: ")
      rectangle_breath = input("What is the breath of the rectangle? Enter Here: ")
      q3 = False
      calculate = True
    elif q2a == "Perimeter":
      rectangle_length = input("What is the length of the rectangle? Enter Here: ")
      rectangle_breath = input("What is the breath of the rectangle? Enter Here: ")
      q3 = False
      calculate = True

if calculate:
 if q1a == "Square":
  if q2a == "Area":
   square_area = square_length * square_length
  elif q2a == "Perimeter":
   square_perimeter = square_length * 4
 elif q1a == "Rectangle"
  if q2a == "Area":
   rectangle_area = rectangle_length * rectangle_breath
   calculate = False
  if q2a == "Perimeter":
   rectangle_perimeter_1 = rectangle_length * 2
   rectangle_perimeter_2 = rectangle_breath * 2
   rectangle_perimeter = rectangle_perimeter_1 + rectangle_perimeter_2
   calculate = False

if ask:
 if q1a == "Square":
  if q2a == "Area": 
   print("The area of the square is " + square_area + " !")
  elif q2a == "Perimeter":
   print("The perimeter of the square is " + square_perimeter + " !")
 elif q1a == "Rectangle":
  if q2a == "Area":
    print("The area of the rectangle is " + rectangle_area + " !")
  elif q2a == "Perimeter":
    print("The perimeter of the rectangle is " + rectangle_perimeter + " !")
 
