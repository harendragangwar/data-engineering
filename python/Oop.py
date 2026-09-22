# 1. CLASS AND OBJECT
class Student:
    # Class attribute
    college = "GLA University"

    # Constructor
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("College:", self.college)


# Creating objects
student1 = Student("Himanshu", 22)
student2 = Student("Rahul", 21)

student1.introduce()
student2.introduce()

# 2. INSTANCE ATTRIBUTES VS CLASS ATTRIBUTES

class Car:
    wheels = 4  # Class attribute

    def __init__(self, brand, model):
        self.brand = brand  # Instance attribute
        self.model = model  # Instance attribute


car1 = Car("Toyota", "Fortuner")
car2 = Car("Honda", "City")

print(car1.brand)
print(car2.brand)

print(car1.wheels)
print(car2.wheels)

# 3. INSTANCE METHOD

class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)


person1 = Person("Himanshu")
person1.show_name()

# 4. CONSTRUCTOR __init__()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(self.name, self.salary)


employee1 = Employee("Himanshu", 50000)
employee1.show_details()

# 5. self
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)
        print(self.age)


s1 = Student("Himanshu", 22)
s1.show()

# 6. CLASS METHOD

class Employee:
    company = "Google"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


print(Employee.company)

Employee.change_company("Microsoft")

print(Employee.company)

# 7. STATIC METHOD
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print(Calculator.add(10, 20))
print(Calculator.multiply(5, 4))

# 8. INSTANCE + CLASS + STATIC METHODS

class Student:
    college = "GLA University"

    def __init__(self, name):
        self.name = name

    # Instance method
    def show_name(self):
        print(self.name)

    # Class method
    @classmethod
    def show_college(cls):
        print(cls.college)

    # Static method
    @staticmethod
    def welcome():
        print("Welcome to Python")


s1 = Student("Himanshu")

s1.show_name()
Student.show_college()
Student.welcome()

# 9. ENCAPSULATION

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.balance)


account = BankAccount(10000)

account.deposit(5000)
account.withdraw(3000)
account.show_balance()

# 10. PUBLIC VARIABLE

class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("Himanshu")

print(s1.name)

# 11. PROTECTED VARIABLE

class Student:

    def __init__(self, name):
        self._name = name


s1 = Student("Himanshu")

print(s1._name)

# 12. PRIVATE VARIABLE

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print(self.__balance)


account = BankAccount(10000)

account.show_balance()

# This will not work directly:
# print(account.__balance)

# 13. NAME MANGLING
class Student:

    def __init__(self, name):
        self.__name = name


s1 = Student("Himanshu")

# Python internally changes __name to _Student__name
print(s1._Student__name)

# 14. GETTER AND SETTER

class Student:

    def __init__(self, age):
        self.__age = age

    # Getter
    def get_age(self):
        return self.__age

    # Setter
    def set_age(self, age):
        if age > 0:
            self.__age = age


s1 = Student(22)

print(s1.get_age())

s1.set_age(23)

print(s1.get_age())

# 15. PROPERTY DECORATOR
class Student:

    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value


s1 = Student(22)

print(s1.age)

s1.age = 23

print(s1.age)

# 16. INHERITANCE
class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()

# 17. SINGLE INHERITANCE
class Parent:

    def show_parent(self):
        print("Parent class")


class Child(Parent):

    def show_child(self):
        print("Child class")


obj = Child()

obj.show_parent()
obj.show_child()

# 18. MULTILEVEL INHERITANCE
class GrandParent:

    def grandparent_method(self):
        print("Grandparent")


class Parent(GrandParent):

    def parent_method(self):
        print("Parent")


class Child(Parent):

    def child_method(self):
        print("Child")


obj = Child()

obj.grandparent_method()
obj.parent_method()
obj.child_method()


# 19. MULTIPLE INHERITANCE
class Father:

    def father_method(self):
        print("Father")


