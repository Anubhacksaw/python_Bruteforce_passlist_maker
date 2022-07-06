from itertools import product
import string
import sys
from termcolor import colored, cprint
import os
cprint('Authore:-Anubhab Mukherjee\n', 'red', attrs=['reverse', 'blink'])
ch=int(input("\n1.Contains only Letters\n2.Contains only numbers\n3.Contains only letters and numbers\n4.Contains letter numbers and special charecters\n"))
i=int(input("Enter the min length of the password: \n"))
j=int(input("Enter the max length of the password: \n"))
if ch==1:
 	p=string.ascii_lowercase+string.ascii_uppercase
elif ch==2:
	p=string.digits
elif ch==3:
	p=string.ascii_lowercase+string.ascii_uppercase+string.digits
elif ch==4:
	p=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

name=input("Enter the name of the output password file(eg. name.txt): ")
file=open(name,'w')

for l in range (i,j+1):
	for c in product(p,repeat=l):
		   wrd="".join(c)
		   file.write(wrd)
		   file.write('\n')
size=os.path.getsize(name)
print("Passfile created succesfully!!!!\nSize of the passfile is",size,"bytes")
cprint('\n https://github.com/Anubhab-ai\n', 'yellow')

