import re
from collections import Counter

text = input("String = ")

words = re.findall(r"[a-zA-Z]+", text.lower())

res = Counter(words).most_common(3)

print(res)
