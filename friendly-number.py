def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):

    ilist = [number]
    format = "%." + str(decimals) + "f"
    h = ""
    if number < 0:
        number = abs(number)
        h = "-"

    if decimals != 0:
        while number >= base:
            ilist.append(float(number) / base),
            number = float(number) / base
    else:
        while number >= base:
            ilist.append((number) / base),
            number = number / base

    rlist = zip(ilist, powers)
    return h + str((format % rlist[-1][0])) + rlist[-1][1] + suffix

if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
    assert friendly_number(102, decimals=2) == '102.00', '102.00'
    assert friendly_number(-150, base=100, powers=["","d","D"]) == "-1d", "-1d"
    assert friendly_number(10**24) == "1Y", "1Y"
    assert friendly_number(42, powers=["u","d"], suffix="-n") == "42u-n", "42u-n"

