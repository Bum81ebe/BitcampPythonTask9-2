# ask
text = input("What to calculate: ")

# splitting
x, y, z = text.split(" ")

# Convert x and z to floats
x = float(x)
z = float(z)

# Calculate 
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

# Print
print("{:.1f}".format(result))