# URLify

def _move_elems_by(s, n):
    for i in range(n):
        pass

def urlify(s, l):
    string = [None] * l
    for i in range(len(s)):
        string[i] = s[i]



    return None

tests = [
    {'input': ("my leet code", 18), 'expected': "my%20leet%20code" },
]

for test in tests:
    n = urlify(*test['input'])
    print('Expected {}, got {}'.format(test['expected'], n))
    assert n == test['expected']