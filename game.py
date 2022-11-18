"""Number Guessing Game"""

import numpy as np

number = np.random.randint(1, 101) # Generating number between 1 and 100

count = 0

while True:
    count += 1
    predict_number = int(input("Please guess the number between 1 and 100: "))
    
    if predict_number > number:
        print("Try guessing lower!")
        
    elif predict_number < number:
        print("Try guessing bigger!")
        
    else:
        print(f"Congratulations! You guessed the number which was {number}, in {count} tries!")
        break # Game ends and the cycle breaks
