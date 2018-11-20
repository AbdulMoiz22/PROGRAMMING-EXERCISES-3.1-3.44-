print ("Abdul Moiz")
print ("18b-011-CS")
print ("problem#3.4")
print('\n Program for executing loop (3 to 12)')
for x in range(3,13):
    print (x)
print('\n Program for executing loop (0 to 8)')

#but with a step of 2 instead of the default 1

for x in range (0,9):
    if x % 2 == 0:
        print(x)
print('\n Program for executing loop (0 to 24)')
#but not including 24 with a step of 3
for x in range (0,24):
    if x % 3 ==0:
        print(x)

print('\n Program for executing loop (3 to 12)')
for x in range(3,12,5):
    print(x)




