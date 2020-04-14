#Austin Schenk
#04/13/2020

#Rosalind Python village Problem 3


######Problem:######
#    Given: Two positive integers a and b (a < b < 10000)
#    Return: The sum of all odd integers from a through b, inclusively.


######Example:######
#    Dataset: 100 200
#    Output: 7500

#Hint: aa % 2 == 1 for odd, a mod two 

######Testing ######
a = 100
b = 200

if a % 2 ==1:
  print(a, ' is odd')
  sum = 0
  for i in range(a, b):
    sum = sum + i
    i = i + 2
  print(sum)
else:
  print(a, ' is even') 
  sum = 0
  for i in range(a+1, b):
    sum = sum + i
    i = i + 2
  print(sum) #14850, too high 

  










