# The square and cube of numbers project
# پروژه مربع و مکعب اعداد

print("Display square and cube numbers")

# Receive the number as a float and store it in the "x" variable.
# "x" دریافت عدد و به صورت فلوت و ذخیره آن در متغیر 
x = float(input("Please enter the desired number:"))

# Store the square of the number in the "square" variable.
# "square" ذخیره مربع عدد در متغیر 
square = x ** 2

# Store the cube of the number in the "cube" variable.
# ذخیره مکعب عدد در متغیر "cube"
cube = x ** 3

# Print variables
# چاپ متغیر ها
print("square:")
print(square)
print("cube:")
print(cube)
