#objective:
#create a program that takes in user input 
#and determines the if the number is positive or negative 
#print "your number is positive or negative or zero"
##if else 
#print()
#input)
#1-3min


#Break down the problem
#1. Take in user input
    #Check the  type of the input
#2.Check if the number is positive or negative or xero
   # need to use if else statement
    # you will be comparing numbers and not string
#3. Print the result

#1 
userInput = input('Please type any number: ')
userInputType = type(userInput)
print('The type of user input is:', userInputType)

userInputNumber = float(userInput)
print('The type of userInputNumber is:', type(userInputNumber))

# 2,3 - if else statement and print
if userInputNumber > 0:
    print('The number is positive')

elif userInputNumber < 0:
    print('The number is negative')

elif userInputNumber == 0:
    print('The number is zero')

  


