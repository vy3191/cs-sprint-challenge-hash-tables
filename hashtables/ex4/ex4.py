def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Make an empty list
    result = []
    # Make an empty dictionary(or hash_table)
    numbers_table = {}
    # Loop through the all the numbers in a given array
    for i in range(0,len(a)):
        number = a[i]
        # if the number is not a 0 or not in a table
        if number not in numbers_table and number != 0:
            # then add that number to the table
            numbers_table[number] = 1
            # print(numbers_table)
            # if find the negative number in the table then push it to the list
            # Make sure to push only positive number so that the test pass
            if -number in numbers_table:
                result.append(abs(number))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
