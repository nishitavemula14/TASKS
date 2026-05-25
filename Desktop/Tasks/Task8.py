def invert_dict(d):
    inverted = {}

    for key, value in d.items():
        inverted[value] = key

    return inverted


d = {"a": 1, "b": 2, "c": 3}

print(invert_dict(d))