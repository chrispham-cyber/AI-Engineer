weight = float(input("Weight (kg) = "))
height = float(input("Height (m) = "))

bmi = weight / (height ** 2)

if bmi < 18.5:
	print("Slim")
elif bmi < 25:
	print("Normal")
elif bmi < 30:
	print("Fat")
else:
	print("Obesity")
