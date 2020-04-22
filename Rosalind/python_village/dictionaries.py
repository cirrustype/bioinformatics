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
  s3 = d.split(',')
  listlen = len(s3) # needed to add range so that the index was an integer?
  for i in range(listlen):
    i1 = s3[i]
    i2 = str(i1)
    kill = "{}:',"
    for char in kill: 
      i2 = i2.replace(char, "")
    s3[i] = i2

  sol = "\n".join(s3) #this works
  
  print(sol)

  out.write(sol)


ini6('ini6.txt', 'r', 'ini6out.txt')

#TODO clean this up a lot. 

#look up python Counter do do this in only two lines



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































