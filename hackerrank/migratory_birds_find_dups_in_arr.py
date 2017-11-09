# Problem https://www.hackerrank.com/challenges/migratory-birds/problem


def migratoryBirds(n, ar):
    # Complete this function
    bird_count = [0] * 6
    max_count = 0
    for bird_type in ar:
        bird_count[bird_type] += 1
        if max_count <= bird_count[bird_type]:
            max_count = bird_count[bird_type]
            id = bird_type

    return id


def migratoryBirds_using_dict(n, ar):
    # Complete this function
    max_count = 0
    max_type = 0
    bird_dict = dict()
    for i, bird in enumerate(ar):
        if bird in bird_dict:
            bird_dict[bird] += 1
        else:
            bird_dict[bird] = 1
        if max_count <= bird_dict[bird]:
            max_count = bird_dict[bird]
            max_type = bird

    return max_type


arr = [1, 4, 4, 4, 5, 3]
print(migratoryBirds(len(arr), arr))

arr = [1, 5, 5, 5, 4, 4, 4, 3]
print(migratoryBirds(len(arr), arr))
