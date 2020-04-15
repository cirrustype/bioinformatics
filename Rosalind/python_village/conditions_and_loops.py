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

#trying a more simple step:
#this one works 
def all(a, b):
  sum = 0
  for num in range(a, b+1, 1):
    sum = sum+num
  print(sum)

#trying dataset
all(100,200) #15,150 does not match originial

# this function is wrong because the range only goes to b and not b+1
def odds(a, b):
  a = int(a)
  b = int(b)
  sum = 0

  if a % 2 == 1:
    for num in range(a, b, 2):
      sum = sum+num
    print(sum)
  else:
    for num in range(a+1, b, 2):
      sum = sum+num
    print(sum)


#trying a differnt method
#this loop works but it has to check every number in the range. 
def odds2(a,b):
  sum = 0
  for num in range(a, b+1):
    if num % 2 ==1:
      sum = sum+num
  print(sum)


######solution######

#this wone matches odds2 and works but it only has to check the first number
#and then every other number after. 
def oddsplus(a, b):
  a = int(a)
  b = int(b)
  sum = 0

  if a % 2 == 1:
    for num in range(a, b+1, 2):
      sum = sum+num
    print(sum)
  else:
    for num in range(a+1, b+1, 2):
      sum = sum+num
    print(sum)

odds(100, 200) #7500, this is correct! 
oddsplus(4809, 9479)
odds2(4809, 9479)#correct! 









  










