raw = input ('Enter a Number: ')

try:
    ival = int(raw)
except:
    ival = -1

if ival > 0 :
    print('Great job.')
else:
    print('Nope. Not a number.')