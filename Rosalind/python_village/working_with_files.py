
######Working with Files######

#Rosalind Python Village, INI5 (problem 4)
#Austin Schenk 4/15/2020


###### Notes ######

#Use something = open(file.txt, (r/w/a)) to open files. This opens the file and names it 'something.' The first parameter is the name of the file and the second is permission; read, write, and append. 

# the comand something.read(n) returns n bytes of information form the file 'something' as a string. if n is left blank the command will return the entire file as a string. 

#something.readline() takes a single line from the file. each line ends with \n for a new line ecept the last. You can remove the \n by using .strip(). 

#every time you use .readline() it takes the next line. You can take a specific line by indicating that line's number in the argument. The default numbering in python is 0-based!

#something.readlines() will return every line in the file. 

#You can also use a loop to get the lines of a file 
#for line in something:
  #print line

#### When data in not separated by \n ###

#You can use someline.split() to separate on white space and \n
#you can slipt on multiple types of delimiter using .split();
# .split(",") will split on commas

#.splitlines() will split up every line and list them. 

### writing to a file ###
#something.write('important stuff') will add 'important stuff' or what ever is in the argument to the file 'something.' This only works with strings. 
# To add something that is not a string you must convert it to a sting using str() command. 

#something.close() will colse the file to be tiddy

###### The Problem ######

#Given: A file containing at most 1000 lines.

#Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

###example data

e = open('ini5example.txt', 'r') # everything has to be in single quotes

#print(e.read())

def ini5(a, m, b, n):
  e = open(a, m)
  elines = e.readlines()
  elist = list(elines)
  out =open(b, n)
  for i in range(1, len(elist), 2):
    print(elist[i]) #finally 
    #lines = [elist[i]]
    #print(lines)
    out.write(elist[i])

ini5('ini5example.txt', 'r', 'inifoutputtest.txt', 'w') #this works

###### Solution ######

ini5('ini5.txt', 'r', 'ini5output.txt', 'w') #correct! 
