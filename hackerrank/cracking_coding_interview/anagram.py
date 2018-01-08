
def number_needed(a, b):
    l = [0] * 26

    for v in a:
        l[97 - ord(v)] += 1


    for v in b:
        l[97 - ord(v)] -= 1

    print(l)
    s = 0
    for v in l:
        s += abs(v)
    return s

def number_needed1(a, b):
    num_to_delete = 0
    if a not in b:
        print("Nothing common", len(set(a)) + len(set(b)))
        # return len(set(a)) + len(set(b))

    d = dict()
    for l in a:
        if d.has_key(l):
            d[l] = d[l] + 1
        else:
            d[l] = 1
    print("Word", a, "dict", d)
    d = dict()
    for l in b:
        if d.has_key(l):
            d[l] = d[l] + 1
        else:
            d[l] = 1

    print("Word", b, "dict", d)
    for k, v in d.items():
        num_to_delete += abs(v)

    return num_to_delete

a = 'fcrxzwscanmligyxyvym'
b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

print(number_needed(a, b))

