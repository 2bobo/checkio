def convert(numerator, denominator):
    '''
    print "&&&&"
    print numerator/denominator
    print numerator%denominator
    print divmod(float(numerator), denominator)
    print "&&&&"
    '''
    a, b = divmod(float(numerator), denominator)
    c = 0
    q = [0]
    r = [0]
    q[0],r[0] = numerator/denominator, float(numerator)%denominator
    while 1:
        a = int((r[c]*10) / denominator)
        b = (float(r[c])*10) % denominator
        q.append(a)
        r.append(b)
        c += 1
        if b in r:
            break
    q_str = map(str, q)
    r_str = map(str, r)
    nj = q_str[1:c-1]
    j = q_str[c:]
    print "----"
    print q_str
    print r_str
    print "----"
    if c == denominator-1:
        print q_str[0] + "." + "".join(q_str[1:c-1])
        return q_str[0] + "." + "".join(q_str[1:c-1])
    else:
        if len(q[1:c-1]) == 0:
            print q_str[0] + ".(" + "".join(q_str[c:]) + ")"
            return q_str[0] + ".(" + "".join(q_str[c:]) + ")"
        else:
            print q_str[0] + "." + "".join(q_str[1:c-1]) + "(" + "".join(q_str[c:]) + ")"
            return q_str[0] + "." + "".join(q_str[1:c-1]) + "(" + "".join(q_str[c:]) + ")"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert(1, 3) == "0.(3)", "1/3 Classic"
    assert convert(5, 3) == "1.(6)", "5/3 The same, but bigger"
    assert convert(3, 8) == "0.375", "3/8 without repeating part"
    assert convert(7, 11) == "0.(63)", "7/11 prime/prime"
    assert convert(29, 12) == "2.41(6)", "29/12 not and repeating part"
    assert convert(11, 7) == "1.(571428)", "11/7 six digits"
    assert convert(0, 117) == "0.", "Zero"

