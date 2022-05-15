#!/bin/python3
 
import math
import os
import random
import re
import sys
 
 
#
# Complete the 'fibCypher' function below.
## The function is expected to return a STRING.
# The function accepts following parameters:
#  1. CHARACTER option
#  2. INTEGER num1
#  3. INTEGER num2
#  4. CHARACTER key
#  5. STRING msg
def forLoop(lanif, laniffinal):
   for x in lanif:
     laniffinal += chr(x)
   return laniffinal
def fibCypher(option, num1, num2, key, msg):
   # Write your code here
   alphabet = [chr(i) for i in range(97, 123)]
   lanif, numlist, letterslist, okay, laniffinal, num3, alphint  = [], [], [], [], "", 0, 0
   if option == "E":
       for x in range(0,len(msg)):
           if x%2 == 0:
               alphint = (alphabet.index(key) + num1)%26;letterslist.append(alphabet[alphint])
           if x%2 == 1:
               alphint = (alphabet.index(key) - num1)%26;letterslist.append(alphabet[alphint])
           num3 = num2 + num1; num1 = num2; num2 = num3
       for a in range(len(letterslist)):
           lanif.append(ord(letterslist[a])*3+int(ord(msg[a])));laniffinal = laniffinal+str(lanif[a]) + " "
       return(laniffinal.strip())
   if option == "D":
       okay = msg.split()
       for x in range(len(msg)):
           if x%2 == 0:
               alphint = (alphabet.index(key) + num1)%26;letterslist.append(alphabet[alphint])
           if x%2 == 1:
               alphint = (alphabet.index(key) - num1)%26;letterslist.append(alphabet[alphint])
           num3 = num2 + num1; num1 = num2; num2 = num3
       [lanif.append(int(okay[x])-3*ord(letterslist[x])) for x in range(len(okay))]
       return(forLoop(lanif, laniffinal))
if __name__ == '__main__':
   fptr = open(os.environ['OUTPUT_PATH'], 'w')
 
   option = input()[0]
 
   num1 = int(input().strip())
 
   num2 = int(input().strip())
 
   key = input()[0]
 
   msg = input()
 
   result = fibCypher(option, num1, num2, key, msg)
 
   fptr.write(result + '\n')
 
   fptr.close()
 
 


