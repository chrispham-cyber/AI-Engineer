vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

text = input("String = ")

for ch in text.strip():
	if ch.lower() in vowels:
		count += 1

print(count)
