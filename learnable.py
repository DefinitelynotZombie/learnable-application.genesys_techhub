def nth_most_rare(list, n):
    # Created a dictionary to store the frequency of each element
    frequency_dict = {}

    # append the number and the frequency to the frequency dictionary
    for item in list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    # for debugging
    print(frequency_dict)

    # Sort the dictionary items based on frequency (rarest to most common)
    sorted_items = sorted(frequency_dict.items(), key=lambda x: x[1])

    # for debugging
    print(sorted_items)

    # Check if n is within a valid range
    if n <= 0 or n > len(sorted_items):
        return None  # in case of invalid input for n

    # the nth rarest item
    return sorted_items[n - 1][0]


# Example used:
lst = [5, 4, 5, 4, 5, 4, 4, 5, 3, 3, 3, 2, 2, 1, 5]
n = 2
result = nth_most_rare(lst, n)

print(f"The 2nd rarest item is: {result}")
