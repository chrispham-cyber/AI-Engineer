inpDict = {"a": 1, "b": 2, "c": 3}
result = {}

"""The most optimized solution
result = {v: k for k, v in inpDict.items()}"""

for k, v in inpDict.items():
    result[v] = k

print(result)
