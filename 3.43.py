print('Abdul Moiz')
print('18b-011-CS-A')
print('Program # 3.43')
def hit(x1,y1,r,x2,y2):
    import math
    dist = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    if dist<=r:
        print("Its a Hit :) !")
    else:
        print("Missed it :( !")

x1 = float(input(" x coordinates:"))
y1 = float(input(" y coordinates:"))
r = float(input("Radius:"))
x2 = float(input("x2   :"))
y2 = float(input("y2   :"))

hit(x1,y1,r,x2,y2)

