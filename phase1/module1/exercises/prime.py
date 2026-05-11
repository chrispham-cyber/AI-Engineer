num = int(input("Integer Number = "))
isPrime = True

for i in range(2, int(num ** 0.5)+1):
	if num % i == 0:
		isPrime = False
		break

print(f"{num} is a prime number.") if isPrime else print(f"{num} is not a prime number.")
