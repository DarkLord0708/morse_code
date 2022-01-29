MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

task = int(input("Enter 1 to encode and 2 to decode:\n"))

if task == 1:
    i = input("Enter a word or sentence to convert to morse:\n")
    original = i
    converted = ""

    for word in i:
        for letter in word:
            if letter.isalpha():
                converted += MORSE_CODE_DICT[letter.upper()] + " "
            elif letter.isnumeric():
                converted += MORSE_CODE_DICT[letter] + " "
            elif letter == " ":
                converted += " / "
            elif letter not in MORSE_CODE_DICT.keys():
                print(f"The symbol {letter} is not in the database. Sorry!")
            else:
                converted += MORSE_CODE_DICT[letter] + " "

    print(original)
    print(converted)
elif task == 2:
    i = input("Enter a word or sentence to decode:\n")
    original = i
    decoded = ""

    for word in i.split("/"):
        for letter in word.split(" "):
            if letter == " " or letter == '':
                decoded += " "
            else:
                decoded += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(letter)]
        decoded += " "

    print(original)
    print(decoded)

# t = ".- .-.. .-.. / .... ..- -- .- -. / -... . .. -. --. ... / .- .-. . / -... --- .-. -. / ..-. .-. . . / .- -. -.. / . --.- ..- .- .-.. / .. -. / -.. .. --. -. .. - -.-- / .- -. -.. / .-. .. --. .... - ... .-.-.- / - .... . -.-- / .- .-. . / . -. -.. --- .-- . -.. / .-- .. - .... / .-. . .- ... --- -. / .- -. -.. / -.-. --- -. ... -.-. .. . -. -.-. . / .- -. -.. / ... .... --- ..- .-.. -.. / .- -.-. - / - --- .-- .- .-. -.. ... / --- -. . / .- -. --- - .... . .-. / .. -. / .- / ... .--. .. .-. .. - / --- ..-. / -... .-. --- - .... . .-. .... --- --- -.. .-.-.-"