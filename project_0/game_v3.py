import numpy as np
import math

def random_predict(number:int=1) -> int:
        
    """Randomly guessing the number
    Args:
        number(int, optional): Guessed number. Defaults to 1.
    Returns:
        int: Number of tries
    """
    count = 0
    predict_number = np.random.randint(1, 101)
    max_number = 100
    min_number = 1

    my_list = range(min_number, max_number+1)
    while True:
        count += 1 
        if number == predict_number:
            break
        elif predict_number > number:
            max_number = predict_number
            my_list = range(min_number, max_number+1)
            predict_number = int((min_number + max_number)/2)
            
        elif predict_number < number:
            min_number = predict_number
            my_list = range(min_number, max_number+1) 
            predict_number = int((min_number + max_number)/2)
    
    return(count)
    
print(f'Number of tries:{random_predict()}')

def score_game(random_predict) -> int:
    """For how many attempts on average out of 1000 approaches our algorithm guesses
    Args:
        random_predict ([type]): guessing function
    Returns:
        int: average guessing tries
    """

    count_ls = []
    np.random.seed(1) 
    random_array = np.random.randint(1, 100, size=(1000))
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f'Your algorithm guesses the number on average in: {score} tries')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)