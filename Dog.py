from Animal import Animal


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name, breed)

    def speaks(self):
        print(f"{self.name} barks")


d = Dog("Rocky", "Labradore")
d.speaks()

# super() this keyword is use to call the parent class

# method overRiding
# if child class and parent class have same class method then it will give priority to child class method this concept called method overRiding.
