#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best_score_value = next(iter(a_dictionary.values()), None)
        best_score_key = None

        for key, value in a_dictionary.items():
            if value > best_score_value:
                best_score_value = value
                best_score_key = key

        return best_score_key
    else:
        return None
