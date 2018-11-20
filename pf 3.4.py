print ("Abdul Moiz")
print ("18b-011-CS")
print ("problem#3.4")
print('\n Program for checking you can login or not')

lst= ['joe','sue','hani','sophie']
login= str(input('Enter Your Login ID: '))
if login in lst:
    print('Your login is succeful,Enjoy')
    print('Done')
else:
    print('You entered an invalid id')
    print('Done')
