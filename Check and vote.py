# ! check if user can vote or not 
# get user age from inout
#convert userinout (str) to (int) to number
# if else statment
# if 18 above print 'you can vote
#if below 18, print "you cannot vote"


user = input("enter your age: ") 
userage = int(user)
if userage >= 18:
    print (' you can vote')
elif userage <= 18:
    print("you cannot vote")