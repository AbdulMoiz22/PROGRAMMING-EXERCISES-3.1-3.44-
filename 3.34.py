print('Abdul Moiz')
print('18b-011-CS-A')
print('Program # 3.34')
def pay(x,y):

    if  y>40:
        z=y-40
        s=x*40
        p=z*(x*1.5)
        print("Pay :",s+p)
    else: 
        print("Pay :",x*y)
wage = int(input("Please enter the hourly wage:"))
hour = int(input("Please enter the number of hours worked:"))

pay(wage,hour)        
    
