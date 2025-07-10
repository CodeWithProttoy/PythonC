#list,array,collection is same
#index=     0  1  2  3  4  5  6  7  8   
numbers = [45,50,90 ,67,87,89,59,56,92]
#index=    -9 -8 -7 -6 -5 -4 -3 -2 -1  

print(numbers[3],numbers[-3])


#list(start : end)   #start from the start index stop before the end index
print(numbers [2:6])
print(numbers[1:7])


#list(start : end : step)

print(numbers[1:7:1])
print(numbers[1:7:2])
print(numbers[2:7:-1])

print(numbers[7:2:-1])
print(numbers[7:2:-2])
print(numbers[4:])
print(numbers[:5])
print(numbers[:])
print(numbers[::-1])
