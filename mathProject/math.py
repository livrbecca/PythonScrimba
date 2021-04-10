from random import randrange as r
from time import time as t

no_questions = int(input("how many questions do you want: "))
score = 0
start = t()
for q in range(no_questions):
    num1, num2 = r(1, 11), r(1, 11)
    ans = num1 * num2

    u_ans = int(input(f'{num1} x {num2} = '))

    if u_ans == ans:
        score += 1
    end = t()

print(f'thanks for playing, you got {score} out of {no_questions} correct. {round(score / no_questions*100)}% in {round(end-start,1)} seconds')
    