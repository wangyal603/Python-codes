#python 3.7.1
import math
import time
print ("Welcome")

print ("Your Name")
Name = (input ())
print ("Hi " + Name)
print ("Should We start Calulating Now")
ent = (input ())
if (ent == "n") or (ent =="N"): print ("Get Lost")
else :print ("Your first No.")
n1 = float(input ())
print("")
print("")
print ("Choose 1 for ADDITION") 
time.sleep(.2)
print ("Choose 2 for SUBSTRACTION")
time.sleep(.2)
print ("Choose 3 for MULTIPLICATION")
time.sleep(.2)
print ("Choose 4 for DIVISION")
time.sleep(.2)
print ("Choose 5 for SQUARE")
time.sleep(.2)
print ("Choose 6 for CUBE")
time.sleep(.2)
print ("Choose 7 for PRESENTAGE")

op = (input ())
print("")
print("")
if op=="5": print("Your Result is \n",n1 * n1)
if op=="6": print ("Your Result is \n",n1 * n1*n1)
 
if op=="6" or op=="5": print ("HAVE A GREAT DAY " +Name )
if op == "1" or op == "2" or op == "3" or op=="4" or op=="7":print ("Your Second No.") 
n2 = float(input ())
per = n1/n2
tage = per*100
if op == "1": print ("Your Result is \n" ,n1 + n2)
if op=="2": print ("Your Result is \n",n1 - n2)
if op=="3": print ("Your Result is \n",n1 * n2)
if op=="4": print ("Your Result is \n",n1 / n2)

if op=="7": print ("Your Result is \n",tage)
if op>"8":print (".......Is Alright.......\n")
print ("HAVE A GREAT DAY " +Name )
