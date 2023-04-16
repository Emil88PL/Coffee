class Base_coffee_price:
  def __init__(self,price):
    self.price = price

  def __str__(self):
    return self.price
  
base_price = Base_coffee_price(100)