# Animal is-a object
class Animal(object):
    pass
    
# class Dog is-a Animal
class Dog(Animal):
    def __init__(self,name):
        #Dog has an attribute
        self.name = name
        
# class cat is-a Animal
class Cat(Animal):
    def __init__(self,name):
        #cat has-a attribute
        self.name = name
        
# Person is-a object class
class Person(object):
    def __init__(self,name):#(self,name, petname): # my dummy way
        #person has-a name attribute
        self.name = name
        #self.pet = petname# my dummy way
        
        # person has-a pet name attribute
        self.pet = None
        
#class Employee is-a Person
class Employee(Person):
     def __init__(self,name,salary):
        # call the parent function to initialize the name attribute
        super(Employee,self).__init__(name)
        # employee has-a attribute called salary
        self.salary = salary
        
# Fish is-a object
class Fish(object):
    pass
    
# Salmon is-a Fish
class Salmon(Fish):
    pass
    
#Halibut is-a Fish
class Halibut(Fish):
    pass
    
# rover is-a dog
rover = Dog("Rover")

# satan is-a cat
satan = Cat("Satan")

print type(satan)

# Mary is an instance of person
#mary = Person("Mary","satan")#my dummy way
mary = Person("Mary")
# Set mary pet attribute to satan
mary.pet = satan   # by doing this, not only string, but all the attributes of satan are assigned to mary.pet 
print str(mary.pet)
#print type(mary.pet)

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()
