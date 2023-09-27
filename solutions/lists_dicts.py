# TODO: Implement a function that returns a list of numbers from 1 to n
def generate_numbers(n):
    list = [1]
    for i in range (2,n+1,1):
        list.append(i)
    return list

# TODO: Implement a function that returns a dictionary where keys are numbers from 1 to n and values are their squares
def generate_squares(n):
    pass
    for i in range (1,n+1,1):
        list= {i: i**2 for i in range(1, n + 1)}
    return list

# TODO: Implement a function that merges two lists in an alternating fashion
def merge_lists(list1, list2):
    pass
    list3 = []
    len1, len2 = len(list1), len(list2)
    maxx = max(len1, len2)

    for i in range(maxx):
        if i < len1:
            list3.append(list1[i])
        if i < len2:
            list3.append(list2[i])
    return list3

# TODO: Implement a function that returns a list and replicates the dictionary keys based on their respective values
def multiply_keys(data):
    pass
    result = []
    
    for i, value in data.items():
        result.extend([i] * value)
    
    return result


# TODO: Implement a function that converts a list of strings to a dictionary with the string as the key and its length as the value
def list_to_dict(items):
    pass

    result = {value: len(value) for value in items}
    return result

# TODO: Implement a function to find the majority element in a list
def majority_element(nums):
    pass
    i = 0
    j = 0
    a = 0
    b = 0
    c = 0

    
    for i in nums :
        h = i
        a = 1
        for j in nums:
            if j == h:
                a = a + 1 
            if a > b:
                b = a
                c = i
    return c


# TODO: Implement a function that filters a dictionary based on a threshold value. If the value of any key in the dictionary is greater than the threshold, that key-value pair should be retained in the output dictionary. Otherwise, it should be excluded.
def filter_dictionary(data, threshold):
    pass
    result = {key: value for key, value in data.items() if value >= threshold}
    return result
   
