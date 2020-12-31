# Variables

q1 = True
q2 = False
q3 = False
calculate = False
q1a = ""
q2a = ""
square_length = ""
square_area = ""
square_perimeter = ""
rectangle_length = ""
rectangle_breath = ""
rectangle_area = ""
rectangle_perimeter = ""

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
'''    
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
  elif q1a == "Perimeter":
    if q2a == "Area":
      rectangle_length = input("What is the length of the rectangle? Enter Here: ")
      '''
