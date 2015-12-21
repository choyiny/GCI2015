# My first python program for GCI 2015
# choy.in

print("Are you old enough to drink?")

age = int(input("Please enter your age: "))

drinkingage = int(18)
whencanidrink = drinkingage - age


if age >= drinkingage:
  print("You can drink, congratulations!")

elif 1 < age < drinkingage:
  print("You cannot drink, but you can in " + str(whencanidrink) + " years!")

else:
  print("Your age is not recognizable by us!!")