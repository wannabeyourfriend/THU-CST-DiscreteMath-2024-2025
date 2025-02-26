def findNomap(A, f):
    for a in A:
        mapped = False
        for m in f:
            if m[1] == a:
                mapped = True
                break
        if mapped == False:
            return a
    return None


def mapping(A, f):
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A
    unmapped_element = findNomap(A, f)
    if unmapped_element is not None:
        for m in f:
            if m[0] == unmapped_element:
                f.remove(m)
        A.remove(unmapped_element)
        return mapping(A, f)
    return A
