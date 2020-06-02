#***CODE BY LOONY****#
#NOCOPYRIGHT
#LEARNING_AND_WRITING


import random
import time
pass_generator = 'abcdefghijklmnopqrstuvwxyz12345678910*)$($+$838282(2+$;$!$))'

number = input("Number Password: ")
number = int(number)

lenght = input("Password Length ")
lenght = int(lenght)

for x in range(number):
  password= ''
  for g in range(lenght):
     password += random.choice(pass_generator)
     
print("Generating Password,Please Wait...")
time.sleep(2)
print("")
time.sleep(1)
print"30%"
print("")
time.sleep(1.5)
print"70%"
print("")
time.sleep(2)
print"""100%"""
time.sleep(1.3)
print("This your Password", password )
