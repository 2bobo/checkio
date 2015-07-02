def total_cost(calls):
    data = {}
    r = 0
    for dd in calls:
        s = 1
        dd = dd.split(" ")
        if not dd[0] in data:
            data[dd[0]] = 0
        elif data[dd[0]] > 99:
            s = 2
        data[dd[0]] += int(dd[2]) / 60
        if int(dd[2]) % 60 != 0:
            data[dd[0]] += 1
    for d in data.values():
        if d > 100:
            r += 100
            d = d -100
            r += (d * 2)
        else:
            r += d
    return r


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost((u"2014-01-01 01:12:13 181",
                       u"2014-01-02 20:11:10 600",
                       u"2014-01-03 01:12:13 6009",
                       u"2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost((u"2014-02-05 01:00:00 1",
                       u"2014-02-05 02:00:00 1",
                       u"2014-02-05 03:00:00 1",
                       u"2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost((u"2014-02-05 01:00:00 60",
                       u"2014-02-05 02:00:00 60",
                       u"2014-02-05 03:00:00 60",
                       u"2014-02-05 04:00:00 6000")) == 106, "Precise calls"

