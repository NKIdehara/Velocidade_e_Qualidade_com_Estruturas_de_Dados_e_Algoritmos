def greatestNumber(array):
    greatest = array[0]
    for i in array:
        if i > greatest:
            greatest = i
    return greatest
