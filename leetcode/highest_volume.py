import jovian
from jovian.pythondsa import evaluate_test_cases

tests = [{  # query is in the middle
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0]
    },
    'output': 3
}, {
    'input': {  # the query is the first element
        'cards': [4, 2, 1, -1]
    },
    'output': 0
}, {
    'input': {  # cards contains just one element, query
        'cards': [6]
    },
    'output': 0
}, {
    'input': {  # cards do not contain query
        'cards': [9, 7, 5, 2, -9]
    },
    'output': -1
}, {
    'input': {  # the card is empty
        'cards': []
    },
    'output': -1
}, {
    'input': {  # numbers can repeat in cards
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
    },
    'output': 7
}, {
    'input': {  # query occurs multiple times
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
    },
    'output': 2
}]


def highest_vol_search(cards):
    new_c = cards.copy()
    for i in range(len(cards)):
        for n in range(len(new_c)):
            if cards[i] < cards[n] and i != n:
                width = cards[i].index - cards[]
                vol = cards[i] * width
                print('n', n, 'i', i, 'width', width, 'vol', vol)
                print(vol)
            elif cards[i] > cards[n] and i != n:
                width = i - n
                vol = cards[n] * width
                print('n', n, 'i', i, 'width', width, 'vol', vol)
                print(vol)


(highest_vol_search(tests[1]['input']['cards']))
