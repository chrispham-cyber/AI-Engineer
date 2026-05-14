# Object-Oriented Programming

## Class
```
class Dog: 
	def __init__(self, name: str, age: int): 
		self.name = name 
		self.age = age 

	# Method 
	def bark(self): 
		print(f"{self.name} says Woof!") 

	def info(self): 
		return f"{self.name} is {self.age} years old"

# Create instance
buddy = Dog("Buddy", 3)
charlie = Dog("Charlie", 5)

# Access attributes
print(buddy.name) # "Buddy"
print(charlie.age) #5

# Call method
buddy.bark() # "Buddy says Woof!"
print(charlie.info()) # "Charlie is 5 years old"
```

## Class Variables vs Instance Variables
```
class Dog:
	# Class variable — shared among all objects (instances)
	species = "Canis lupus familiaris"

	def __init__(self, name, age):
		# Instance variable — unique to each specific object
		self.name = name
		self.age = age

buddy = Dog("Buddy", 3)
charlie = Dog("Charlie", 5)

print(buddy.species) # "Canis lupus familiaris"
print(charlie.species) # "Canis lupus familiaris"

# Modifying the class variable
Dog.species = "Dog"
print(buddy.species) # "Dog" (both objects reflect the change)
```

# Encapsulation — Public, Protected, Private

Python does not have true private members; instead, it relies on protected.

```
class BankAccount: 
	def __init__(self, owner: str, balance: float): 
		self.owner = owner # public 
		self._balance = balance # protected (convention: internal) 
		self.__pin = "1234" # "private" (name mangling) 

	def get_balance(self) -> float: 
		return self._balance 

	def deposit(self, amount: float): 
		if amount > 0: 
		self._balance += amount

acc = BankAccount("Ian", 1000)
print(acc.owner) # "Ian"
print(acc._balance) # 1000 (accessible, but "don't")
# print(acc.__pin) # AttributeError
print(acc._BankAccount__pin) # "1234" (still accessible if tried)
```
Rule: `_name` = "don't touch; can be changed later". `__name` = name mangling (rarely used).

# Dunder methods
```
classPoint: 
	def __init__(self, x: float, y: float): 
		self.x = x 
		self.y = y 

	# Print out string 
	def __str__(self): 
		return f"Point({self.x}, {self.y})" 

	# For debugging 
	def __repr__(self): 
		return f"Point(x={self.x}, y={self.y})" 

	# Compare == 
	def __eq__(self, other): 
		if not isinstance(other, Point): 
		returnNotImplemented 
		return self.x == other.x and self.y == other.y 

	# Addition + 
	def __add__(self, other): 
		return Point(self.x + other.x, self.y + other.y) 

	# Allow len() 
	def __len__(self): 
		return 2 

	# Hash → can be used as key dict, set 
	def __hash__(self): 
		return hash((self.x, self.y))

p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1) # Point(1, 2)
print(p1 == Point(1, 2)) # True
print(p1 + p2) # Point(4, 6)
print(len(p1)) #2

# Used as key
points = {p1: "first", p2: "second"}
```

### Top dunder methods

| Method | Used for |
|--------|---------|
| `__init__` | init |
| `__str__` | `print(obj)` (user-friendly) |
| `__repr__` | `repr(obj)` (debug) |
| `__eq__` | `obj1 == obj2` |
| `__lt__` | `<` |
| `__hash__` | key |
| `__len__` | `len(obj)` |
| `__iter__` | `for x in obj` |
| `__next__` | iterator |
| `__getitem__` | `obj[i]` |
| `__contains__` | `x in obj` |
| `__call__` | `obj()` (callable) |

# Inheritance 
```
class Animal: 
	def __init__(self, name: str): 
		self.name = name 

	def speak(self): 
		print(f"{self.name} makes a sound")

class Dog(Animal): # Dog inherits Animal 
	def speak(self): # override 
		print(f"{self.name} says Woof!") 

	def fetch(self): # new method 
		print(f"{self.name} fetches the ball")

class Puppy(Dog): # Multi-level 
	def __init__(self, name: str, age: int): 
		super().__init__(name) # call parent's __init__ 
		self.age = age 

	def speak(self): 
		super().speak() # call method parent 
		print("(in a tiny voice)")

buddy = Dog("Buddy")
buddy.speak() # Buddy says Woof!
buddy.fetch() # Buddy fetches the ball

mini = Puppy("Mini", 1)
mini.speak() # Mini says Woof! (in a tiny voice)
```

### isinstance & issubclass
| Funcion                  | Check if                          |
| ------------------------ | --------------------------------- |
| `isinstance(obj, cls)`   | Object belongs to which class?    |
| `issubclass(cls1, cls2)` | Class inherit from another class? |

## Properties 

## @classmethod và @staticmethod

## Dataclasses

## Pydantic
