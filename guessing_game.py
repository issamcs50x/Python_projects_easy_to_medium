## the guessing game
# استيراد مكتبة لتوليد رقم عشوائي بين 1 و 100
from random import randint

rand_num = randint(1, 100)
# الاستمرار في سؤال المستخدم ليخمن رقم
while True:
    answer = input("Guess the number between 1 and 100: ").strip()
    try:
        number = int(answer)
        # اذا كان ما ادخله المستخدم رقم افعل التالي
        # مقارنة ما ادخله المستخدم بالرقم المولد
        diff = abs(rand_num - number) 
        if number > rand_num:
            if diff > 5:
                print("Far high!")
            else:
                print("High but close!")
        elif number < rand_num:
            if diff > 5:
                print("Far low!")
            else:
                print("Low but close!")
        else:
            print("Congratulation! You guessed the number.")
            break
    except ValueError:
        # طباعة رسالة خطا في حالة ادخال المستخدم لقيمة غير رقمية
        print("Please enter a valid number")
