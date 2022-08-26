c = 0
s = 0
print ('Before', c, s)
for v in [24,15,69,32,74,25]:
    c = c + 1
    s = s + v
    print (c, s, v)
print ('After', 'Count:', c, 'Sum:', s, 'Average:', s/c)