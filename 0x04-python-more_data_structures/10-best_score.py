#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best_score = next(iter(a_dictionary.values()), None)
        for key in a_dictionary:
            if a_dictionary[key] > best_score:
                best_score = a_dictionary[key]
        return best_score
    else:
        return None
