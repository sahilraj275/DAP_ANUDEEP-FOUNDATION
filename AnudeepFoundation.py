# 1.Calculation volume of a sphere
# input the radius in cm
# radius = float(input("Enter the radius of sphere: "))

# calculating the volume of the sphere
# volume = (4 * 3.14 * radius * radius * radius) / 3

# showing volume of sphere
# print("Volume of sphere is:", volume, "cubiccm")

# 2. write a program to input cost price of book. then apply 20% discount on it, calculate the price to be paid bt the customer?

# enter the cost price of the book
# cost_price = float(input("enter the cost price of the book: "))

# # calculating 20% discount on the book
# discount = (cost_price * 20) / 100

# # amount to be paid by the customer
# amount = cost_price - discount

# # displaying the amount
# print("The cost price of the book is", cost_price,"rs")
# print("_______________________________________________________")
# print("Discount of 20% is", discount,"rs")
# print("_____________________________________")
# print("Amount you have to pay for this book is:", amount,"rs")


# Write a program to check a number  is natural number or not

# number = int(input("enter the number: "))

# if number > 0:
#     print("It is a natural number")
# else:
#     print("it is not a natural number")

# 4. write a program  to input  marked price of a product. if the quatity is greater than 10 then apply 20% discount otherwise apply 10% discount. then calcualate the price to be paid by customer.

# # enter the marked price of the product
# marked_price = float(input("enter the marked_price: "))
# # enter the quantity you want to purchase
# quantity = int(input("enter the quantity: "))
# # taking a discount variable
# discount = 0
# # checking the condition if quantity is greater than 10 then apply 20% discount
# if quantity > 10:
#     discount = ((marked_price * 20) / 100) * quantity
#     amount = (marked_price * quantity) - discount
#     print("Amount to be paid by customer:", amount)
# # if quantity is less than 10 then apply 10% discount
# else:
#     discount = ((marked_price * 10) / 100) * quantity
#     amount = (marked_price * quantity) - discount
#     print("Amount to be paid by customer: ", amount)


# 5. write a program  to input  three angles  and check if they can  form a triangle or not.

# angle1 = float(input("enter the first angle: "))
# angle2 = float(input("enter the second angle: "))
# angle3 = float(input("enter the third angle: "))


# if (angle1 > 0 and angle2 > 0 and angle3 > 0) and (angle1 + angle2 + angle3 > 180):
#     print("yes they can form a triangele")
# else:
#     print("No it can't form a triangle")

# 6. write a program TO Input three angle of triangle and check if they can form a triangle or not. if they form a triangle then specify the type of triangle.


# angle1 = float(input("enter the first angle: "))
# angle2 = float(input("enter the second angle: "))
# angle3 = float(input("enter the third angle: "))


# if (angle1 > 0 and angle2 > 0 and angle3 > 0) and (angle1 + angle2 + angle3 > 180):
#     if angle1 < 90 and angle2 < 90 and angle3:
#         print("Above angles will form acute angle triangle")
#     else:
#         if angle1 == 90 or angle2 == 90 or angle3 == 90:
#             print("Above angle will form a right angle triangle")
#         else:
#             print("Above angle will form Obtuse angle")
# else:
#     print("Thses angle will not form any triangle")


# num1 = int(input("enter the firs num"))
# num2 = int(input("enter the second num"))
# num3 = int(input("enter the third num"))
# num4 = int(input("enter the 4rth num"))


# if num1 > num2 and num1 > num3 and num1 > num4:
#     print("This is gratest", num1)
# elif num2 > num1 and num2 > num3 and num2 > num4:
#     print("This is greates", num2)

# elif num3 > num1 and num3 > num2 and num3 > num4:
#     print("this is greatest:", num3)
# else:
#     print("this is greatest", num4)


# Write a program to arrange three numbers in ascending order
# Taking input from the user
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))

# # Using conditional statements to sort numbers
# if num1 > num2:
#     num1, num2 = num2, num1
# if num2 > num3:
#     num2, num3 = num3, num2
# if num1 > num2:
#     num1, num2 = num2, num1

# # Displaying the sorted numbers
# print("The numbers in ascending order are:", num1, num2, num3)

# Calculate the multiplication and sum of two numbers

# # getting input of first and second number here
# first_number = int(input("enter the first number: "))
# second_number = int(input("enter the second number: "))

# # calculating multiplication of first and second number
# multiplication = first_number * second_number
# # calculation addition of first and second number
# sum = first_number + second_number

# # printing first and second number and their multiplication to the user
# print("-------------Multiplication----------------------")
# print("first number: ", first_number)
# print("second number: ", second_number)
# print("-----------------------------------")
# print("Multiplication of", first_number, "and", second_number, "is =", multiplication)

# # printing first and second number and their addition to the user
# print("--------------Addition---------------------")
# print("first number: ", first_number)
# print("second number: ", second_number)
# # print("-----------------------------------")
# # print("Sum of", first_number, "and", second_number, "is =", sum)


