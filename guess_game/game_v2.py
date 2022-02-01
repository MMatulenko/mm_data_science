"""Guess the right number game, number is generated and found by pc
"""

import numpy as np

numbers_list=range(101)

def random_predict(number: int = 1) -> int:
    """guess the right number with binary search 

    Args:
        number (int, optional): hidden number. Defaults to 1.

    Returns:
        int: count of tries
    """
    count = 0
    left_border=0
    right_border=101
    middle_border=0
    #binary search, numbers are always from 1-100, that is why we are allowed not to use array
    while left_border<=right_border:
        count += 1
        middle_border=(left_border+right_border)//2
        if middle_border==number:
            return count
        if number<middle_border:
            right_border=middle_border-1
        else:
            left_border=middle_border+1
    return -1


def score_game(random_predict) -> int:
    """function that counts mean number of tries to guess the right number by using binary search

    Args:
        random_predict ([function]): guess function

    Returns:
        int: mean tries number
    """
    count_ls = []
    #np.random.seed(1)  # fix the seed
    random_array = np.random.randint(1, 101, size=(1000))  # list of random numbers

    for number in random_array:
        if random_predict(number)==-1:
            print("Error")
            return -1
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Your algorithm finds the right number in : {score} tries")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    

