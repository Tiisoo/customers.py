
class Customer:  
  def __init__(self,name,location):
    self.name =name
    self.location =location
  def __str__(self):
    return f'name:{self.name}\nlocation:{self.location}'
class Product:
  def __init__(self,name,quantity):
    self.name =name
    self.quantity =quantity
  def __str__(self):
    return f'name:{self.name}\nquantity:{self.quantity}'
class Payment:
  total_amount =0
  def __init__(self,amount):
    self.amount = amount
  @classmethod
  def set_total_amount(cls,product1_fee,product2_fee,product3_fee):
    cls.total_amount = product1_fee + product2_fee + product3_fee
  @classmethod
  def get_total_amount(cls):
    return cls.total_amount
  def get_discount(self):
    #if customer1 buys daily:
      return 0.1*self.total_amount
  @classmethod
  def set_final_amount(cls,total_amount):
    cls.set_final_amount = total_amount-get_discount
  @classmethod
  def get_final_amount(cls):
    return cls.final_amount
customer1 =Customer('Shadiah','Kasana')
customer2 =Customer('Aishah','Kajjansi')
customer3 =Customer('Najib','Kampala')
product1 = Product('pens',10)
product2 = Product('books',8)
product3 = Product('juice',1)

print(f'customer1:\n{customer1}\n\ncustomer2:\n{customer2}\n\ncustomer3:\n{customer3}')
print(customer1.name)
print(f'product1:\n{product1}\n\nproduct2:\n{product2}\n\nproduct3:{product3}')
print(product1.name)

def __str__(self):
    return f'Amount paid is {self.amount}\nDiscount:{self.get_discount()}'


Payment.set_total_amount(5000,1600,100)
print(Payment.get_total_amount())

payment2 =Payment(5000)
print(payment2.get_discount())
