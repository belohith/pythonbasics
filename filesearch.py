fhand = open('hello.txt')
for line in fhand:
    lin = line.rstrip()
    if line.startswith('Here'):
        print(line)