class QuizBrain:
   def __init__(self, q_list):
      self.question_number = 0
      self.question_list = q_list
      self.score = 0
   
   def still_has_questions(self):
      return not(self.question_number > len(self.question_list)-1)

   def next_question(self):
      # for _ in self.question_list:
      current = self.question_list[self.question_number]
      correct_answer = current.answer
      self.question_number += 1
      user = input(f"Q.{self.question_number}: {current.text} (True/False)?: ")
      self.check_answer(user, correct_answer)


   def check_answer(self, user, correct_answer):
      if user.lower() == correct_answer.lower():
         self.score += 1
         print(f"You got it right!")
      else:
         print("That's wrong")
      print(f"The correct answer was {correct_answer}\nYour score is {self.score}/{self.question_number}\n")
   