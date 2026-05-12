# Functions

## Function Definition
```
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def get_users() -> list[dict]:
    return [{"name": "Ian"}, {"name": "Henry"}]
```

### Why should we use `type hints`?
- VS Code/Pylance autocomplete is better
- Catch bugs easier
- Code is easier to read 

## Arguments
```
def magic(positional, *args, default="hi", **kwargs):
    print(f"positional: {positional}")
    print(f"args: {args}")
    print(f"default: {default}")
    print(f"kwargs: {kwargs}")

magic("a", 1, 2, 3, default="hello", x=100, y=200)
# positional: a
# args: (1, 2, 3)		 Tuple inside func
# default: hello
# kwargs: {'x': 100, 'y': 200}   Dict inside func
```

## Return values
```
def stats(nums: list[float]) -> tuple[float, float, float]:
    return min(nums), max(nums), sum(nums) / len(nums)

lo, hi, avg = stats([1, 2, 3, 4, 5])
```

## Lambda
```
square = lambda x: x ** 2
list(map(lambda x: x * 2, nums))       # [2, 4, 6, 8, 10]
list(filter(lambda x: x > 2, nums))    # [3, 4, 5]
```

## Scope
```
x = 10                # global

def outer():
    y = 20            # enclosing
    
    def inner():
        z = 30        # local
        print(x, y, z)
    
    inner()

outer()    # 10 20 30
```

### LEGB Rule

Python searches for variables in order: Local → Enclosing → Global → Built-in

## Important Build-in modules
```
import os                    # file system
import sys                   # system, argv
import json                  # JSON
import datetime              # date, time
import random                # random
import re                    # regex
from pathlib import Path     # path (modern)
from collections import Counter, defaultdict, deque
```

## Exercises
