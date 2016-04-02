"""
You are given a pattern, such as [a b a b]. You are also given a string, example "redblueredblue". 
A few examples:
Pattern: [a b b a] String: catdogdogcat returns 1
Pattern: [a b a b] String: redblueredblue returns 1
Pattern: [a b b a] String: redblueredblue returns 0
http://stackoverflow.com/questions/26702757/check-if-the-given-string-follows-the-given-pattern
"""

def search(pattern, string, matches=None):
    if not matches:
        matches = dict()

    if not pattern and not string:
        return True

    if pattern:
        head = pattern[0]
    else:
        return False

    expect = matches.get(head)
    if expect:
        if string.startswith(expect):
            return search(pattern[1:], string[len(expect):], matches)
        else:
            return False
    else:
        for matchLen in range(len(string), 0, -1):  # loop from len(string) to 1
            match = string[:matchLen]
            matches[head] = match
            if search(pattern[1:], string[len(match):], matches):
                return True
            else:
                del matches[head]
        else:
            return False

print search("abba", "catdogdogcat")