class Mother:

    def mother_method(self):
        print("Mother")


class Child(Father, Mother):

    def child_method(self):
        print("Child")


obj = Child()

obj.father_method()
obj.mother_method()
obj.child_method()


# 20. HIERARCHICAL INHERITANCE

class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")


class Cat(Animal):

    def meow(self):
        print("Meowing")


dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()


# ============================================================
# 21. HYBRID INHERITANCE
# ============================================================

class A:

    def method_a(self):
        print("A")


class B(A):

    def method_b(self):
        print("B")


class C(A):

    def method_c(self):
        print("C")


class D(B, C):

    def method_d(self):
        print("D")


obj = D()

obj.method_a()
obj.method_b()
obj.method_c()
obj.method_d()


# ============================================================
# 22. METHOD OVERRIDING
# ============================================================

class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


animal = Animal()
dog = Dog()

animal.sound()
dog.sound()


# ============================================================
# 23. super()
# ============================================================

class Parent:

    def __init__(self):
        print("Parent constructor")


class Child(Parent):

    def __init__(self):
        super().__init__()
        print("Child constructor")


obj = Child()


# ============================================================
# 24. super() WITH ATTRIBUTES
# ============================================================

class Parent:

    def __init__(self):
        self.name = "Parent"


class Child(Parent):

    def __init__(self):
        super().__init__()
        self.age = 22


obj = Child()

print(obj.name)
print(obj.age)


# ============================================================
# 25. POLYMORPHISM
# ============================================================

class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


def make_sound(animal):
    animal.sound()


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)


# ============================================================
# 26. DUCK TYPING
# ============================================================

class Dog:

    def sound(self):
        print("Bark")


class Person:

    def sound(self):
        print("Hello")


def make_sound(obj):
    obj.sound()


make_sound(Dog())
make_sound(Person())


# ============================================================
# 27. METHOD OVERLOADING
# ============================================================
# Python does not support traditional method overloading.
# We can achieve similar behavior using default arguments.


class Calculator:

    def add(self, a, b=0, c=0):
        return a + b + c


calc = Calculator()

print(calc.add(10))
print(calc.add(10, 20))
print(calc.add(10, 20, 30))


# ============================================================
# 28. OPERATOR OVERLOADING
# ============================================================

class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)


num1 = Number(10)
num2 = Number(20)

result = num1 + num2

print(result.value)


# ============================================================
# 29. COMMON MAGIC / DUNDER METHODS
# ============================================================

class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student: {self.name}"

    def __len__(self):
        return len(self.name)


s1 = Student("Himanshu")

print(s1)
print(len(s1))


# ============================================================
# 30. __eq__() - EQUALITY
# ============================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


s1 = Student("Himanshu", 22)
s2 = Student("Himanshu", 22)

print(s1 == s2)


# ============================================================
# 31. __lt__() - LESS THAN
# ============================================================

class Student:

    def __init__(self, marks):
        self.marks = marks

    def __lt__(self, other):
        return self.marks < other.marks


s1 = Student(70)
s2 = Student(80)

print(s1 < s2)


# ============================================================
# 32. __gt__() - GREATER THAN
# ============================================================

class Student:

    def __init__(self, marks):
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks


s1 = Student(90)
s2 = Student(80)

print(s1 > s2)


# ============================================================
# 33. ABSTRACT CLASS
# ============================================================

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


dog = Dog()

dog.sound()


# ============================================================
# 34. ABSTRACT CLASS WITH NORMAL METHOD
# ============================================================

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Vehicle stopped")


class Car(Vehicle):

    def start(self):
        print("Car started")


car = Car()

car.start()
car.stop()


# ============================================================
# 35. ABSTRACT CLASS CANNOT CREATE OBJECT
# ============================================================

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


# This will give an error:
# animal = Animal()


# ============================================================
# 36. COMPOSITION
# ============================================================

