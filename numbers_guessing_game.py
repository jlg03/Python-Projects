import random
import time

def main_menu():
    valid_choice = False
    while not valid_choice:
        print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")
        print()
        print("Please select the difficulty level: \n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n4. Quit")
        print()
        user_input = input("Enter your choice: ")
        
        if user_input == "1":
            valid_choice = True
            answer = random_number()
            chances = easy_chances()
            game(chances=chances, answer=answer)
        elif user_input == "2":
            valid_choice = True
            answer = random_number()
            chances = medium_chances()
            game(chances=chances, answer=answer)
        elif user_input == "3":
            valid_choice = True
            answer = random_number()
            chances = hard_chances()
            game(chances=chances, answer=answer)
        elif user_input == "4":
            exit()
        else:
            print("That was an invalid input please try again")

def random_number():
    answer = random.randint(1, 100)
    return answer

def easy_chances():
    chances = 10
    return chances
def medium_chances():
    chances = 5
    return chances
def hard_chances():
    chances = 3
    return chances
    

def game(chances, answer):
    correct_guess = False
    original_chances = chances
    start_time = time.time()
    while not correct_guess:
        if chances == 0:
            print("Game Over, you ran out of chances")
            break
        while True:
            try:
                user_guess = int(input("Enter your guess: "))
                break
            except Exception:
                print("Invalid input. Try again")
        if user_guess < answer:
            print(f"Incorrect! The number is greater than {user_guess}")
            chances -= 1
        elif user_guess > answer:
            print(f"Incorrect! The number is less than {user_guess}")
            chances -= 1
        elif user_guess == answer:
            print(f"Congratulations! You guessed the correct number in {original_chances - chances + 1} attempts")
            end_time = time.time()
            print(f"You took {end_time - start_time:.2f} seconds")
            correct_guess = True
            valid_input = False
            while not valid_input:
                try:
                    print("Do you want to play again? (Y/N): ")
                    play_again = input("Enter your choice: ")
                    if play_again.upper() == 'Y':
                        valid_input = True
                        main_menu()
                    elif play_again.upper() == 'N':
                        valid_input = True
                        exit()
                    else:
                        print("That was an invalid input try again")
                except Exception:
                    print("That was an invalid input try again")
                    
        else:
            print("That was an invalid input try again!")


main_menu()