def tasu(data, total=0):
    if len(data) == 0:
        return total
    return tasu(data, total + data.pop())

def checkio(data):
    return tasu(data)
