import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 5

'''Create an Dictionary that stores question as key and
 list of options as value where the correct answer is in list[0]'''
QUESTIONS = {
    'What is the capital of France?': ['Paris', 'Berlin', 'London', 'Madrid'],
    'Which programming language is known for its readability and simplicity?': ['Python', 'Java', 'C++', 'JavaScript'],
    'What is the result of 2 + 3 * 4?': ['14', '20', '18', '10'],
    'In Python, how do you open a file for reading?': ['open("filename", "r")', 'file_open("filename", "r")', 'open_file("filename", "read")', 'read_file("filename")'],
    'What is the purpose of the "if __name__ == "__main__":" statement in a Python script?': ['It ensures that the script is not executed when imported as a module.', 'It is used to define a main function.', 'It is a syntax error in Python.', 'It is used to include external libraries.'],
    'What is the largest planet in our solar system?': ['Jupiter', 'Venus', 'Mars', 'Saturn'],
    'What is the main purpose of the "elif" keyword in Python?': ['To check an additional condition if the preceding "if" or "elif" condition is False.', 'To handle multiple exceptions in a try-except block.', 'To indicate the end of a conditional statement.', 'To define a block of code that will be executed if the condition before it is False.'],
    'Which data structure follows the Last In, First Out (LIFO) principle?': ['Stack', 'Queue', 'Linked List', 'Array'],
    'What does the acronym API stand for?': ['Application Programming Interface', 'Advanced Programming Interface', 'Application Protocol Interface', 'Advanced Protocol Interface'],
    'In object-oriented programming, what is encapsulation?': ['A mechanism of bundling data and methods that operate on the data.', 'A process of converting data into a byte stream.', 'A way to organize code into reusable units.', 'A technique for optimizing code execution.'],
    'What is the purpose of the "pass" statement in Python?': ['To create an empty code block.', 'To terminate the program immediately.', 'To skip the current iteration in a loop.', 'To raise an exception.'],
    'What is the difference between a list and a tuple in Python?': ['Lists are mutable, and tuples are immutable.', 'Lists can only contain integers, while tuples can contain any data type.', 'Lists are indexed from 0, and tuples are indexed from 1.', 'There is no difference; they can be used interchangeably.'],
    'What does the term "DRY" stand for in software development?': ['Don\'t Repeat Yourself', 'Do Repeat Yourself', 'Do Refactor Yourself', 'Don\'t Refactor Yourself']
    #these questions are from internet
}

def start_quiz():
    questions = GetQuestions(
        QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ
    )

    #Number of correct answers
    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question, alternatives)

    print(f"\nYou got {num_correct} correct out of {num} questions")

#to generate random questions 
def GetQuestions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

#asks the question and display options of it
def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = getUserChoice(question, ordered_alternatives)
    if answer == correct_answer:
        print(" Correct! ")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0

#get the user input and returns to check the correct answer
def getUserChoice(question, alternatives):
    print(f"{question}?")
    all_options = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in all_options.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in all_options:
        print(f"Please answer one of {', '.join(all_options)}")

    return all_options[answer_label]


if __name__ == "__main__":
    start_quiz()
    print("Great to have your time !! Thank you")
