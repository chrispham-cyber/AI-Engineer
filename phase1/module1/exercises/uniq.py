"The most optimized solution"

"""from collections import Counter

numbs = list(map(int, input("Array = ").split(" ")))
result = []
freq = Counter(numbs)

result = [x for x, count in freq.items() if count == 1]
print(result)"""

numbs = list(map(int, input("Array = ").split(" ")))
result = []
freq = {}

for n in numbs:
    freq[n] = freq.get(n, 0) + 1

for key in freq:
    if freq.get(key) == 1:
        result.append(key)

print(result)
