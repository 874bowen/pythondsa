import math

from jovian.pythondsa import evaluate_test_cases


tests = [{  # query is in the middle
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0]
    },
    'output': 5.5
}, {
    'input': {  # the query is the first element
        'cards': [4, 2, 1, -1]
    },
    'output': 1.5
}, {
    'input': {  # cards contains just one element, query
        'cards': [6]
    },
    'output': 6
}, {
    'input': {  # cards do not contain query
        'cards': [9, 7, 5, 2, -9]
    },
    'output': 5
}, {
    'input': {  # the card is empty
        'cards': []
    },
    'output': -1
}, {
    'input': {  # numbers can repeat in cards
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
    },
    'output': 4.5
}, {
    'input': {  # query occurs multiple times
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
    },
    'output': 6
}]


def find_median(cards):

    lo, hi = 0, len(cards)-1
    mid = (hi + lo) / 2
    print(lo, hi)
    # case for even length of list
    while lo <= hi:
        if type(mid) == int:
            median = cards[mid]
            return median
        else:
            median = (cards[math.ceil(mid)] + cards[math.floor(mid)])/2
            return median
    return -1


# print(find_median([1, 2, 3, 4]))
evaluate_test_cases(find_median, tests)
# num = 14.5
#
# print(math.floor(num))