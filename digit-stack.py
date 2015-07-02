def digit_stack(commands):
    stack = []
    sum = 0
    for command in commands:
        if "PUSH" in command:
            num = command.split(" ")
            stack.append(int(num[1]))
        elif "POP" in command and len(stack):
            sum = sum + stack.pop()
        elif "PEEK" in command and len(stack):
            sum = sum + stack[-1]
    return sum

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"

