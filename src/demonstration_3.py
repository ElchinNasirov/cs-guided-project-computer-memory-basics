"""
Given a list of integers `lst`, any integer with a frequency that is equal to its value is considered a **lucky integer**.

Write a function that returns the lucky integer from the array. If the array contains multiple lucky integers, return the largest one. If there are no lucky integers return -1.

**Example 1**:

Input: arr = [2,3,3,3,4]
Output: 3

**Example 2**:

Input: arr = [1,2,2,3,3,3,4,4,4,4]
Output: 4

**Example 3**:

Input: arr = [1,1,2,2,2]
Output: -1
"""
def find_lucky(lst):
    # UNDERSTAND
    # if the count = value, return the value
    # PLAN
    # Define an output variable
    output = -1
    # Sort the list from largest to smallest
    lst.sort(reverse=True)
    # Make a set
    set_list = set(lst)
    # Iterate through the set, counting the # of times each value shows up
    for number in set_list:
        # Make a count variable
        count = lst.count(number)
        # Check if the count == the value
        if number == count:
            # If it does, add it to output variable
            output = number
    # If nothing matches, return -1
    return output

print(find_lucky([1,1,2,2,2]))
print(find_lucky([1,2,2,3,3,3,4,4,4,4]))