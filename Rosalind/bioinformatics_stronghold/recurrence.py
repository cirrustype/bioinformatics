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


n=5
k=3
for number in list(range(n+1)):
  f = 1
  f = f + k*number
  print(f)




###### FUnction ######



###### Solution ######



###### Other solutions ######














