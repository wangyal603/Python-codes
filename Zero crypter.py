#Python-codes
#Coded By Wangyal
#Convert Your Secret Messages Into Numbers
#importing Modules
import time
#Introduction
print("Welcome To Zero_Crypter\n")
time.sleep(1)
print("This Program Is Created By Programmer_wtb\n")
time.sleep(1)
print("Convert Your Secret Messages Into Numbers\n")
time.sleep(1)
print("Program Starting...\n")
time.sleep(1)
print("Select Options From The Following :\n")
time.sleep(1)
print("1.Encrypt Messages\n")
time.sleep(1)
print("2.Decrypt Messages\n")
time.sleep(1)
Choice = input("Enter 1/2 : ")
if Choice=='1':
   enc= input("Enter The Message To Encrypt : ")
   time.sleep(1)
   print("\nYour Encrypted Sring Is1
     1")
   for item in enc:
     print(ord(item),end = " ")
   print("\n\nThanks For Using My Program, Please Comment\nAnd Give A Star")
elif Choice=='2':
  message = input("Enter The Codes To Decode : ")
  decodedMessage = ""
  for item in message.split():
    decodedMessage += chr(int(item))
  print("The Decoded message Is:", decodedMessage)
  print("Thanks For Using My Program\nPlease Leave A Star")
else:
  print("Wrong Input")
