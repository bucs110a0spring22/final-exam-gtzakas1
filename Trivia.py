import requests


class Trivia:
  def __init__(self):
    self.trivia= "https://opentdb.com/api.php?amount=10"



  def get_question(self):
    r = requests.get(self.trivia)
    trivia = r.json()
    question = trivia["results"][0]
    return question


  def __str__(self):
    print(self.trivia)