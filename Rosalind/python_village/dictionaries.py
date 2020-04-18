#Rosalind: python village ini6 (Dictionaries)

#Austin Schenk, 4/17/2020

###### Notes ######

###### Problem ######
#Given: A string s of length at most 10000 letters.

#Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.


###### Testing ######
d = open('ini6example.txt', 'r')
s = d.read()
w = s.split(' ')
print(s)
print(w)

dict = {}
for i in w:
  if i in dict:
    dict[i] = dict[i] + 1
  else:
    dict[i] = 1
print(dict)
#works on first try, awesome. 

###### Solution ######
def ini6(a, m, b):
  inPut = open(a, m)
  out = open(b, 'w')
  read = inPut.read()
  words = read.split(' ')
  print(read)
  print(words)
  dictionary = {}
  for i in words:
    if i in dictionary:
      dictionary[i] = dictionary[i] + 1 
    else:
      dictionary[i] = 1
  print(dictionary)
  out.write(str(dictionary))
  
  #TODO: I need to rework the dictionary so that the output is separated by lines and does not have the quotes and colons. Maybe a function in place of str(dictionary) that writes out a new string?

ini6('ini6.txt', 'r', 'ini6out.txt') #need to use a .strip() somewhere