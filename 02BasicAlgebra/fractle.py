# from turtle import *


# def draw_branch(branch_length, angle):
#     if branch_length > 5:
#         forward(branch_length)
#         right(angle)
#         draw_branch(branch_length - 15, angle)
#         left(2 * angle)
#         draw_branch(branch_length - 15, angle)
#         right(angle)
#         backward(branch_length)

# def draw_tree(trunk_length, angle):
#     speed("fastest")
#     left(90)
#     up()
#     backward(trunk_length)
#     down()
#     draw_branch(trunk_length, angle)
#     done()

# draw_tree(100, 20)

def encode(text):
    """
    Returns the run-length encoded version of the text
    (numbers after symbols, length = 1 is skipped)
    """
    textLength = len(text)
    result = ""
    previousChar = ""
    continuityCounter = 1
    for i, char in enumerate(text):
        if i == (textLength - 1):
            if char == previousChar:
                continuityCounter += 1
            else:
                result += get_char_num(previousChar, continuityCounter)
                previousChar = char
                continuityCounter = 1
            result += get_char_num(previousChar, continuityCounter)
        elif char == previousChar:
            continuityCounter += 1
        else:
            result += get_char_num(previousChar, continuityCounter)
            previousChar = char
            continuityCounter = 1
    return result

def get_char_num(char, counter):
    return char + (str(counter) if counter != 1 else "")
    

def decode(text):
    """
    Decodes the text using run-length encoding
    """
    lastIndex = len(text)
    result = ""
    i = 0
    while i < len(text):
        char = text[i]
        if i == lastIndex - 1:
            result += char
            break        
        nextChar = text[i + 1]
        if nextChar.isdigit():
            result += char * int(nextChar)
            i += 1
        else:
            result += char
        i += 1    
    return result

# Tests
# Test that the functions work on their own
assert encode("AABCCCDEEEE") == "A2BC3DE4"
assert decode("A2BC3DE4") == "AABCCCDEEEE"

# Test that the functions really invert each other
assert decode(encode("AABCCCDEEEE")) == "AABCCCDEEEE"
assert encode(decode("A2BC3DE4")) == "A2BC3DE"