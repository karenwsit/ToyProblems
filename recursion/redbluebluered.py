"""
You are given a pattern, such as [a b a b]. You are also given a string, example "redblueredblue". 
A few examples:
Pattern: [a b b a] String: catdogdogcat returns 1
Pattern: [a b a b] String: redblueredblue returns 1
Pattern: [a b b a] String: redblueredblue returns 0
http://stackoverflow.com/questions/26702757/check-if-the-given-string-follows-the-given-pattern
"""

def search(pattern, string, matches=None):
    if matches is None:
        matches = {}
    max_match_len = len(string)
    while max_match_len != 0:
        match = string[0:max_match_len]
        head = pattern[0]
        matches_copy = dict(matches)
        if head not in matches_copy:
            matches_copy[head] = match

        if matches_copy[head] == match:
            if len(pattern) > 1:
                tail = pattern[1:]
                remain_str = string[len(match):]
                if len(remain_str) > 0 and search(tail, remain_str, matches_copy):
                    return True
            else:
                #Implicitly checked desired pattern matches
                if len(string[len(match):]) == 0:
                    return True
        max_match_len = -1
    return False

