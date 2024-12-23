# Oops in python
# to map with real world scenarios, we started using objects in code.

# why we use oops in programming==>
# Object-Oriented Programming (OOP) helps organize and simplify code by breaking complex systems into smaller, manageable "objects."

# first we were using procedural programming then it comes functional programming to increase the reusability of the code and lower the redundancy of the code after it comes object oriented programming it makes our program more reusable

# classes and objects
# class is a blueprint for creating objects.
# suppose we have to build a house first we create a blueprint or template it defines the structure of the house no. of rooms,doors and windows.


# creating class with 'class' keyword followed by classname.
class Student:
    # initializing constructor function --> All classes have a function called __init__(), which is always executed when the object of the class is being initialized. it always takes a parameter 'self' as a first parameter.
    # self parameter is basically refers to the newly created object of the class, and it is used to access the variables that belongs to the class.

    home = "Bihar"  # this is constant for everybody in the class it will occupy memory only one time,this is called class attribute.

    def __init__(self, name, age):
        # print(
        #     "This is Constructor function it always executes whenever an object is initialize,if a programmer does not define constructor function the interpreter automatically create the init function."
        # )
        self.name = name  # this name variable will occupy memory space evrytime a new object will be created, so whenever something will not be same we use self keyword to point to the newly created objject, this is called object attribute.
        self.age = age  # this name variable will occupy memory space evrytime a new object will be created, so whenever something will not be same we use self keyword to point to the newly created objject,this is called object attribute.

    # method inside the class --> methods are functions that belongs to objects.
    def Welcome(self):
        print("Welcome Champ", self.name)

    def getAge(self):
        return self.age


# objects
# An object is the actual house built using the blueprint.
# you can build many houses(objects) from the same blueprint each with its own unique features like colors or size.

s = Student(
    "Sahil", 23
)  # creating first object of the class and passing arguments name and age of the new object

# print(s.name, s.age)
# s.Welcome()
# print(s.getAge())
# print(s.home)


# let's Practice
# create a student class that takes name and marks of 3 subjects as arguments in constructor,then create a method to print the average.


# class Student:

#     def __init__(self, name, maths_marks, science_marks, english_marks):
#         self.name = name
#         self.maths_marks = maths_marks
#         self.science_marks = science_marks
#         self.english_marks = english_marks

#     def getAvg(self):
#         avg = self.english_marks + self.maths_marks + self.science_marks / 3
#         print(f"Average of student {self.name} is: ", avg)


# s1 = Student("Sahil", 56, 70, 77)
# s1.getAvg()


# static method
# methods that don't use the self parameter
# Decorator in python -> decorators allow us to wrap another function  in order to extend the behaviour of the wrapped function without permanently modifying it.


# class College:
#     def __init__(self, name, location):
#         self.name = name
#         self.location = location
#         print(f"The name of the college is {name} and it's location is {location}")

#     # This is a static method, defined using the @staticmethod decorator.
#     # this is called decorator it allows us to write a function without passing self parameter.
#     @staticmethod
#     def Teacher():
#         print("Hello from teacher!")


# c = College("Happy College", "Siwan")

# c.Teacher()


# Abstraction
# Hiding the implementation  details of a class and only showing the essential features to the user.

# Real-World Example of Abstraction:

# Think of a car dashboard:

# When you drive a car, you interact with the steering wheel, accelerator, brake, and gear shift.
# You don’t need to know how the engine, fuel injection system, or braking mechanism works internally.
# In programming terms:

# The controls on the dashboard are the abstracted interface (essential features).
# The complex internal systems of the car are hidden implementation details.
# This allows the user to focus on driving without worrying about the underlying technicalities.


# class Car:
#     def __init__(self):
#         self.accelerator = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.accelerator = True
#         self.clutch = True
#         print("The car is started...")


# car1 = Car()
# car1.start()


# Encapsulation
# wrapping data and functions into a single unit(object) called Encapsulation
# suppose it is as we make a capsule in that capsule we put data and functtion inside it this process called encapsulation.

# all the codes we were writing so far is the example of encapsulation.

# example- >
# class Student:

#     def __init__(self, name, maths_marks, science_marks, english_marks):
#         self.name = name
#         self.maths_marks = maths_marks
#         self.science_marks = science_marks
#         self.english_marks = english_marks

#     def getAvg(self):
#         avg = self.english_marks + self.maths_marks + self.science_marks / 3
#         print(f"Average of student {self.name} is: ", avg)


# s1 = Student("Sahil", 56, 70, 77)
# s1.getAvg()


# let's practice
# create account class with 2 attributes balance and account number
# create a method for debit , credit and printing the balance


# class Account:
#     def __init__(self, acc, bal):
#         self.account_number = acc
#         self.balance = bal

#     # debit method
#     def debit(self, amount):
#         self.balance -= amount
#         print(f"Rs {amount} is debited from account ")
#         print("total balance=", self.get_balance())

#     # credit method
#     def credit(self, amount):
#         self.balance += amount
#         print(f"Rs {amount} is credited from account ")
#         print("total balance=", self.get_balance())

#     def get_balance(self):
#         return self.balance


# acc1 = Account(12000, 897878)
# acc1.debit(2000)
# # acc1.credit()
# acc1.get_balance()

# del keyword
# used to  delete  object properties or object itself.

# class Student:
#     def __init__(self, name):
#         self.name = name


# s1 = Student("Sahil")
# print(s1.name)

# del s1.name
# print(s1.name)


# private attributes and methods
# private attributes and methods are meant to be used only within the class and are not accessible from outside the class.
# we put __ before the attributes and methods to make it private in python.


# class Account:
#     def __init__(self, account_no, account_pass):
#         self.acc_no = account_no
#         # now we can't access account_pass out of this class
#         self.__acc_pass = account_pass

#     def reset_pass(self):
#         print(self.__acc_pass)


# a1 = Account(12345, 54321)
# print(a1.acc_no)  # this is not the recommended for sensitive data handling.
# a1.reset_pass()


# class Person:
#     __name = "Sahil"

# making method as private
#     def __hello(self):
#         print("hello person")

#     def welcome(self):
#         self.__hello()


# p1 = Person()
# print(p1.welcome())

# Inheritance
# when one class derives the properties and method  of another class.


class Car:
    color = "Blue"

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped..")


class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name
        print(self.name)


# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Prius")
# print(car1.color)

# types of inheritance
# 1. Single Inheritance
# 2. Multi-level inheritance
# 3. Multiple inheritance


# 1. Single Inheritance -> in this tyoe of inheritance there is one base class and one derived class.
# class Car:
#     color = "Blue"

#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car stopped..")


# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name
#         print(self.name)

# 2. Multi-level inheritance -> in this type of inheritance there is one base class that will pass on its properties and method to a child class and then this child class pass on its and its parent class properties and behaviour to another child class.


class Car:

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped..")


class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand
        print(self.brand)


class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type
        print(self.type)


fortuner1 = Fortuner("Diesel")
# print(fortuner1.brand)
fortuner1.start()  # there won't be any error because it will inherit the start( method) from it's parent class
