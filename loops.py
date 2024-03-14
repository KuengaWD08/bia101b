#loops over an array
fruits = ['a','b','c']
#loops through each elements
#at each stage, if the elements is 'a'
#print True
for e in fruits:
    if e == 'a':
        print('True')
    if e == 'b':
        print('True')

#iterate over a string
greetings = 'hello'
for char in greetings:
    print(char)

#Exercise : check if strings contains vowel
    
#iterate over a range
    for i in range(20):
        print(10)
#20 = no of iterations

for i in range(9):
    val = i + 5 # 5,6,7,8,9,10,11,12,13
    print(val)

for i in range(5,14):
    print(i)

for i in range(5,14,2):
    print(i)
#iterates by jumping 2 forward

#While loops
count = 0
#while loop functions untils its true
while count < 5:
    print(count)
    count = count + 1

#user input strings is unknown
#print every char of the strings
s = 'helloabc'
counter = 0
lenth_s = len(s)
print('coutner:', counter)
print('len s:', lenth_s)
# 0 , 1 , 2, 3, 
print('going in loop')
while counter < lenth_s:
    print('counter:', counter)
    char = s[counter]
    print(char)
    counter = counter + 1
    print('-----')

 
