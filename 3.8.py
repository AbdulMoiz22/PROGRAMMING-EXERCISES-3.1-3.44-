print ("Abdul Moiz")
print ("18b-011-CS")
print ("problem#3.8")
print('\n Practice Problem #3.8')

def perimeter(r):
    import math
    perimeter= (2*math.pi*r)
    return perimeter

radius = int(input("Give the value of radius: "))
print("Calculated perimeter is :",perimeter(radius))
