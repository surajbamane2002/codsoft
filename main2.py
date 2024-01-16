import random


def load_quiz_questions():

  questions = [
      "What does RAM stands for?", "What does GPU stands for?",
      "Which is odd number?"
  ]
  choices = [[
      "A) random access memory", "B) random access manage",
      "C) real access memory"
  ],
             [
                 "A) graphics processing unit", "B) graphics pre unit",
                 "C) graphics project unit"
             ], ["A) 1", "B) 4", "C) 6"]]
  correct_answers = ["A", "A", "A"]
  return questions, choices, correct_answers


def present_quiz_question(question, choices):
  print(question)
  for choice in choices:
    print(choice)


def evaluate_user_answer(user_answer, correct_answer, score):
  if user_answer.upper() == correct_answer:
    print("Correct!")
    return score + 1
  else:
    print(f"Incorrect. The correct answer is {correct_answer}.")
    return score


def display_final_results(score, total_questions):
  percentage = (score / total_questions) * 100
  print(f"\nYour final score: {score}/{total_questions} ({percentage:.2f}%).")
  if percentage >= 70:
    print("Great job! You did well.")
  else:
    print("You can do better. Keep practicing!")


def play_quiz():
  questions, choices, correct_answers = load_quiz_questions()
  total_questions = len(questions)
  score = 0

  print("Welcome to the Quiz Game!")
  print("Here are the rules:")
  print("- You will be asked multiple-choice questions.")
  print("- Choose the correct answer and see how well you know the topic.\n")

  play_again = True
  while play_again:
    for i in range(total_questions):
      present_quiz_question(questions[i], choices[i])
      user_answer = input("Your answer (A, B, or C): ")
      score = evaluate_user_answer(user_answer, correct_answers[i], score)
      print("\n" + "=" * 30 + "\n")

    display_final_results(score, total_questions)
    play_again = input(
        "Do you want to play again? (yes/no): ").lower() == "yes"
    if play_again:
      score = 0

  print("Thanks for playing!")


if __name__ == "_main_":
  play_quiz()
