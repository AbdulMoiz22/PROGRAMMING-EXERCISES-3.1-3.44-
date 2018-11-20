print('Abdul Moiz')
print('18b-011-CS')
print('practice problem#3.10')
def noVowel(s):
    for x in s:
        if x in ("a","e","i","o","u","A","E","I","U"):
            print("False")
            break
            
    else:
        print("True")

user_string = input("\n\nPlease enter a word:")
noVowel(user_string)
    
    
