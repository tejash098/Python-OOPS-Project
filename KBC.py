class KBCGame:
    def __init__(self):
        self.questions = [
            "Q1. What is the capital of India?",
            "Q2. Who is known as the father of the nation (India)?",
            "Q3. Which planet is known as the Red Planet?",
            "Q4. What is the national animal of India?",
            "Q5. Who wrote the national anthem of India?"
        ]

        self.options = [
            ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
            ["A. Bhagat Singh", "B. Mahatma Gandhi", "C. Subhash Chandra Bose", "D. Jawaharlal Nehru"],
            ["A. Venus", "B. Jupiter", "C. Mars", "D. Saturn"],
            ["A. Tiger", "B. Lion", "C. Elephant", "D. Peacock"],
            ["A. Bankim Chandra Chatterjee", "B. Rabindranath Tagore", "C. Sarojini Naidu", "D. Premchand"]
        ]

        self.answers = ["B", "B", "C", "A", "B"]
        self.prize_money = [1000, 5000, 10000, 20000, 50000]
        self.amount_won = 0

    def start_game(self):
        print("\n Welcome to Kaun Banega Crorepati (KBC) \n")
        input("Press Enter to continue...")

        for i in range(len(self.questions)):
            self.ask_question(i)

            if self.amount_won == sum(self.prize_money):
                print(f"You completed the Quiz! Your total winning amount is {self.amount_won} rupees.")
                break

    def ask_question(self, index):
        print(f"\nQuestion for {self.prize_money[index]} rupees")
        print(self.questions[index])
        print()

        for opt in self.options[index]:
            print(opt)

        ans = input("\nEnter your option: ").upper()

        self.check_answer(ans, index)

    def check_answer(self, user_answer, index):
        if user_answer == self.answers[index]:
            self.amount_won += self.prize_money[index]
            print(f"\nCorrect! You won {self.prize_money[index]} rupees.")
            print(f"Your total amount is now: {self.amount_won}\n")
            input("Press Enter to continue...")
        else:
            print(f"\nWrong answer! Game Over.")
            print(f"Your winning amount is {self.amount_won}")
            exit()

game = KBCGame()
game.start_game()
