import json
import random


def random_func():

    # [1, 2, 4, 5, 6, 7]
    numS1 = [1, 2, 4, 7]
    # [10, 11, 12, 13, 14, 15, 16, 17]
    numS2 = [10, 11, 12, 16, 17]
    # [18,21, 22, 23, 24, 26, 28, ,14, 15, 16, 17]
    numS3 = [18, 22, 23, 24, 28, 14, 15, 16, 17]
    # []
    numS4 = list(range(17,41))
    numS5 = list(range(20, 40))
    numS6 = list(range(35, 45))
    
    s1 = random.choices(numS1, weights=None, cum_weights=None, k=1)[0]
    s2 = random.choices(numS2, weights=None, cum_weights=None, k=1)[0]
    s3 = random.choices(numS3, weights=[3, 1, 1, 1, 1, 1, 1, 1, 1], cum_weights=None, k=1)[0]
    s4 = random.choices(numS4, weights=None, cum_weights=None, k=1)[0]
    s5 = random.choices(numS5, weights=None, cum_weights=None, k=1)[0]
    s6 = random.choices(numS6, weights=None, cum_weights=None, k=1)[0]
        
    result = (s1,s2,s3,s4,s5,s6)

    return result
    
def lambda_handler(event, context):
    response = []
    for i in range(5):
        a = random_func()
        response.append(a)

    return (response)