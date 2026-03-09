import math

file = open("./results/CF_freq.csv", "w")
file.write("Generation\tFreq_c\tFreq_CC\tFreq_Cc\tFreq_cc\n")

q = 0.02
p = 1 - q

# דור ראשון
CC = p**2
Cc = 2 * p * q
cc = q**2

generations = int(input("how many generation? "))

for generation in range(generations):
    CC = p**2
    Cc = 2 * p * q
    cc = q**2
    
    #  כתיבה לקובץ 
    file.write(f"{generation }\t{q:.6f}\t{CC:.6f}\t{Cc:.6f}\t{cc:.6f}\n")
    
    
    q = q / (1 + q) 
    p = 1 - q
    
file.close()