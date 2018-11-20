print ("Abdul Moiz")
print ("18b-011-CS")
print ("problem#3.5")
print('\n Program for checking four lettered words in a list')
lst=[]
word = input("Your word here: ")
lst.append(word)
word = input("Your word here: ")
lst.append(word)
word = input("Your word here: ")
lst.append(word)
word = input("Your word here: ")
lst.append(word)

print('\n\t\t FOUR LETTERED WORDS')

for x in lst:
    if len(x)==4:
        print(x)


