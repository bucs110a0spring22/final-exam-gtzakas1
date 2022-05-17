from Trivia import Trivia 
from Dog import Dog

def main():
  Triv = Trivia()
  triv_question= Triv.get_question()
  print('Here Is Your Question:')
  print(triv_question['question'])
  
  if triv_question['difficulty'] == 'hard':
    print('This question is too hard, here is a dog fact!')
    dg= Dog()
    getDog= dg.get_dog()
    print(getDog['facts'][0])

  else:
    print('This is too easy, No dog fact for you.')


main()