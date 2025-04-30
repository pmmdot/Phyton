import random
import time

OPERATORS = ["+", "-", "*"]
presets  = {"EASY" : "0 5" , "STANDARD" : "0 10", "HARD" : "0 100", "IMPOSSIBLE" : "100 9999"}
rvar2  = {"1" : "EASY" , "2" : "STANDARD", "3" : "HARD", "4" : "IMPOSSIBLE"}
wrong = 0

print("Welcome to Mather!")
name = input("ENTER YOUR NAME: ")
print("SELECT DIFFICULTY")

difficulty = input("""
1. EASY
2. STANDARD
3. HARD
4. IMPOSSIBLE
>>>>>>>>>>>>>>>> """)

selecteddifficulty = rvar2[difficulty]
rvar3 = presets[selecteddifficulty].split(" ")
selecteddifficulty = rvar2[difficulty]
MIN_OPERAND = int(presets[selecteddifficulty].split(" ")[0])
MAX_OPERAND = int(presets[selecteddifficulty].split(" ")[1])

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

print("--------------------------------------------------------")
print(f"You are about to play MATHER **{selecteddifficulty}**")
input("To begin, Press ENTER ")
start_time = time.time()

for i in range(11):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem # :::" + str(i + 1) + "::: " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = end_time - start_time
accuracy = ((21 -wrong) / 21) * 100
print("--------------------------------------------------------")
print(f"Nice work! You finished in {total_time} seconds! with {accuracy}% accuracy!")

L = open("LeaderBoard.txt", "a")
L.write(f"Player : {name}\n Difficulty: {selecteddifficulty}\n Score(time): {total_time}\n Accuracy: {accuracy}\n")
L.close()
