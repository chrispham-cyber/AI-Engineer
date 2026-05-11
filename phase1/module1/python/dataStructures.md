# Data Structures

## List
```
# Create
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
empty = []

# Access (starts from index 0)
print(fruits[0]) # "apple"
print(fruits[-1]) # "orange" (negative index = from the end)

# Modify
fruits[0] = "mango"

# Add
fruits.append("melon") # end: ["mango", "banana", "orange", "melon"]
fruits.insert(1, "guava") # position 1: ["mango", "guava", "banana", "orange", "melon"]
fruits.extend(["kiwi", "grape"]) # multiple elements

# Remove
fruits.remove("banana") # remove by value
last = fruits.pop() # remove last + return value
first = fruits.pop(0) # remove at position 0
del fruits[0] # remove by index
fruits.clear() # remove all

# Search
fruits = ["apple", "banana", "orange", "banana"]
print(fruits.index("banana")) # 1 (first occurrence)
print(fruits.count("banana")) # 2

# Sort
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort() # modifies original list: [1, 1, 2, 3, 4, 5, 9]
numbers.sort(reverse=True) # descending order
sorted_nums = sorted(numbers) # creates a new list; does not modify original Original

# Reverse
nums.reverse()
reversed_nums = nums[::-1] # Create a reversed copy
```

## Slicing
```
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nums[2:5]      # [2, 3, 4]   (from index 2 up to, but not including, 5)
nums[:5]       # [0, 1, 2, 3, 4]
nums[5:]       # [5, 6, 7, 8, 9]
nums[:]        # [0..9] (copy the entire list)
nums[::2]      # [0, 2, 4, 6, 8] (step of 2)
nums[::-1]     # [9..0] (reversed)
nums[1::2]     # [1, 3, 5, 7, 9] (odd indices)
```

## List Comprehension 
```
# Traditional
squares = []
for x in range(10):
	squares.append(x ** 2)

# Pythonic
squares = [x ** 2 for x in range(10)]

# Conditional
evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Transformation
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
# ["HELLO", "WORLD", "PYTHON"]

# Nested (be careful, don't make it too complex)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Tuple
```
# Creation
point = (3, 4)
empty = ()

# Access (same as lists)
print(point[0])      # 3
print(point[-1])     # 4

# Cannot be modified

# Unpacking
x, y = point
print(x, y)          # 3 4

# Swapping
a, b = 1, 2
a, b = b, a          # Swap without a temporary variable

# Functions returning multiple values
def get_min_max(nums):
	return min(nums), max(nums)

lo, hi = get_min_max([3, 1, 4, 1, 5])
print(lo, hi)        # 1 5
```

### When to apply?
- Immutable data: coordinates (x, y), RGB color (r, g, b)
- Used as dictionary keys (lists cannot be used as keys)
- Returning multiple values from a function

## Dict
The Dict (hash map) is the most important data structure in Python.

```
# Creation
person = {
	"name": "Lan",
	"age": 25,
	"skills": ["Python", "ML"]
}

# Accessing
print(person["name"])           # "Lan"

# Modifying / Adding
person["age"] = 26
person["city"] = "Hà Nội"      # add new key-value pair

# Deleting
del person["city"]
removed = person.pop("age")     # delete + return value

# Checking
"name" in person                # True

# Iterating
for key in person:              # iterate over keys
	print(key)

for key, value in person.items():
	print(f"{key}: {value}")

for value in person.values():
	print(value)

# Dict comprehension
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Counting frequency
text = "hello world"
freq = {}
for char in text:
	freq[char] = freq.get(char, 0) + 1
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ...}

# A more standard approach:
from collections import Counter
freq = Counter(text)
```

### Merge dicts
```
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}

merged = a | b              # {"x": 1, "y": 3, "z": 4} (b ghi đè a)

# OR
merged = {**a, **b}
```

## Set
```
# Creation
s = {1, 2, 3, 4}
empty = set()              # ⚠️ {} is an empty dict, not an empty set

# From a list (removes duplicates)
nums = [1, 2, 2, 3, 3, 3, 4]
unique = set(nums)         # {1, 2, 3, 4}

# Add / Remove
s.add(5)
s.remove(1)        # KeyError if not present
s.discard(100)     # No error if not present

# Membership testing (extremely fast — O(1))
3 in s             # True

# Set operations
a = {1, 2, 3}
b = {2, 3, 4}

a | b              # union: {1, 2, 3, 4}
a & b              # intersection: {2, 3}
a - b              # difference: {1}
a ^ b              # symmetric diff: {1, 4}
```

### When to apply?
- Remove duplicates from a list
- Fast membership testing 
- Set operations (intersection, union, etc.)

## Which one?
**List:** Ordered data; supports adding, removing, and modifying elements.
```python
todo_list = ["milk", "gym"]
```

**Tuple:** Fixed data; immutable.
```python
position = (10.5, 20.3)
```

**Dict:** Maps keys to values.
```python
user_db = {"u001": {"name": "Ian"}, "u002": {"name": "Henry"}}
```

**Set:** Used for membership testing and removing duplicates.
```python
visited_pages = {"home", "about", "contact"}
```

## Useful Functions
```
nums = [3, 1, 4, 1, 5, 9, 2, 6]

len(nums)       # 8
sum(nums)       # 31
min(nums)       # 1
max(nums)       # 9
sorted(nums)    # [1, 1, 2, 3, 4, 5, 6, 9]

# zip
names = ["Ian", "Henry"]
ages = [25, 30]
list(zip(names, ages))  # [("Ian", 25), ("Henry", 30)]
```

## Exercises
- [Find the Unique Element](../exercises/.py)
- [Reverse a dictionary](../exercises/.py)
- [Top 3 Most Frequent Words](../exercises/.py)
- [Two numbers whose sum equals the target.](../exercises/.py)