# # 2. Python program to convert the temperature in degree centigrade to Fahrenheit

# # Ask the user to enter a temperature in degrees (assuming Celsius)
# temperature = float(input("Enter the temperature in degree: "))

# # Now let's convert this temperature to Fahrenheit
# # The formula to convert Celsius to Fahrenheit is (Celsius * 9/5) + 32
# fahrenheit = float((temperature * 9 / 5) + 32)

# # Finally, let's print out the result so the user can see the temperature in Fahrenheit
# print("-------------------------------------------")
# print("Temperature in degree was:", temperature)
# print("-------------------------------------------")
# print("Temperature in Fahrenheit is", fahrenheit)


# 3. Python program to find the area of a triangle whose sides are given

# # Importing the math module to use the sqrt function for square root calculations
# import math
# # Prompting the user to enter the lengths of the three sides of the triangle
# side1 = float(input("Enter the length of the first side: "))
# side2 = float(input("Enter the length of the second side: "))
# side3 = float(input("Enter the length of the third side: "))

# # Calculating the semi-perimeter (s)
# # Formula for semi-perimeter: s = (side1 + side2 + side3) / 2
# s = (side1 + side2 + side3) / 2

# # Displaying the semi-perimeter with a decorative separator
# print("----------------------------")
# print("Semi-perimeter (s) is:", s)
# print("----------------------------")

# # Calculating the area using Heron's formula
# # Formula: Area = sqrt(s * (s - side1) * (s - side2) * (s - side3))
# area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

# # Displaying the area with a decorative separator
# print("----------------------------")
# print("The area of the triangle is:", area)
# print("----------------------------")


# 4. Create a python program to Calculate area and perimeter of rectangle.

# Prompting the user to enter the length and width of the rectangle
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))

# # Calculating the area of the rectangle
# # Formula for area: Area = length * width
# area = length * width

# # Calculating the perimeter of the rectangle
# # Formula for perimeter: Perimeter = 2 * (length + width)
# perimeter = 2 * (length + width)

# # Displaying the calculated area and perimeter with decorative separators
# print("\n----------------------------")
# print("Length of triangle is:", length)
# print("width of triangle is:", width)
# print("\n----------------------------")
# print("The area of the rectangle is:", area)
# print("\n----------------------------")
# print("The perimeter of the rectangle is:", perimeter)
# print("----------------------------")


# First, let's ask the user to input five numbers.
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# num4 = float(input("Enter the fourth number: "))
# num5 = float(input("Enter the fifth number: "))

# # Now that we have all five numbers, let's calculate their sum.
# # We'll add all five numbers together to get the total sum.
# total_sum = num1 + num2 + num3 + num4 + num5

# # To find the average, we simply divide the total sum by 5
# average = total_sum / 5

# #  display the numbers the user entered
# print("\n----------------------------")
# print("The numbers you entered are:", num1, num2, num3, num4, num5)
# print("\n----------------------------")

# #  show the average of the numbers
# print("The average of the five numbers is:", average)
# print("----------------------------")


# take percentage input from user and base on  percentage value you have to print that student is in distinction (Percentage>70) /first class(Percentage>60)/sencond class (percentage >50)/third class (percentage >35)/fail(percentage is less than 35)


# percentage = int(input("Enter the marks in %: "))


# if percentage < 0 or percentage > 100:
#     print("Invalid input! Please enter a percentage between 0 and 100.")
# else:
#     if percentage >= 70:
#         print("First Class")
#     elif percentage >= 60:
#         print("Second Class")
#     elif percentage >= 50:
#         print("Third Class")
#     elif percentage >= 35:
#         print("Pass")
#     else:
#         print("Fail")

# string - it's a sequence of characters

str = "sahil"  # use to store single character
str1 = "rahil"
str2 = """Manel is sheltering from a rabies-like disease which sweeps the planet, until he is forced to leave and meet unlikely but essential traveling companions."""  #''' triple quotes use to store multi line strings


# print(str2[0])


# idx = 0
# while idx < len(str):
#     print(str[idx])
#     idx += 1


# for i in range(len(str1)):
#     print(str1[i])
#     i += 1


# skipping space in string

# str4 = "Anudip foundation"
# i = 0

# while i < len(str4):
#     if str4[i] == " ":
#         i += 1  # Increment to avoid infinite loop
#         continue
#     print(str4[i], end="") # we use end to print data horizontally
#     i += 1


# reverse a string
# str5 = "Choose"

# rev = ""

# for i in str5:
#     rev = i + rev
# print(rev)

# str = 'sahil /' 'raj'

# print(str)

# s = "apple"
# s1 = "banana"

# print(s === s1)

# print("apple"<'banana')

# print(10<10)


# print("demo" < "dummy")

# method-- method is a block of code that we can call whenever we want


# def add(a, b):
#     return a + b


# res = add(3, 4)
# print(res)


# user_input = input("Enter your Sentence:")
# cleaned_input = user_input.replace("your","our")
# print(cleaned_input)


