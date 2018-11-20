print('Abdul Moiz')
print('18b-011-CS-A')
print('Program # 3.25')
user_lst = []
for x in range(3):
    a = input(" student name "+str(x+1)+":")
    user_lst.append(a)

for x in range(3):
    if user_lst[x][:1] in ('A','a','B','b','c','C','c','D','d','e','E','f','F','G','g','h','H','i','I','J','j','K','k','l','L','m','M'):
        print(user_lst[x])

