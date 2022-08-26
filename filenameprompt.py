fname = input('Enter the filename: ')
fhand = open(fname)
count  = 0
for line in fhand:
    if line.startswith('Oceans'):
        count = count + 1
print('There are', count, 'ocean lines in', fname)