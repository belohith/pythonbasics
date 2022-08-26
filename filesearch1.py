fhand = open('hello.txt')
for line in fhand:
    lin = line.rstrip()
    if not line.startswith('Here'):
        continue
    print(line)