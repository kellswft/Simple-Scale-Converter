# Scale calculator/converter (1:48)

real = input('What is the actual length (in.)? ')
ans = int(real)
scale = float(ans / 48)
cent = scale * 2.54
print(scale), print('Inches')
print(cent), print('Centimetres')

# Output in both inches and centimeters @ 1:48 scale of input (inches)
