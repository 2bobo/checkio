FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):
    string_number = ""

    if number / 100 != 0:
        string_number = string_number + FIRST_TEN[(number / 100) - 1]
        string_number = string_number + " " + HUNDRED
        if number % 100 != 0:
            string_number = string_number + " "
        number = number % 100

    if 20 > number > 9  and number != 0:
        string_number = string_number + SECOND_TEN[number - 10]
        number = number - number
        return string_number

    if number >= 20 :
        string_number = string_number + OTHER_TENS[(number / 10) - 2]
        if number % 10 != 0:
             string_number = string_number + " "
        number = number % 10

    if number != 0:
        string_number = string_number + FIRST_TEN[number - 1]

    return string_number

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"

