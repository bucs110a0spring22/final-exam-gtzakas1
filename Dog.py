import requests 

class Dog:
  def __init__(self):
    self.dog= "http://dog-api.kinduff.com/api/facts"

  def __str__(self):
    print(self.dog)

  def get_dog(self):  
    r = requests.get(self.dog)
    dog = r.json()
    return dog
 
   
   