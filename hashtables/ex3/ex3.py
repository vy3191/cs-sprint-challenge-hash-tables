def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    hash_table = {}
    count = len(arrays)

    for single_array in arrays:
        for number in single_array:
            if number not in hash_table:
                hash_table[number] = 1
            else:
                hash_table[number] += 1  # if there are three arrays inside the main array the number should repeat that many times.
                if hash_table[number] == len(arrays):
                    result.append(number)
    # print(hash_table)     
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
