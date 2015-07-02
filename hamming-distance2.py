def checkio(n, m):
    n = format(n, "b")
    m = format(m, "b")
    n_len = len(n)
    m_len = len(m)
    if n_len > m_len:
        cnt = n_len
    else:
        cnt = m_len

    r = []
    for a, b in zip(list(n.zfill(cnt)), list(m.zfill(cnt))):
        if int(a) == int(b):
            r.append(0)
        else:
            r.append(1)
    return sum(r)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
    assert checkio(1, 999999) == 11, "Force example"

