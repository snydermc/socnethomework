def clist(s):
    """Helper function to convert the string argument into a list."""

    l = []
    while ', ' in s:
        a = s.split(', ', 1)
        b = a[0]
        s = a[1]
        l.append(b)
    if ', ' not in s:
        l.append(s)

    l2 = []
    for i in l:
        i = i.strip(']')
        i = i.strip('[')
        if i[0] == "'":
            a = i.lstrip("'")
            b = a.rstrip("'")
            l2.append(b)
        if i[0] == '"':
            a = i.lstrip('"')
            b = a.rstrip('"')
            l2.append(b)

    return l2
