def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}

    for i, weight in enumerate(weights):
        cache[weight] = i
    for i, weight in enumerate(weights):
        if limit - weight in cache:
            x = cache[limit - weight]
            if i > x:
                return (i, x)
            else:
                 return (x, i)

    return None
