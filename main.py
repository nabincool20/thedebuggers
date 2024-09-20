import requests
import json
import html
import threading
import time


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.score = 0

    def update_score(self, points):
        self.score += points

    def __str__(self):
        return f"User: {self.name}, Age: {self.age}, Score: {self.score}"

class Question:
    def __init__(self, question, correct_answer, incorrect_answers):
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
        self.all_answers = incorrect_answers + [correct_answer]
        
    def get_shuffled_answers(self):
        from random import shuffle
        shuffle(self.all_answers)
        return self.all_answers

class Quiz:
    def __init__(self, user):
        self.user = user
        self.questions = []

    def fetch_questions(self):
        response = requests.get("https://opentdb.com/api.php?amount=10")
        if response.status_code == 200:
            data = response.json()
            for item in data['results']:
                question = Question(html.unescape(item['question']), item['correct_answer'], item['incorrect_answers'])
                self.questions.append(question)

    def timer(self, timeout):
        time.sleep(timeout)
        print("\n Time's UP !")

    def play(self):
        self.fetch_questions()
        for question in self.questions:
            print(question.question)
            answers = question.get_shuffled_answers()
            for idx, answer in enumerate(answers, 1):
                print(f"{idx}. {answer}")

            timer_thread = threading.Thread(target=self.timer, args=(30,))
            timer_thread.start()
            
            user_answer = int(input("Your answer (number): ")) - 1
            if answers[user_answer] == question.correct_answer:
                print("Correct!")
                self.user.update_score(1)
            else:
                print(f"Wrong! The correct answer was: {question.correct_answer}")

        print(f"Your final score is: {self.user.score}")

if __name__ == "__main__":
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    user = User(name, age)

    quiz = Quiz(user)
    quiz.play()
