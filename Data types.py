#ctreation of arrays
array1= [1,2,3,'thimphu',2.5]

print(array1)
#retrieving
element1= array1[0]
element2= array1[4]
print(element2)
print(array1)
lastelement=array1[-1]
print(lastelement)
#modifying
array1[0] = 10
print(array1)

#getting number of elements in an array
no_of_elements = len(array1)
print(no_of_elements)
#counts starting from 1 when it comes to length

#slicing
elements = array1[0:2]
print(elements)
#0 till 2 but not 2
#inclusive of 0 but exclusive of 2 in this case

#concatenate lists
arr1=[1,10]
arr2= ['thimphu','wangdue']
arr3 = arr1 + arr2
print(arr3)

#checking index
number_to_check= 1
result = number_to_check in arr1
print(result)
#'1' is not same as 1

#listing method
#append
arrVariable = [1,2,3]
arrVariable.append(4)
print(arrVariable)

#insert at a specific index
arrVariable.insert(1,10)
#1=index
#10=value
print(arrVariable)

#sorting
arrVariable.sort()
print(arrVariable)

#stack
#adding to stack

stackVAR= []
stackVAR.append(4)
stackVAR.append(2)
stackVAR.append(9)
stackVAR.append(1)

print(stackVAR)
print('after appendin',stackVAR)

#popping
element = stackVAR.pop() #stores the removed index in elements variable
print('after popping',stackVAR)
print('storing in elements',element)