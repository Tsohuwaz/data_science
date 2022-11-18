"""Game that guesses the 
number of the guessing game
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Randomly guessing a number

    Args:
        number (int, optional): Guessed number. Defaults to 1.

    Returns:
        int: Number of tries
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # Generating a number between 1 and 100
        if number == predict_number:
            break
    return count

print(f"Numbers of tries:{random_predict()}")

def score_game(random_predict) -> int:
    """For how many attempts on average out of 1000 approaches our algorithm guesses

    Args:
        random_predict (_type_): Guessing function

    Returns:
        int: Average try count
    """
    count_lst = [] # List for saving the amount of tries
    np.random.seed(1) # fix seed for reproducibility
    random_array = np.random.randint(1, 101, size=(1000)) # Memorised the list of numbers
    
    for number in random_array:
        count_lst.append(random_predict(number))
    
    score = int(np.mean(count_lst))
    
    print(f"You algorithm is guessing the number on average {score} tries")
    return score

# RUN
score_game(random_predict)