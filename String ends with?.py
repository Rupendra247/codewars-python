def solution(text, ending):
    # your code here...
    n = len(ending)
    if n > len(text):
        return False
    if text[-n:] == ending:
        return True
    else:
        return False
    pass