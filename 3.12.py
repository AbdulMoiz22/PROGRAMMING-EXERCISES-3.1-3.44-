print ("Abdul Moiz")
print ("18b-011-CS")
print ("problem#3.12")
def negatives(x):
    for a in x:
        if a<0 :
            print(a)
user_list= []
for x in range(4):
    number=int(input('Enter number' + str(x+1) + ' : '))
    user_list.append(number)
negatives(user_list)
