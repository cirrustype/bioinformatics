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
#print(s)
#print(w)

dict = {}
for i in w:
  if i in dict:
    dict[i] = dict[i] + 1
  else:
    dict[i] = 1
#print(dict)
#works on first try, awesome. 

###### Solution ######
def ini6(a, m, b):
  inPut = open(a, m)
  out = open(b, 'w')
  read = inPut.read()
  r = read.strip('\n')
  words = r.split(' ')
  #print(read)
  #print(words)
  dictionary = {}
  for i in words:
    if i in dictionary:
      dictionary[i] = dictionary[i] + 1 
    else:
      dictionary[i] = 1
  #print(dictionary)
  d = str(dictionary)
  s3 = d.split(',') # d = s2
  for i in s3:
    i1 = s3[i]
    i2 = str(i1)
    kill = "{}:'"
    for char in kill: 
      i2 = i2.replace(char, "")
    s3[i] = i2
    #print(i2)
  print(s3)
  
  #TODO: I need to refactor the loops to get rid of the inner one so that the unwanted characters are removed all at once. Then split on the commas and write each entry in the list onto a new line of the output file. 

  out.write(d)
  # look up re library and re.sub???
  #https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python

  #### building blocks of the loop, left for reference ####
  #s1 = d.strip('{') #good
  #s2 = s1.strip('}')
  #i3 = i2.replace(":", "") #good
  #i4 = i3.replace("'", "")
  #i3 = i2.strip(':')
  #print(i4)
  #print(s3)





  

ini6('ini6.txt', 'r', 'ini6out.txt') #need to use a .strip() somewhere



