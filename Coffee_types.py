class Coffee_type:
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def __str__(self):
    return self.name  
  
decaf_coffee = Coffee_type("decaf", 100)
normal_cofee = Coffee_type("normal", 200)