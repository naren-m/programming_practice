# Problem https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem


class Stack(object):
    def __init__(self):
        self.list = list()

    def push(self, val):
        self.list.append(val)

    def peek(self):
        return self.list[-1]

    def pop(self):
        val = self.list[-1]
        del self.list[-1]
        return val

    def __str__(self):
        return str(self.list)


def is_matched(expression):
    if len(expression) % 2 != 0:
        return False

    stack = list()
    for e in expression:
        if e == "{": stack.append("}")
        elif e == "(": stack.append(")")
        elif e == "[": stack.append("]")
        else:
            if len(stack) == 0 or stack[-1] != e:
                return False
            stack.pop()
    if len(stack) > 0: return False
    return True


tests = [{
    "input": "{[()]}",
    "expected": True
}, {
    "input": "{[(])}",
    "expected": False
}, {
    "input": "{{[[(())]]}}",
    "expected": True
}, {
    "input": "{}[]()",
    "expected": True
}, {
    "input": ")}{){(]{)([)}{)]())[(})[]]))({[[[)}[((]](])][({[]())",
    "expected": False
}]

for t in tests:
    res = is_matched(t['input'])
    print(t, res)
    if res != t['expected']:
        print("Test case failed:", res, t['expected'])