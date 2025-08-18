import random
def number_guessing_game():
    secret_number=random.randint(1,100)
    attempts=0
    guess=0
    
    print("welcome, guess the no b/w 1-100")
    
    while guess!=secret_number:
        try:
            guess_input=input("Take a Guess: \n")
            guess=int(guess_input)
            
            attempts+=1
            
            if guess<secret_number:
                print("Too low!Try again\n")
                
            elif guess>secret_number:
                print("Too high! Try again\n")
                
            else:
                print(f"Congratulations! You've guessed the number {secret_number} correctly!")
                print(f"it took you: {attempts}attempts  to win")
                
        except ValueError:
            print("invalid input")
            
if __name__=="__main__":
    number_guessing_game()