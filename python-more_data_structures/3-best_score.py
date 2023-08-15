def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    sorted_dict = sorted(a_dictionary.items(), key=lambda x:x[1])
    converted_dict = dict(sorted_dict)
    res = list(converted_dict.keys())[0]
    return res