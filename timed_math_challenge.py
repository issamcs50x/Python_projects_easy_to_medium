import random
import time

def generate_x_y():
    while True:
        x, y = random.randint(MIN, MAX), random.randint(MIN, MAX)
        if x > y:
            return x, y

def operator(x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "×":
        return x * y
    # No problem with zeroDivisionError because MIN > 0 
    else:
        return x / y

MIN = 1
MAX = 100
operations = ["+", "-", "×", "÷"]

score = 0

start = time.time()
for _ in range(len(operations)):
    rand_op = random.choice(operations)
    operations.remove(rand_op)
    x, y = generate_x_y()
    question = f"{x} {rand_op} {y} = "
    while True:
        try:
            answer = int(input(question).strip())
        except ValueError:
            print("You answer must be a number!")
        else:
            break

    result = operator(x, y, rand_op)
    if answer == int(result):
        score += 1
        print("Correct answer!")
    else:
        print("Wrong answer!")
        print(f"The correct is: {question}{result}")

end = time.time()
print(f"Your score is: {score}")
print(f"Your time is: {end - start}")
