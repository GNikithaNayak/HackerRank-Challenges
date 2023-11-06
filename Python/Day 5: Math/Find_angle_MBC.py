# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

ab = int(input()) 
bc = int(input()) 
ac = math.sqrt(ab**2+bc**2) 
value =int(round(math.degrees(math.atan2(ab, bc)), 0)) 
print(str(value)+u"\N{DEGREE SIGN}")
