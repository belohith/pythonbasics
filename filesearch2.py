fhand = open('hello.txt')
for line in fhand:
    lin = line.rstrip()
    if not 'perfect':
        continue
    print(line)