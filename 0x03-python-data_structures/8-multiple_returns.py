#!/usr/bin/python3
def multiple_returns(sentence):
    len_str = len(sentence)
    first = sentence[0]
    return (len_str, first if len_str > 0 else None)
