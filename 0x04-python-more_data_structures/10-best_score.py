#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        first_key = next(iter(a_dictionary.keys()))
        best_score_value = a_dictionary[first_key]
        best_score_key = first_key

        for key, value in a_dictionary.items():
            if value > best_score_value:
                best_score_value = value
                best_score_key = key

        return best_score_key
    else:
        return None
