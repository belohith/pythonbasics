#opening a text file

xfile = open('hello.txt')
for cheese in xfile.readlines():
    print(cheese)