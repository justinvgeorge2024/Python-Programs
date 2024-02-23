# String slicing
String = 'ASTRING'
 
s1 = slice(3)
s2 = slice(1, 5, 2) #searches from index 1 to 5-1=4 with step 2 #prints index 1,3 only. not 5
s3 = slice(-1, -12, -2)
s4 = slice(1, -3,1)
s5 = slice(1,-3) #same as s4
s6 = slice(-2,2)
 
print('String slicing')
print(String[s1])
print(String[s2])
print(String[s3])
print(String[s4])
print(s4) # prints the statement: slice(1,-3,1)
print(String[s5])
print(String[slice(-2,1,2)]) #empty print - no value to slice with step as 2
print(String[slice(-2,1,-2)]) # prints NR

#######
print(String[:3])
print(String[1:5:2])#prints SR
print(String[-1:-12:-2])
print(String[::-1]) #for reverse printing #step -1
print(String[::3]) # forward with step 3


"""
arr[start:stop]         # items start through stop-1
arr[start:]             # items start through the rest of the array
arr[:stop]              # items from the beginning through stop-1
arr[:]                  # a copy of the whole array
arr[start:stop:step]    # start through not past stop, by step
"""
