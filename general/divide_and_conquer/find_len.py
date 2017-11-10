# Problem Grokking algorithms book. Exercise 4.2

# Base condition: empty list


def find_len(l):
    if l == []:
        return 0

    return 1 + find_len(l[1:])


l = [1, 2, 3, 4, 5]

print(find_len(l))