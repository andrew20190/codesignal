def areFollowingPatterns(strings, patterns):
    p2s = dict(zip(patterns, strings))
    pattern_strings = []
    for p in patterns:
        pattern_strings.append(p2s[p])
        
        
    s2p = dict(zip(strings, patterns))
    string_patterns = []
    for s in strings:
        string_patterns.append(s2p[s])
        
    return(pattern_strings == strings and string_patterns == patterns)
