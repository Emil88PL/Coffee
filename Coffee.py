"""
- one function one thing Single-responsibility principle SRP
- names for functions and variabels 
- K.I.S.S keep it simple 
"""

import time
from Coffee_types import decaf_coffee, normal_cofee 
#from Prices import base_price
from Time import time_S

class Base_price_coffee():
  def __init__(self,price):
    self.price = price

  def __str__(self):
    return self.price
  
base_price = Base_price_coffee(100)
final_price = 100

def grind():
  beans = input("Do you wanna decaf £2 or normal £3?: ")
  beans = beans.lower() 
  

  if beans == decaf_coffee.name: 
    global final_price
    
    #base_price.price += decaf_coffee.price
    final_price = base_price.price + decaf_coffee.price
    print("Grinding decaf beans...")
    time.sleep(time_S.grinding_time_S)
    print(final_price)
  
  elif beans == normal_cofee.name:
    
    final_price = base_price.price + normal_cofee.price
    print("Grinding normal beans...")
    time.sleep(time_S.grinding_time_S)
    print(final_price)
  
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
    time.sleep(time_S.boiling_time_S)


def addMilk():
  milk = input("Do you want to add some milk? it is only 20p!: ")
  milk = milk.lower()
  price_milk = (20) 
  pozitive_answer = "y"
  while milk != pozitive_answer: 
    print("OK no milk")
    global final_price
    
    break
  else:
    print("Adding milk...")
    print(final_price)
    time.sleep(time_S.add_milk_S)
    final_price += price_milk
    print(final_price)
   
    
    

  

def pourWaterOverGrounds():
  print("Adding water...")
  time.sleep(time_S.pour_time_S) 
  
def coffee_machine():
  grind()
  boildWater() 
  pourWaterOverGrounds()
  addMilk()  
  print("Your coffee is ready!", "£" + str(final_price/100))

def tea_machine():
  boildWater()
  pourWaterOverGrounds()
  addMilk()  
  print("Your Tea is ready!", "£", final_price)

while True:
  machine_with = {"2":coffee_machine, "1":tea_machine}
  tea_coffe = input("Press 1 for tea(£1) or 2 for coffe(£2): ")
  machine_with[tea_coffe]()

##
## delete hardcoded code
## private _let
## add class
## write tp file