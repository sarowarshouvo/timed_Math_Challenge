import random
import time

OPERATOR = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problems():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATOR)

    expr = str(left) +" "+operator+" "+str(right)
    answer = eval(expr) #eval basically evalute basic python string
    return expr,answer

input("Press Enter to start! ")
print("----------------------")
start_time = time.time()
wrong = 0

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problems()
    while True:
        guess = input("Problem #" +str(i+1)+ ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time,2)
print("----------------------")
print("Nice work! You finished in",total_time,"seconds!")
print("U wronged",wrong,"times")

