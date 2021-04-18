#string = "PCPCPPCPCCPCPCPP"
text = input('input string: ')

def hurufBergantian(string):
    count = 0
    char_stored = ''

    for char in string:
        if char == char_stored:
            count += 1
        elif char == 'P':
            char_stored = char
        elif char == 'C':
            char_stored = char

    return count

print('count:', hurufBergantian(text))

