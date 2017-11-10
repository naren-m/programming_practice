# Problem Grokking algorithms book. Exercise 4.1


def find_sum(l):
    if len(l) == 0:
        return 0

    return l[0] + find_sum(l[1:])


l = [1, 2, 3, 4, 5]

print(find_sum(l))