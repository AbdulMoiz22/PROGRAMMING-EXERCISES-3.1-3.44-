print('Abdul Moiz')
print('18b-011-CS-A')
print('Program # 3.24')
user_lst = []
for x in range(4):
    a = input(" word "+str(x+1)+":")
    user_lst.append(a)

for x in range(4):
    if user_lst[x]!='secret':
        print(user_lst[x])

