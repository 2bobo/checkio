def clock_angle(time):
    ltime = time.split(":")

    if int(ltime[0]) >= 12:
        hh = ((int(ltime[0]) - 12) * 60) + int(ltime[1])
    else:
        hh = int(ltime[0]) * 60 + int(ltime[1])
    h_angle = 0.5 * hh
    m_angle = 6.0 * int(ltime[1])

    if abs(h_angle) >= abs(m_angle):
        angle = abs(h_angle - m_angle)
    else:
        angle = abs(m_angle - h_angle)

    if angle > 180:
        angle = 360 - angle

    if angle == int(angle):
        return int(angle)
    else:
        return angle

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"


