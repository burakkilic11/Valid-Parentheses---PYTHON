def isValid(s: str):
    stack = []
    dict = { '(':')' , '{':'}' , '[':']' }

    for char in s:
        if char in dict:
            stack.append(char)
        elif not stack or dict[stack.pop()] != char:
            return False

    return len(stack) == 0

def main():
    inp = input("Type the string here: ")
    print(isValid(inp))

if __name__ == '__main__':
    main()