def multiple_returns(sentence):
    if len(sentence) == 0:
        return None, 0
    else:
        return len(sentence), sentence[0]