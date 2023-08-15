def common_elements(set_1, set_2):
    #create a new set to store the common elements
    common_set = set()
    #iterate through the elements in set_1
    for elements in set_1:
        #condition to check if elements in set_1 are in set_2
        if elements in set_2:
            #add the elements to the new set store
            common_set.add(elements)
        return common_set