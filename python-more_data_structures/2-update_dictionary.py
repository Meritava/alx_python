def update_dictionary(a_dictionary, key, value):
    if not isinstance(key, str):
        raise TypeError("Key must be a string") #ensure the key provided is a string
    if a_dictionary == None:   #check if dictionary is empty
        a_dictionary = {}  #create an empty dictionary
        a_dictionary[key] = value   #update the dictionary with new provided values
    return a_dictionary

    