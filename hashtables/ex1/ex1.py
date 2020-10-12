def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # if the length of the weights list is less than two then return None
    if len(weights) < 2:
        return None
    # if the length of the weights list is exactly two and their sum is equal to limit return their indices properly    
    if length == 2 and weights[0] + weights[1] == limit:
        return [1,0]

    # convert the weight list into a dictionary with weight as keys and values as indices
    weights_table = {}
    for i in range(0, length):
        value = i
        key = weights[i]
        weights_table[key] = value # index is stored as a value in the dictionary 

    # now check if the complemnet of the weight is present inside the weights table. If you find the 
    # complement wight exists in the dictionary then push its index to a new list.
    result = []
    for weight in weights:
        # Find the complement weight
        complement_weight = limit - weight
        # if the complement weight exists inside the dictionary or weights table
        if complement_weight in weights_table:
            # then push the index of it to the result list
            complemnet_weight_index = weights_table[complement_weight]
            result.append(complemnet_weight_index)
    # Make sure the result list contains index and its complemnet index
    if len(result) == 2:
        return result
    
    return None
