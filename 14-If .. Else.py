#Python supports the usual logical conditions from mathematics:
'''
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
'''
'''
a = 33
b = 200
if b > a:
  print("b is greater than a")
'''
#The elif keyword is pythons way of saying "if the previous conditions were not true,
# then try this condition".
'''
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
'''
#The else keyword catches anything which isn't caught by the
# preceding conditions.
'''
a = 200
b = 33
c = 150
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
'''
#One line if, else statement:
'''
a, b = 200,  56
if a > b: print("a is greater than b")
#This technique is known as Ternary Operators, or Conditional
# Expressions.
print("A") if a > b else print("B")
'''
#The and keyword is a logical operator, and is used to combine
# conditional statements:
'''
a, b, c = 200, 33, 500
if a > b and c > a:
  print("Both conditions are True")
'''
#The or keyword is a logical operator, and is used to combine
# conditional statements:
'''
a, b, c = 200, 33, 500
if a > b or a > c:
  print("At least one of the conditions is True")
'''
#You can have if statements inside if statements, this is called
# nested if statements.
'''
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
'''
#if statements cannot be empty, but if you for some reason have
# an if statement with no content, put in the pass statement to
# avoid getting an error.
'''
a, b = 33, 200
if b > a:
  pass
'''










