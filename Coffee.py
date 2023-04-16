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

price = 100 ## shoudnt be global

class Coffee_type:
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def __str__(self):
    return self.name
  

decaf_coffe = Coffee_type("decaf", 100)
normal_cofee = Coffee_type("normal", 200)

decaf_coffee_name = decaf_coffe.name
normal_cofee_name = normal_cofee.name

price_decaff_coffee = decaf_coffe.price
price_normal_cofee = normal_cofee.price



def grind():
  beans = input("Do you wanna decaf £2 or normal £3?: ")
  beans = beans.lower() # making sure it is lower case not sure now

  base_coffee_price = 100
  
  if beans == decaf_coffee_name: ##
    base_coffee_price += price_decaff_coffee
    print("Grinding decaf beans...")
    time.sleep(grinding_time_S) 
  elif beans == normal_cofee_name:
    base_coffee_price += price_normal_cofee
    print("Grinding normal beans...")
    time.sleep(grinding_time_S) 
  else:
    print("Add some beans!")

def boildWater():
  water = input("Is it cattle ready on the stove and full of water? Y/N: ")
  water = water.lower()

  

  while water != "y": ##
    print("Add water!") 
    water = input("How about now? Y/N: ")
    water = water.lower()
  else:
    print("Boiling water...")
    time.sleep(boiling_time_S)

def addMilk():
  milk = input("Do you want to add some milk? it is only 20p!: ")
  milk = milk.lower()

  price_milk = 20 
  pozitive_answer = "y"

  while milk != pozitive_answer: 
    print("OK no milk")
    break
  else:
    print("Adding milk...")
    global price
    price += price_milk
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

#"""