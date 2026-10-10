#1. display quiz question and choices

#2. ask the user for his answer

#3. keep asking if it is an invalid choice

# otherwise comparing the user's answer to the question's right answer

#4. increase the user's score if his answer was correct


from random import shuffle

from string import ascii_lowercase

# Storing test questions, options, and answers in a list of dictionaries in the form of

# {question: value, options: (opt1, opt2, opt3), answer: value}

quizzes = [

    {"question": "What is the largest continent on Earth by land area?",

     "choices": ("Africa", "Asia", "North America", "Eurasia"),

     "answer": "Eurasia"},

    {"question": "In which year did humans first land on the Moon?",

     "choices": ("1965", "1969", "1972"),

     "answer": "1969"},

    {"question": "Which gas do plants absorb from the atmosphere during photosynthesis?",

    "choices": ("Oxygen", "Nitrogen", "Carbon dioxide"),

    "answer": "Carbon dioxide"}

]

def main():

    score = 0

    # display quiz

    shuffle(quizzes)

    for quiz_num, quiz in enumerate(quizzes, start=1):

        print(f"{quiz_num}. {quiz['question']}")

        letters = ascii_lowercase[0:len(quiz["choices"])]

        for choice_num, choice in enumerate(quiz["choices"]):

            print(f" {letters[choice_num]}. {choice}")    

        user_answer = validate_answer(letters)

        # checking if the user's answers are correct then increase his score

        review = review_answer(quiz, user_answer, letters)

        if review:

            score += 1

    # display results

    display_results(score)


def validate_answer(letters):

    # keep asking the user the same question as long as they haven't answered from the options.

    while True:  

        user_answer = input(f"What is your answer? ({'/'.join(letters)}): ").strip().lower()

        if user_answer in letters:

            return user_answer

        else:

            print("Invalid choice!")


def review_answer(quiz, user_answer, letters):

    #1. get the answer location based on the list of options

    #2. get the letter based on that location

    answer_letter = letters[quiz["choices"].index(quiz["answer"])]

    if user_answer == answer_letter:

        print("Correct!")

        return True

    print(f"False! the correct answer is :'{quiz["answer"]}'")

    return False


def display_results(score):

    print(f"Your result: {int(score * 100 / len(quizzes))}%")

    print(f"You answered {score} out of {len(quizzes)} questions.")


main() 