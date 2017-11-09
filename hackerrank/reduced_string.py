# Problem https://www.hackerrank.com/challenges/reduced-string/problem
def super_reduced_string(s):
    # Complete this function
    res = list()
    for c in s:
        if res and res[-1] == c:
            res.pop()
        else:
            res.append(c)

    if len(res) == 0: return 'Empty String'

    return ''.join(res)


tests = [{
    "input": "aaabccccddd",
    "expected": "abd"
}, {
    "input": "aa",
    "expected": ""
}, {
    "input": "a",
    "expected": "a"
}]

for t in tests:
    print(t["input"], super_reduced_string(t["input"]), t["expected"])
