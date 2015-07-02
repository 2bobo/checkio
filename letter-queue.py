def letter_queue(commands):
    queue = []
    for command in commands:
        if "PUSH" in command.split()[0]:
            queue.append(command.split()[1])
        elif "POP" in command.split()[0] and len(queue) != 0:
            del queue[0]
    return "".join(queue)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"

