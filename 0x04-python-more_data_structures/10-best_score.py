#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    output = list(a_dictionary.keys())[0]
    large = a_dictionary[output]
    for k, v in a_dictionary.items():
        if v > large:
            large = v
            output = k
    return output
