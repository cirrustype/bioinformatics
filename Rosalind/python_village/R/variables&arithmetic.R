#Austin Schenk
#July 12th, 2020
#Bioinformatics, Rosalind, Python Village

#Variables and Some Arithmetic

######Problem######

#Given: Two positive integers aand b, each less than 1000.

#Return: The integer corresponding to the square of the 
#hypotenuse of the right triangle whose legs have lengths a
#and b.

"Notes:The dataset changes every time you click 
Download dataset. We check only your final answer 
to the downloaded dataset in the box below, not your 
code itself. If you would like to provide your code as 
well, you may use the upload tool. Please also note that 
the correct answer to this problem will not in 
general be 34; it is simply an example of what you 
should return in the specific case that the legs of the 
triangle have length 3 and 5."

a = 3
b = 5
c = a^2 + b^2
c

hyp <- function(a, b){
  c <- a^2 + b^2
  return(c)
}

hyp(3,5)


hyp(889,967)
