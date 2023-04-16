"""
- one function one thing Single-responsibility principle SRP
- names for functions and variabels 
- K.I.S.S keep it simple 
"""

import time


grinding_time_S = 2
boiling_time_S = 3
pour_time_S = 2 
add_milk_S = 1

price = 100

def grind():
  beans = input("Do you wanna decaf £2 or normal £3?: ")
  beans = beans.lower()
  if beans == "decaf":
    global price
    price += 100 #
    print("Grinding decaf beans...")
    time.sleep(grinding_time_S) 
  elif beans == "normal":
    price += 200 #
    print("Grinding normal beans...")
    time.sleep(grinding_time_S) 
  else:
    print("Add some beans!")

def boildWater():
  water = input("Is it cattle ready on the stove full of water? Y/N: ")
  water = water.lower()
  while water != "y": #
    print("Add water!") 
    water = input("How about now? Y/N: ")
    water = water.lower()
  else:
    print("Boiling water...")
    time.sleep(boiling_time_S)

def addMilk():
  milk = input("Do you want to add some milk? it is only 20p!: ")
  milk = milk.lower()
  while milk != "y": #
    print("OK no milk")
    break
  else:
    print("Adding milk...")
    global price
    price += 20 #
    time.sleep(add_milk_S)

def pourWaterOverGrounds():
  print("Adding water...")
  time.sleep(pour_time_S) 
  
def coffee_machine():
  grind()
  boildWater()
  pourWaterOverGrounds()
  addMilk()
  coffee = print("Coffee is ready!",  "£",price/100)
  return coffee

def tea_machine():
  boildWater()
  pourWaterOverGrounds()
  addMilk()
  final_price = price/100
  print("Your tea is ready!", "£"+ str(final_price))



while True:
  machine_with = {"2":coffee_machine, "1":tea_machine}

  tea_coffe = input("Press 1 for tea(£1) or 2 for coffe(£2): ")

  machine_with[tea_coffe]()


##
## delete hardcoded code
## private _let
## add class
## write tp file
