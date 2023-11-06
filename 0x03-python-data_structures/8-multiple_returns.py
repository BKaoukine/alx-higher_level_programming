#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is not None:
        first_char = sentence[0]
        sent_len = len(sentence)
        info = (sent_len, first_char)

        return info
    else:
        first_char = None
        sent_len = len(sentence)
        info = (sent_len, first_char)
        return info
