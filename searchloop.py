find = False
print('Before', find)
for value in [13, 24, 35, 46, 57]:
    if value == 35:
        find = True
    print(find, value)
print('After', find)