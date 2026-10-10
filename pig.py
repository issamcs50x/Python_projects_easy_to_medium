# 1- تحديد عدد الاعبين من 2 ل 6
# 2- تحديد الاعب الحالي من ضمن فقط من لم يتم سحب منهم الدور حاليا
# 3- رمي النرد
# 4- اذا رقم النرد من 2 ل 6 تتم اضافته للسلة المؤقتة 
    # - يتم تخيير الاعب بين الاستمرار او التوقف حاليا
    # - اذا كان رقم النرد هو 1 يتم تصفير سلة الاعب المؤقتة و يسحب دوره 
        # اذا استنفد الاعب عدد ادواره الاقصى
        # يسحب منه الدور لياخده لاعب اخر و ايضا تصفر سلته
    #  و لاتخزن نقاطه طلما لم يضغط hold
# 5- بعد كل دورة نتحقق هل هناك لاعب استوفى شرط الربح اذا كان ننهي اللعبة

import random

def get_players_number():
    while True:
        user_input = input("How many players? (2-6): ").strip()
        try:    
            players_number = int(user_input)
            if players_number < 2 or players_number > 6:
                print("Invalid number!")
            else:
                return players_number
        except ValueError:
            print("Inavlid input!")

def create_players_safe(players_number):
    return {"player" + str(i+1): 0 for i in range(players_number)}

def determing_active_player(players_safe, withdrawn_player):
    players = list(players_safe.keys())
    if withdrawn_player :
        next_index = (players.index(withdrawn_player) + 1) % len(players)
        return players[next_index]
    return random.choice(players)

def roll_dice():
    return random.randint(1, 6)

def dice_logic(dice, turn_score):
    if dice == 1:
        return 0
    else:
        return turn_score + dice

def score_deposit(players_safe, turn_score, active_player):
    players_safe[active_player] += turn_score

def hold_keep_logic(players_safe, turn_score, active_player):
    while True:
        choice = input(f"What do you want to do next '{active_player}'?\n1- Keep\n2- Hold\nYour answer: ").strip()
        if choice == "1":
            return True
        elif choice == "2":
            score_deposit(players_safe, turn_score, active_player)
            return False
        else:
            print("Invalid choice")

def winning_case(players_safe, winnig_score):
    for plr, score in players_safe.items():
        if score >= winnig_score:
            return plr
    return False

def display_players_safe(players_safe):
    print("-" * 10)
    for plr, score in players_safe.items():
        print(f"{plr}: {score}", end=" | ")
    print()
    print("-" * 10)


def main():

    WINNING_SCORE = 10

    players_safe = create_players_safe(get_players_number())

    withdrawn_player = ""

    activity = False

    while True:
        # تبديل الادوار طالما تحقق شرط النرد 1 او اختار الاعب الحفض 
        if not activity:
            max_rolls = random.randint(3, 8)

            active_player = determing_active_player(players_safe, withdrawn_player)
            withdrawn_player = active_player

            activity = True
            turn_score = 0
            roll_count = 0

            display_players_safe(players_safe)
            print(f"{active_player} is playing")
        
            
        # تدوير النرد و طباعته
        dice = roll_dice()
        roll_count += 1
        print(f"{active_player}, your dice is '{dice}'")

        # اذا صادف الاعب رقم 1 يتم جعله لاعب منسحب  و يتم ايقاف نشاطه حاليا
        turn_score = dice_logic(dice, turn_score)
        if not turn_score:
            activity = False
            continue

        # الاعب هو من يقرر هل يستمر او يتوقف لحفض تقدمه
        activity = hold_keep_logic(players_safe, turn_score, active_player)

        # ايقاف نشاط الاعب اذا تخطى عدد مرات الرمي في دوره الحالي
        if roll_count == max_rolls:
            print("🤡")
            activity = False

        # اذا وصلت نقاط الاعب المخزنة لشرط الفوز تنتهي اللعبة
        winning = winning_case(players_safe, WINNING_SCORE)
        if winning:
            print(f"congratulation, '{winning}' win!")
            display_players_safe(players_safe)
            return
        
main()

