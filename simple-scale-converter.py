# Scale calculator/converter (1:48)
# Scale = real number / scale (48)
real = input('What is the actual length (in.)? ')
ans = int(real)
scale = float(ans / 48)
# To change scale: change 48 to scale value (12, 24, etc.)
# Add the option of cm as well as inches
cent = scale * 2.54
print(scale), print('Inches')
print(cent), print('Centimeters')
# Output in both inches and centimeters @ 1:48 scale of input (inches)
