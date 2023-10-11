#!/usr/bin/python3
def common_elements(set_1, set_2):
    # Initialize an empty set to store common elements
    common_set = set()

    # loop through the elements in set_1
    for element in set_1:
        # Check if the element is in set_2
        if element in set_2: # If it is , add it to the common_set
            common_set.add(element)

            return common_set
