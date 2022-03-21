import jovian
from jovian.pythondsa import evaluate_test_cases

def test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid: ", mid, ", mid_number: ", mid_number)
    if mid_number == query:
        if mid-1 >=0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

def locate_card(cards, query):
    # iterate through the list and check whether the number corresponds
    lo, hi = 0, len(cards)-1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]
        print("lo: ", lo, "hi: ", hi, "mid: ", mid, "mid_number: ", mid_number)
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

# card = [13, 11, 10, 7, 4, 3, 2, 1]
# q = 7
# output = 3
tests = [{
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}, {
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
}, {
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0
}, {
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
}, {
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
}, {
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
}, {
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
}]
# query is in the middle
# the query is the first element
# cards contains just one element, query
# cards do not contain query
# the card is empty
# numbers can repeat in cards
# query occurs multiple times


# result = locate_card(tests[1]['input']['cards'], tests[1]['input']['query'])
evaluate_test_cases(locate_card, tests)
# result = tests[0]['output']
# jovian.commit(project='python-binary-search', environment=None)
# print(result)
# print(tests)
