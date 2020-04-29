#Austin Schenk, 4/24/2020
#Rosalind, Bioinformatics Stronghold 
#Problem 2

###### Transcribing DNA into RNA ######

###### Info ######

# The Second Nucleic Acid (http://rosalind.info/problems/rna/)
#In “Counting DNA Nucleotides”, we described the primary structure of a nucleic acid as a polymer of nucleotide units, and we mentioned that the omnipresent nucleic acid DNA is composed of a varied sequence of four bases.

#Yet a second nucleic acid exists alongside DNA in the chromatin; this molecule, which possesses a different sugar called ribose, came to be known as ribose nucleic acid, or RNA. RNA differs further from DNA in that it contains a base called uracil in place of thymine; structural differences between DNA and RNA are shown in Figure 1. Biologists initially believed that RNA was only contained in plant cells, whereas DNA was restricted to animal cells. However, this hypothesis dissipated as improved chemical methods discovered both nucleic acids in the cells of all life forms on Earth.

#The primary structure of DNA and RNA is so similar because the former serves as a blueprint for the creation of a special kind of RNA molecule called messenger RNA, or mRNA. mRNA is created during RNA transcription, during which a strand of DNA is used as a template for constructing a strand of RNA by copying nucleotides one at a time, where uracil is used in place of thymine.

#In eukaryotes, DNA remains in the nucleus, while RNA can enter the far reaches of the cell to carry out DNA's instructions. In future problems, we will examine the process and ramifications of RNA transcription in more detail

###### scratchwork ######
sDNA = 'GATGGAACTTGACTACGTAAATT'

liDNA = list(sDNA)

#print(liDNA[1])

sRNA = {'A':'A', 'C':'C', 'G':'G', 'T':'U'}
#print(sRNA)

codex = list()
for i in range(len(liDNA)):
  codex.append(sRNA[liDNA[i]])

print(codex)# works 

#coverting back to a string
RNA = ''.join(str(n) for n in codex) #learn more about .join method!

#print(RNA)


###### Function ######

def dna2rna(a):
  transcription = {'A':'A', 'C':'C', 'G':'G', 'T':'U'}
  dna = list(a)
  ribose = []
  for i in range(len(dna)):
    ribose.append(transcription[dna[i]])
  rna = ''.join(str(n) for n in ribose)
  print(rna)

#dna2rna('GATGGAACTTGACTACGTAAATT') #correct 

###### Solution ######

dna2rna("""CATCACTGTAAATGTTAACGAATTGACGTGCCTCGAGCATCGCTCCCCTGGTAGGTGAGGGGGTCAACATGCGCGCAACCTACCACACCCTCTGTCACATTCCTTGTAGGGTAAAAGTAGTTTTATGGCACACAGACGATCCACTCGGGATTAGAGCCTATCTGCATGAGACGCTGGCGAGGGCGTGAGTCGACCAGCAGGCTGGGACAACATCGGGGGCCGTAGGCGACATTCTTCGTCGTTGGACTGTTACATTTGTGCCATCCTGTCTTGTTAGCTTGTTTTGACGAATGCCGACAATTAAATGCTTGCGAACTGTCGAGAAATAGTTAAGACGATTTGCAGAGTTTCCGCGGACACGCGGTCACCGGATGCCTCCGTTGCCTCATAGTGCATCGTTCACAACCCCCCCGGTTACTACTACCTTAATTATCCCTAGTTGCCTCACAGAGGGAGATTGCTACGACTACTTCTTAGGAAACCACTATGTCACGTAAGGATGCTGGGGTAAAGATGCGGCTATCGGTAGGCCGGATCATCCTGACCGCATCCTTTAGGCTTCTGGGCGGCTCACGGCAACAAAAATAGTCGAAGGTAGCCCCACCGTAGGCGCTATCCAACGCCGCCCGCGGTGGGCGCGCTAGTAGACGGCAGACAGGATATCCAAAATTTCGGGCACAGCCGCTCATCAGTTTATGAAGATCTGCATCTCTTTAGGCGTCATTATCATGGTATTGGTCCTCGCATACACTAGCACACACGACCGTATACAGACTTTTATAAACCGCATTCGACGTCCGATGCTCACTGAACACCGCGATACCGAGGCTGAAACGTGCCACGACCGGGTGTAGAGACTCTTCATTACTGAGGACCAGACGTCTCGTGGTTGTTTTCAGCGTCGTTTGGTCCAGGTATATGTTCTAGATGTATCACCGGTTAGTTGTATAGACAGCCGTGGCGCCGCGTAAAGTATACTTTCCTTC""")

#need to use """ for long ass strings 
#correct 

###### Other solutions ######
#from imslavko

s = input("""CAUCACUGUAAAUGUUAACGAAUUGACGUGCCUCGAGCAUCGCUCCCCUGGUAGGUGAGGGGGUCAACAUGCGCGCAACCUACCACACCCUCUGUCACAUUCCUUGUAGGGUAAAAGUAGUUUUAUGGCACACAGACGAUCCACUCGGGAUUAGAGCCUAUCUGCAUGAGACGCUGGCGAGGGCGUGAGUCGACCAGCAGGCUGGGACAACAUCGGGGGCCGUAGGCGACAUUCUUCGUCGUUGGACUGUUACAUUUGUGCCAUCCUGUCUUGUUAGCUUGUUUUGACGAAUGCCGACAAUUAAAUGCUUGCGAACUGUCGAGAAAUAGUUAAGACGAUUUGCAGAGUUUCCGCGGACACGCGGUCACCGGAUGCCUCCGUUGCCUCAUAGUGCAUCGUUCACAACCCCCCCGGUUACUACUACCUUAAUUAUCCCUAGUUGCCUCACAGAGGGAGAUUGCUACGACUACUUCUUAGGAAACCACUAUGUCACGUAAGGAUGCUGGGGUAAAGAUGCGGCUAUCGGUAGGCCGGAUCAUCCUGACCGCAUCCUUUAGGCUUCUGGGCGGCUCACGGCAACAAAAAUAGUCGAAGGUAGCCCCACCGUAGGCGCUAUCCAACGCCGCCCGCGGUGGGCGCGCUAGUAGACGGCAGACAGGAUAUCCAAAAUUUCGGGCACAGCCGCUCAUCAGUUUAUGAAGAUCUGCAUCUCUUUAGGCGUCAUUAUCAUGGUAUUGGUCCUCGCAUACACUAGCACACACGACCGUAUACAGACUUUUAUAAACCGCAUUCGACGUCCGAUGCUCACUGAACACCGCGAUACCGAGGCUGAAACGUGCCACGACCGGGUGUAGAGACUCUUCAUUACUGAGGACCAGACGUCUCGUGGUUGUUUUCAGCGUCGUUUGGUCCAGGUAUAUGUUCUAGAUGUAUCACCGGUUAGUUGUAUAGACAGCCGUGGCGCCGCGUAAAGUAUACUUUCCUUC""")
print(s.replace("T", "U")) #


#from prograde (in BASH):
#cat rosalind_rna.txt | tr T U

#from Johnny673
with open('rosalind_rna.txt') as file:
  print "U".join(file.read().split("T")) #I like this one!



#for i in liDNA:
  #if liDNA[i] = "T":
    #sRNA[i] = 'U'
  #else:
    #sRNA[i] = sDNA[i]
#print(sRNA)
  
#TODO make a dictionary for the DNA to RNA bases
#TODO remake everything because this was somehow not saved! 
###### Function ######


###### Solution ######


###### Other solutions ######