print ("Abdul Moiz")
print ("18b-011-CS")
print ("problem#3.1")
print ('\n\na)Program for pension concerns: ')
age= int(input("Your age here:  "))
if age > 62:
    print("Yes you can avail pension benefits")
    
print ('\n\nb) A program for checking name in the list : ')
lst= ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']
name = str(input("Enter a name to be checked: "))
name = name.title()
if name in lst:
    print('One of the top 5 baseball players, ever!')

print ('\n\nc) Program to check hits and shield')
hits = int(input('enter number of hits : '))
shield = int(input('enter number of shields : '))
if hits > 10 and shield ==0:
    print('YOU ARE DEAD BRO!')

print ('\n\nd) Program to check safety')
North=True
South=False
East=False
West = True
if (North , South , East , West == 'True'):
    print('I can escape')


   
