from cgitb import small


smallest = None
print ('Before')
for value in [44, 58, 63, 17, 5, 33]:
    if smallest is None:
        smallest = value
    elif value < smallest :
        smallest = value
    print (smallest, value)
print('After', smallest)