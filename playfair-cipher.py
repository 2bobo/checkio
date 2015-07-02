def encode(message, key):
    keymap = create_keymap(key)
    message = list(check_keystring(message))
    msg_list = []
    result = ""

    for i in range(0, len(message), 2):
        if i+1 < len(message):
            if (message[i] == message[i+1]) and not(message[i] == "x" and message[i+1] == "x"):
                message.insert(i+1, "x")
            elif message[i] == "x" and message[i+1] == "x":
                message.insert(i+1, "z")
    if (len(message) % 2) != 0:
        if message[-1] == "z":
            message.append("x")
        else:
            message.append("z")
    while len(message) !=0:
        msg_list.append(message[0:2])
        del message[0:2]

    for msg in msg_list:
        r = []
        for w in msg:
            for y, row in enumerate(keymap):
                for x, word in enumerate(row):
                    if w in word:
                        r.append([y, x])
        if r[0][1] == r[1][1]:
            r[0][0] += 1
            r[1][0] += 1
            if r[0][0] == 6:
                r[0][0] = 0
            if r[1][0] == 6:
                r[1][0] = 0
        elif r[0][0] == r[1][0]:
            r[0][1] += 1
            r[1][1] += 1
            if r[0][1] == 6:
                r[0][1] = 0
            if r[1][1] == 6:
                r[1][1] = 0
        else:
            p = r[0][1]
            q = r[1][1]
            r[1][1] = p
            r[0][1] = q
        result = result + keymap[r[0][0]][r[0][1]] + keymap[r[1][0]][r[1][1]]
    return result

#    return "do2y7mt22kry94y2y2"
def decode(secret_message, key):
    keymap = create_keymap(key)
    list_secret_message = list(secret_message)
    msg_list = []
    result = ""
    smessage = []
    rmessage = ""

    while len(list_secret_message) !=0:
        msg_list.append(list_secret_message[0:2])
        del list_secret_message[0:2]

    for msg in msg_list:
        r = []
        for w in msg:
            for y, row in enumerate(keymap):
                for x, word in enumerate(row):
                    if w in word:
                        r.append([y, x])
        if r[0][1] == r[1][1]:
            r[0][0] -= 1
            r[1][0] -= 1
            if r[0][0] == 6:
                r[0][0] = 0
            if r[1][0] == 6:
                r[1][0] = 0
        elif r[0][0] == r[1][0]:
            r[0][1] -= 1
            r[1][1] -= 1
            if r[0][1] == 6:
                r[0][1] = 0
            if r[1][1] == 6:
                r[1][1] = 0
        else:
            p = r[0][1]
            q = r[1][1]
            r[1][1] = p
            r[0][1] = q
        rmessage = rmessage + keymap[r[0][0]][r[0][1]] + keymap[r[1][0]][r[1][1]]
    return rmessage

def create_keymap(key):
    key_fill = "abcdefghijklmnopqrstuvwxyz0123456789"
    keymap = []
    key = check_keystring(key) + key_fill
    for w in key:
        if not w in keymap:
            keymap.append(w)
    return [keymap[x:x + 6] for x in xrange(0, 36, 6)]

def check_keystring(words):
    numstring = []
    for word in words.lower():
        if word.isalnum():
            numstring.append(word)
    return "".join(numstring)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert encode("Fizz Buzz is x89 XX.", "checkio101") == 'do2y7mt22kry94y2y2', "Encode fizz buzz"
    assert decode("do2y7mt22kry94y2y2", "checkio101") == 'fizxzbuzzisx89xzxz', "Decode fizz buzz"
    assert encode("How are you?", "hello") == 'ea2imb1ht0', "Encode How are you"
    assert decode("ea2imb1ht0", "hello") == 'howareyouz', "Decode How are you"
    assert encode("My name is Alex!!!", "alexander") == 'i1dlkxjqlexn', "Encode Alex"
    assert decode("i1dlkxjqlexn", "alexander") == 'mynameisalex', "Decode Alex"
    assert encode("Who are you?", "human") == 'rnvftc1jd5', "Encode WHo"
    assert decode("rnvftc1jd5", "human") == 'whoareyouz', "Decode Who"
    assert encode("ATTACK AT DAWN", "general") == 'ewwektewhnua', "Encode attack"
    assert decode("ewwektewhnua", "general") == 'attackatdawn', "Decode attack"

