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

    home = "Bihar"  # this is constant for everybody in the class it will occupy memory only one time.

    def __init__(self, name, age):
        print(
            "This is Constructor function it always executes whenever an object is initialize,if a programmer does not define constructor function the interpreter automatically create the init function."
        )
        self.name = name  # this name variable will occupy memory space evrytime a new object will be created, so whenever something will not be same we use self keyword to point to the newly created objject.
        self.age = age  # this name variable will occupy memory space evrytime a new object will be created, so whenever something will not be same we use self keyword to point to the newly created objject.

    # second method inside the class
    def PersonDetails():
        print("This is from person details")


# objects
# An object is the actual house built using the blueprint.
# you can build many houses(objects) from the same blueprint each with its own unique features like colors or size.

s = Student(
    "Sahil", 23
)  # creating first object of the class and passing arguments name and age of the new object
print(s.name, s.age)

print(s.home)
