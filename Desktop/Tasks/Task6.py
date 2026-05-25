def alternate_lists(a, b):
    result = []

    min_length = min(len(a), len(b))

    # Alternate elements
    for i in range(min_length):
        result.append(a[i])
        result.append(b[i])

    # Add remaining elements
    result.extend(a[min_length:])
    result.extend(b[min_length:])

    return result


a = [1, 2]
b = ['a', 'b', 'c']

print(alternate_lists(a, b))