#Austin Schenk, 5/1/2019
#Rosalind, Bioinformatics Stronghold
# Rabbits and Recurrence Relations 


###### Notes ######

#Wascally Wabbits (http://rosalind.info/problems/fib/)

#In 1202, Leonardo of Pisa (commonly known as Fibonacci) considered a mathematical exercise regarding the reproduction of a population of rabbits. He made the following simplifying assumptions about the population:

    # 1. The population begins in the first month with a pair of newborn rabbits.
    # 2. Rabbits reach reproductive age after one month.
    # 3. In any given month, every rabbit of reproductive age mates with another    #####rabbit of reproductive age.
    # 4. Exactly one month after two rabbits mate, they produce one male and one #####female rabbit.
    # 5. Rabbits never die or stop reproducing.

#Fibonacci's exercise was to calculate how many pairs of rabbits would remain in one year. We can see that in the second month, the first pair of rabbits reach reproductive age and mate. In the third month, another pair of rabbits is born, and we have two rabbit pairs; our first pair of rabbits mates again. In the fourth month, another pair of rabbits is born to the original pair, while the second pair reach maturity and mate (with three total pairs). The dynamics of the rabbit population are illustrated in Figure 1. After a year, the rabbit population boasts 144 pairs.

#Although Fibonacci's assumption of the rabbits' immortality may seem a bit farfetched, his model was not unrealistic for reproduction in a predator-free environment: European rabbits were introduced to Australia in the mid 19th Century, a place with no real indigenous predators for them. Within 50 years, the rabbits had already eradicated many plant species across the continent, leading to irreversible changes in the Australian ecosystem and turning much of its grasslands into eroded, practically uninhabitable parts of the modern Outback (see Figure 2). In this problem, we will use the simple idea of counting rabbits to introduce a new computational topic, which involves building up large solutions from smaller ones.


###### Scratchwork ######
# n = number of months 
n = 5

# k = reproductive capacity of each pair of rabbits. number of rabbit pairs produced for each living pair. 
k = 3

F1 = 1
F2 = 1

#(f = [] for i in range(3, len(n)): 
# f(1) = 1
# f(2) = 2 
# f(i) = f(i-1) + k*f(i-2)
# f.append(f(i)))

#print(list(range(n+1)))
#n=5
#k=3
#for number in list(range(n+1)):
  #f = 1
  #f = f + k*number
  #print(f)

pairs = [1,1]
#print(pairs[2-1])
n=5 #number of cycles
k=3 #pairs per cycle per existing pair 
for i in range(3, n+1): #new pairs born on the thrid week, n+1 because list starts at 0 in python; 'range(3,5)'
  f = pairs[i-2] + k*pairs[i-3] #[i-2]=[1] and [i=3]=[0] on the first step just to adjust fopr the index starting at 0
  pairs.append(f) # adds the value for the pairs of rabits at step n to the pairs vector. 
print(pairs[n-1]) #pairs[n] would be out of bounds because the index goes from 0-4 not 1-5


###### FUnction ######
def FIB(n, k):
  pairs = [1,1]
  for i in range(3, n+1):
    f = pairs[i-2] + k*pairs[i-3]
    pairs.append(f)
  print(pairs[n-1])

FIB(5,3) #correct 

###### Solution ######

FIB(31,2) #correct

###### Other solutions ######
# look at closed form solutions

#from toovst:
from math import sqrt

def fib_rabbits(n, k):
    d = (-1)**2 - 4 * 1 * (-k)
    f_n = (1/sqrt(d))*((1+sqrt(d))/2)**n - (1/sqrt(d))*((1-sqrt(d))/2)**n
    return int(f_n)

print(fib_rabbits(5, 3))

#by Kit Burschka:
def fib(n, k):
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, k*a + b
    return b









