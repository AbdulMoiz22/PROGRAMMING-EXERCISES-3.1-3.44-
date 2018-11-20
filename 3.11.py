print ("Abdul Moiz")
print ("18b-011-CS")
print ("problem#3.11")
print('Practice Problem 3.11')

def Even(x):
    for a in x:
        if a%2!=0:
            print("False")
            break
    else:
        print("True")

user_lst=[]
for x in range(4):
    a=int(input("Pleasse enter number " + str(x+1) + ":"))
    user_lst.append(a)

Even(user_lst)

        