class Engine:

    def start(self):
        print("Engine started")


class Car:

    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car started")


car = Car()

car.start_car()


# ============================================================
# 37. AGGREGATION
# ============================================================

class Teacher:

    def __init__(self, name):
        self.name = name


class School:

    def __init__(self, teacher):
        self.teacher = teacher

    def show_teacher(self):
        print(self.teacher.name)


teacher = Teacher("Rahul")

school = School(teacher)

school.show_teacher()


# ============================================================
# 38. IS-A RELATIONSHIP
# ============================================================

class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

print(isinstance(dog, Animal))
print(isinstance(dog, Dog))


# ============================================================
# 39. HAS-A RELATIONSHIP
# ============================================================

class Engine:
    pass


class Car:

    def __init__(self):
        self.engine = Engine()


car = Car()

print(isinstance(car.engine, Engine))


# ============================================================
# 40. isinstance()
# ============================================================

class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))


# ============================================================
# 41. issubclass()
# ============================================================

class Animal:
    pass


class Dog(Animal):
    pass


print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))


# ============================================================
# 42. MRO - METHOD RESOLUTION ORDER
# ============================================================

class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        print("B")


class C(A):

    def show(self):
        print("C")


class D(B, C):
    pass


obj = D()

obj.show()

print(D.mro())


# ============================================================
# 43. DIAMOND INHERITANCE
# ============================================================

class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        print("B")


class C(A):

    def show(self):
        print("C")


class D(B, C):

    pass


obj = D()

obj.show()

print(D.__mro__)


# ============================================================
# 44. NESTED CLASS
# ============================================================

class Outer:

    class Inner:

        def show(self):
            print("Inside Inner class")


obj = Outer.Inner()

obj.show()


# ============================================================
# 45. OBJECT ATTRIBUTES
# ============================================================

class Student:

    college = "GLA"

    def __init__(self, name):
        self.name = name


s1 = Student("Himanshu")

print(s1.__dict__)


# ============================================================
# 46. CLASS __dict__
# ============================================================

class Student:

    college = "GLA"

    def __init__(self, name):
        self.name = name


print(Student.__dict__)


# ============================================================
# 47. DYNAMIC ATTRIBUTE
# ============================================================

class Student:
    pass


s1 = Student()

s1.name = "Himanshu"
s1.age = 22

print(s1.name)
print(s1.age)


# ============================================================
# 48. DELETE ATTRIBUTE
# ============================================================

class Student:

    def __init__(self, name):
        self.name = name


s1 = Student("Himanshu")

print(s1.name)

del s1.name

# This will give an error:
# print(s1.name)


# ============================================================
# 49. __del__
# ============================================================

class Student:

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("Object destroyed")


s1 = Student("Himanshu")

del s1


# ============================================================
# 50. FINAL COMPLETE OOPS EXAMPLE
# ============================================================

from abc import ABC, abstractmethod


class Employee(ABC):

    company = "Tech Company"

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    # Encapsulation
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self.__salary = value

    # Abstract method
    @abstractmethod
    def work(self):
        pass

    # Instance method
    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self.__salary)
        print("Company:", self.company)

    # Class method
    @classmethod
    def change_company(cls, name):
        cls.company = name

    # Static method
    @staticmethod
    def company_policy():
        print("Work honestly")


class Developer(Employee):

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    # Method overriding
    def work(self):
        print(self.name, "is writing", self.language, "code")


class DataEngineer(Employee):

    def __init__(self, name, salary, tool):
        super().__init__(name, salary)
        self.tool = tool

    # Method overriding
    def work(self):
        print(self.name, "is working with", self.tool)


developer = Developer("Himanshu", 60000, "Python")

data_engineer = DataEngineer("Rahul", 70000, "PySpark")

developer.show_details()
developer.work()

data_engineer.show_details()
data_engineer.work()

Employee.change_company("New Company")

print(developer.company)

Employee.company_policy()