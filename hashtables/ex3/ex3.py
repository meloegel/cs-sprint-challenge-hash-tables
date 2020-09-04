def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = {}

    lists = len(arrays)

    for list in arrays:
        for i in list:
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 1
    result = []
    for x in cache:
        if cache[x] == lists:
            result.append(x)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
