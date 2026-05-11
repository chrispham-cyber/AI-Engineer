# Basics 

## Variable & Data Type
```
# integer
age = 18

# float
height = 1.93

# string
name = "Spidey"

# boolean
is_god = False

# none (null)
Result = None
```

**Rules:** `snake_case` like total_amount, average_grade

## Operators
```
print(10 + 3)    # 13
print(10 - 3)    # 7
print(10 * 3)    # 30
print(10 / 3)    # 3.333... (always returns a float)
print(10 // 3)   # 3 (integer division)
print(10 % 3)    # 1 (modulo/remainder)
print(10 ** 3)   # 1000 (exponentiation)

# Assignment
x = 10
x += 5    # x = x + 5
x -= 2    # x = x - 2
x *= 3    # x = x * 3

# Comparison (returns a boolean)
print(5 > 3)    # True
print(5 == 5)   # True (comparison, not assignment)
print(5 != 3)   # True
print(5 >= 5)   # True

# Logic
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# Membership
print("a" in "apple")   # True
print(3 in [1, 2, 3])   # True
```

## F-string
```
price = 100
tax = 0.1
print(f"Sum: ${price * (1 + tax):.2f}")
```

## Digit Format
```
print(f"{pi:.4f}")   # 3.1416
print(f"{1000000:,}") # 1,000,000

# Padding
print(f"{42:>5}")    # "   42" (right align, width 5)
print(f"{42:<5}|")   # "42   |"
print(f"{42:^5}|")   # " 42  |"
```

## String Methods
```
text = "  Hello World  "

text.strip()              # "Hello World" (removes whitespace)
text.lower()              # "  hello world  "
text.upper()              # "  HELLO WORLD  "
text.replace("World", "AI")  # "  Hello AI  "
text.split()              # ["Hello", "World"]
"-".join(["a", "b", "c"]) # "a-b-c"

text.startswith("  H")    # True
text.endswith("d  ")      # True
"Python" in text          # False
len(text)                 # 15

# Counting
"banana".count("a")       # 3

# Finding position
"banana".find("na")       # 2 (first occurrence)
"banana".find("xyz")      # -1 (not found)
```

## Input
```
age = int(input("Age: "))
```

## Conditions
```
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

status = "Pass" if score >= 50 else "Failed"
```

## Loop with `for`
```
# 0 to 4
for i in range(5):
    print(i)
# 0 1 2 3 4

# 1 to 5
for i in range(1, 6):
    print(i)

# 0, 2, 4, 6, 8
for i in range(0, 10, 2):
    print(i)

# 5, 4, 3, 2, 1
for i in range(5, 0, -1):
    print(i)
```

### Iterable Loop
```
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

#  string
for char in "Python":
    print(char)
# P y t h o n
```

### `zip`
```
for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

### break & continue
```
# break: exit the loop
for i in range(10):
    if i == 5:
        break
    print(i)
# 0 1 2 3 4

# continue: skip iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# 1 3 5 7 9
```

## Comments
```
# 1 line comment

"""
multiple lines
comment
"""
```

## Exercises
### [FizzBuzz](exercises/.py)
### [BMI](exercises/.py)
### [Vowels](exercises/.py)
### [Prime](exercises/.py)
### [Reverse String](exercises/.py)
