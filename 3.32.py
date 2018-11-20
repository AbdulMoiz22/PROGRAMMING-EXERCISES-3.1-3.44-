print('Abdul Moiz')
print('18b-011-CS-A')
print('Program # 3.32')
user_num = int(input("Please enter a 4-digit number only:"))
answer = []
for x in range(4):
    y = int(user_num%10)
    answer.insert(0,y)
    user_num = user_num/10
    
for x in range(4):
    print(answer[x])
