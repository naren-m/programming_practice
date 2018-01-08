def number_needed(a, b):
    d = dict()
    for l in a:
        if l in d:
            d[l] = d[l] + 1
        else:
            d[l] = 1
    for l in b:
        if l in d:
            d[l] = d[l] + 1
        else:
            d[l] = 1

    num_to_delete = 0
    for k, v in d.items():
        print(k, v)
        if v <=1:
            num_to_delete += 1


    print(d)
    return num_to_delete

a = 'cde'
b = 'abc'

print(number_needed(a, b))


