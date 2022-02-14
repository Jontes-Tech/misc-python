print("█▀▄▀█ █░█ █░░ ▀█▀ █ █▀█ █░░ █▄█") #Fancy text
print("█░▀░█ █▄█ █▄▄ ░█░ █ █▀▀ █▄▄ ░█░") #More Fancy Text
print("This software is used to multiply something by 2") #Well, duh.

timesToLoop = int(input("Please enter a number: "))

number = 1
print(number)

while timesToLoop > 0:
  number *= 2
  print(number)
  timesToLoop -= 1
  #time.sleep(0.1) Uncomment for readable speeds.
print("---")
print("The final number is...")
print("Drumroll please...") #Can be removed to debloat
print(number) #Printing the final number

print("Copyleft, GPL 3.0. This software is made by Jonte from Jontes.Page. Very few rights reserved.") #Boring licensing text
print("Source code by opening this file in a text editor.")