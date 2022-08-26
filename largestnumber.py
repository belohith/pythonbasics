largest_now = -1
print ('Before', largest_now)
for the_num in [44, 96, 35, 8, 12, 89, 99, 7]:
    if the_num > largest_now :
        largest_now = the_num
    print (largest_now, the_num)
print('After', largest_now)