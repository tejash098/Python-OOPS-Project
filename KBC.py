# KBC Style Game
questions = [
    "Q1. What is the capital of India?",
    "Q2. Who is known as the father of the nation (India)?",
    "Q3. Which planet is known as the Red Planet?",
    "Q4. What is the national animal of India?",
    "Q5. Who wrote the national anthem of India?"
]
options = [
    ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
    ["A. Bhagat Singh", "B. Mahatma Gandhi", "C. Subhash Chandra Bose", "D. Jawaharlal Nehru"],
    ["A. Venus", "B. Jupiter", "C. Mars", "D. Saturn"],
    ["A. Tiger", "B. Lion", "C. Elephant", "D. Peacock"],
    ["A. Bankim Chandra Chatterjee", "B. Rabindranath Tagore", "C. Sarojini Naidu", "D. Premchand"]
]
answers = ["B", "B", "C", "A", "B"]
prize_money = [1000, 5000, 10000, 20000, 50000]

print(" Welcome to Kaun Banega Crorepati (KBC) \n")
input('Press Enter to continue..')
amount_won = 0

for i in range(len(questions)):
    print(f'Question for {prize_money[i]} rupees \n')
    print(questions[i],'\n')
    print(options[i],'\n')
    ans = input('Enter your option:')
    if ans.capitalize() == answers[i]:
        amount_won += prize_money[i]
        print(f'Congrats! You have won {prize_money[i]} \nYour update amount is {amount_won} \n')
        if amount_won == sum(prize_money):
            print('You completed the Quiz. your winning amount is', amount_won, 'Bye!')
            break
        input('Press Enter to Continue...')
    else:
        print('Wrong answer! Your winning amount is',amount_won)
        break
    