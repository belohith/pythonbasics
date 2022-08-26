fname = input('Enter the filename: ')
try:
    fhand = open(fname)
except:
    print('File not found: ', fname)
    quit()
count  = 0
for line in fhand:
    if line.startswith('Oceans'):
        count = count + 1
print('There are', count, 'ocean lines in', fname)