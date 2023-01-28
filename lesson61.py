print("Wellcome to my computer quiz !")

playing = input("Do you want to play!")

if playing . lower() != 'yes':
  quit()
  
print ('Lets play')
score = 0

answer = input('What does CPU stands for?')
if answer. lower()== "central processing unit":
  print("yes")
  score += 1
else:
  print("NOT")

answer = input("What does GPU stands for?")
if answer.lower( ) == "graphics processing unit":
  print("YES") 
  score += 1
else:
  print("YES")

answer = input("What does RAM stands for?")
if answer .lower() == "random acces memory":
  print("YES")
  score += 1
else:
 print("NOT")

 answer = input("What does PSU stands for?")
 if answer.lower () == "power supply":
   print("YES")
   score += 1
 else:
   print("NOT")

print("Youu got" + str(score) + "question correct!")
print("You got" + str(score / 4)+"%")