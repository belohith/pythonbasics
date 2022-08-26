data = 'Hello there! How are you?'
atpos = data.find('!')
print(atpos)

spos = data.find('y', atpos)
print(spos)

host = data[atpos + 1 : spos]
print(host)
