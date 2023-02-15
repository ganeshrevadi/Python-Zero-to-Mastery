import random
import sys


def run_guess(guess,answer):
    if 0<guess<11:
        if (guess == answer):
                print("Your'e a geniues")
                return True
    else:
        print('Hey bozo, I said 1-10')
        return False

 


answer = random.randint(1,10)

if __name__ == '__main__':
    while True:
        try:
            guess = int(input('guess a number 1-10:   '))
            if(run_guess(guess, answer)):
                break
        
        except ValueError:
            print('Please enter a number')
            continue

     