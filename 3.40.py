print('Abdul Moiz')
print('18b-011-CS-A')
print('Program # 3.40')
user_lst = []
for x in range(5):
    a = input("Please enter Soccer Player "+str(x+1)+" Name:")
    user_lst.append(a)

for x in range(5):
    if user_lst[x][:1] in ('a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','I','i','j','J','k','K','l','L','m','M'):
        print(user_lst[x])
