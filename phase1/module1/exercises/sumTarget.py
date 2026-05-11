numbs = list(map(int, input("Numbers = ").split()))
target = int(input("Target = "))

'The most optimized solution'
"""def two_sum(nums, target):
    seen = {}  
    
    for i, num in enumerate(nums):
        complement = target - num  
        
        if complement in seen:
            return (numbs[seen[complement]], num)  
        
        seen[num] = i  
    
    return None  """

for i in range (len(numbs) - 1):
	for j in range(i + 1, len(numbs)):
		if numbs[i] + numbs[j] == target:
			print(f"({numbs[i]}, {numbs[j]})")
			break
