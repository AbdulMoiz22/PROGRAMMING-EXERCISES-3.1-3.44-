print ("Abdul Moiz")
print ("18b-011-CS")
print ("problem#3.3")
print('\n\na) Program for checking possibility of leap year')
year = int(input('Enter Year in numbers: '))
if year % 4 == 0:
    print('Could be a leap Year')
else:
    print('Definitely not a leap year')
print ('\n\nb) Program To Check two lists ' )

lst_ticket = []
ticket = int(input("Please enter the first number in ticket :"))
lst_ticket.append(ticket)
ticket = int(input("Please enter the second number in ticket:"))
lst_ticket.append(ticket)
ticket = int(input("Please enter the third number in ticket :"))
lst_ticket.append(ticket)
ticket = int(input("Please enter the fourth number in ticket:"))
lst_ticket.append(ticket)

lst_lottery = [6,4,3,2]
print("Ticket's Numbers :", lst_ticket)
print("Lottery's Numbers :",lst_lottery)
if lst_ticket == lst_lottery:
    print("\n\t\tYOU WON!")
else:
    print("\n\t\tBetter luck next time!")
