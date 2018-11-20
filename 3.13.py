print ("Abdul Moiz")
print ("18b-011-CS")
print ("problem#3.13")

'''gives the average of two numbers Ex#3.9'''

def average(x,y):
    average.py= (x+y)/2
    return average.py
num_1= int(input('Enter a number: '))
num_2= int(input('Enter a number: '))

print("The average of the two entered number is: ",average(num_1,num_2))

help(average)

'''Gives a list of negative numbers'''

def negatives(x):
    for a in x:
        if a<0 :
            print(a)
user_list= []
for x in range(4):
    number=int(input('Enter number' + str(x+1) + ' : '))
    user_list.append(number)
negatives(user_list)
help(negatives)



