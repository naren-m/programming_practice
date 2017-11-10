# Problem Grokking algorithms book. Exercise 4.3


def find_max(l):
    if len(l) == 1:
        return l[0]

    m = l[0]
    return max(find_max(l[1:]), m)


l = [1, 2, 3, 4, 5, -1, -2, 50]

print(find_max(l))

l = [-2]

print(find_max(l))