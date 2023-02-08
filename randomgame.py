from random import randint
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))




while True:
    try:
        guess = int(input('guess a number 1-10:   '))
        if 0<guess<11:
            if (guess == answer):
                print("Your'e a geniues")
                break
        else:
            print('Hey bozo 1-10')
    except ValueError:
        print('Please enter a number')
        continue

