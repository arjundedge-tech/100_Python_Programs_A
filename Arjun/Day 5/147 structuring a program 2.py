# 1. input
text = input("Temperature in Fahrenheit: ")

# 2. convert
fahrenheit = float(text)

# 3. compute
celsius = (fahrenheit -32) * (5 / 9) 

# 4. output
print(f"{fahrenheit}°F is {celsius:.1f}°C")