# list_data = [1, 2, 3, 4, 5]
# idx = 0
# while idx < len(list_data):
#     print(list_data[idx])
#     idx += 1

# print("Length of the list is:", len(list_data))

list_data = [1, 2, 3, 4, 5]

# square_list = []

# for i in list_data:
#     square_list.append(i * i)
# print(square_list)

# comprehension_list = [i * i for i in list_data]
# print(comprehension_list)


fruits = ["apple", "mango", "kiwi", "litchi", "orange"]

# fruits_comprehension=[for x in fruits if  ]


# for i in fruits:
#     if "a" in i:
#         list_comprhension.append(i)
# print(list_comprhension)

# now using list_comprehension
list_comprhension = [x for x in fruits if "a" in x]
# print(list_comprhension)


# tuple
# tuple1 = (1, 2, 3, 4)
# print(tuple1[0])
# print(tuple1[1])
# print(tuple1[2])
# print(type, tuple1)

# list1 = [10, 20, 29]
# tuple2 = tuple(list1)
# print(type, tuple2)
# print(tuple2)

# singleton tuple

# singleton_tuple = (121,)
# print(singleton_tuple)

# str = "sahil"
# tuple3 = tuple(str)
# print(tuple3)

# for i in tuple1:
#     print(i)

# for index, ch in enumerate(tuple2):
#     print(f"index is {index} and character is {ch}")


# i = 0
# while i < len(tuple2):
#     print()


# strName = "Sahil"
# nameTuple = tuple(strName)

# n = 0
# c = 0
# while n < len(nameTuple):
#     if nameTuple[n] == "a":
#         c += 1
#         print(f"character 'a' is coming {c} times in your name")
#     n += 1

# tuple function

# t1 = ("sahil")
# print(t1.count("a"))

# strName = "Sahil"
# fnameTuple = tuple(strName)
# lname = "Raj"
# lnameTuple = tuple(lname)

# fullName = fnameTuple + lnameTuple
# repeatition_tuple = fullName * 2

# print(fullName)


tuple1 = (1, 2, 3, 4)
# tuple1[2]=30 #can't be achieved


#! set
# set stores only unique values.
# set datas are unordered.
# set is mutable collection of elements
# A set in Python is an unordered collection of unique elements. It is a built-in data type
# that is used to store a collection of values, with the key characteristic being that each
# element in a set must be unique. In other words, a set does not allow duplicate values.
# No Indexing: Sets do not support indexing

set1 = {1, 2, 3}
# print(set1)

set2 = {1, 1, 1, 2, 3, 3, 4, 5}
# print(set2)  # 1,2,3,4,5 its automatically remove duplicate values

# print(len(set1))

set1.remove(1)
# print(set1)  # 2,3

set1.discard(1)
# print(set1)

strSet = {"sahil"}
# print(strSet)

# strSet.remove('p') #it will search for the character if it is not there it will throw an error
# strSet.discard('p') # but if the character is not present there it won't throw any error

# set2.pop()  # it's remove first element only in list we pass the element along with pop method which we want to remove
# print(dir(set1))


# set2.clear() #it's remove all the elemetn from the set
set1 = {1, 2, 3}
set2 = {1, 1, 1, 2, 3, 3, 4, 5}
set1.add(100)
set1.add(90)
# print(set1)

# print(set1 - set2)
# setz = {
#     [
#         1,
#         2,
#         3,
#         4,
#     ],
#     [5, 6, 7, 8],
# }
# print(setz) #we can't store list in set

setx = {(1, 2, 3), (5, 6, 7)}
# print(setx)  # we can store tuple inside a set


# setA = {1, 2, 3, 4}
# setB = {4, 5, 6, 7, 8, 9}
# it includes both the elements of both the set without including duplicate values
# print(setA.union(setB))


setC = {1, 2, 3, 4, 5}
setD = {1, 2, 3, 11, 12, 13}

setZ = setC.intersection(setD)
# it only returns the common elements of both sets   without including duplicate values
# print(setZ)


# print({100, 200, 300, 400}.difference({100, 1000, 2000, 200, 300}))


# various operation in set
setA = {1, 2, 5}
# setA.add(4)
# print(setA)

# removing elements(remove)
# setA.remove(100)
# print(setA)

# removing elements(discard)
# setA.discard(100) # it won't throw any error if the value is not present there
# print(setA)

# clearing a set
# setA.clear()
# print(setA)

#! union
setA = {1, 2, 5}
setB = {5, 6, 7}
# setC = setA.union(setB) #it will return all values from setA and setB excluding duplicate values
# print(setC)

#! intersection
setA = {1, 2, 5}
setB = {5, 6, 7}

# setC = setA.intersection(setB) # it will return only the common elements from both the sets
# print(setC)

#! Difference
setA = {1, 2, 5}
setB = {5, 6, 7}

# setC = setA.difference(setB) # difference returns only from the first set and returns only elements which is not present in second set.
print(setC)
