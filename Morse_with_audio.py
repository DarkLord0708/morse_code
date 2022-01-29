import pygame
from pygame import mixer



MORSE_CODE_SOUNDS_DICT = { 'A' : 'A_morse_code.ogg.mp3' ,  'B' : 'B_morse_code.ogg.mp3' ,  'C' : 'C_morse_code.ogg.mp3' ,
 'D' : 'D_morse_code.ogg.mp3' ,  'E' : 'E_morse_code.ogg.mp3' ,  'F' : 'F_morse_code.ogg.mp3' ,  'G' : 'G_morse_code.ogg.mp3' ,
 'H' : 'H_morse_code.ogg.mp3' ,  'I' : 'I_morse_code.ogg.mp3' ,  'J' : 'J_morse_code.ogg.mp3' ,  'K' : 'K_morse_code.ogg.mp3' ,
 'L' : 'L_morse_code.ogg.mp3' ,  'M' : 'M_morse_code.ogg.mp3' ,  'N' : 'N_morse_code.ogg.mp3' ,  'O' : 'O_morse_code.ogg.mp3' ,
 'P' : 'P_morse_code.ogg.mp3' ,  'Q' : 'Q_morse_code.ogg.mp3' ,  'R' : 'R_morse_code.ogg.mp3' ,  'S' : 'S_morse_code.ogg.mp3' ,
 'T' : 'T_morse_code.ogg.mp3' ,  'U' : 'U_morse_code.ogg.mp3' ,  'V' : 'V_morse_code.ogg.mp3' ,  'W' : 'W_morse_code.ogg.mp3' ,
 'X' : 'X_morse_code.ogg.mp3' ,  'Y' : 'Y_morse_code.ogg.mp3' ,  'Z' : 'Z_morse_code.ogg.mp3' ,  '0' : '0_number_morse_code.ogg.mp3' ,
 '1' : '1_number_morse_code.ogg.mp3' ,  '2' : '2_number_morse_code.ogg.mp3' ,  '3' : '3_number_morse_code.ogg.mp3' ,  '4' : '4_number_morse_code.ogg.mp3' ,
 '5' : '5_number_morse_code.ogg.mp3' ,  '6' : '6_number_morse_code.ogg.mp3' ,  '7' : '7_number_morse_code.ogg.mp3' ,  '8' : '8_number_morse_code.ogg.mp3' ,
 '9' : '9_number_morse_code.ogg.mp3' ,   ',' : 'Morse_Code_-_Comma.ogg.mp3' ,  '.' : 'Morse_Code_-_Period.ogg.mp3' ,  '?' : 'Morse_Code_-_Question_Mark.ogg.mp3' ,
 '/' : 'Morse_Code_-_Slash.ogg.mp3' ,  '-' : '-_morse_code.ogg.mp3' ,  '(' : 'Morse_Code_-_Parenthesis_(Open).ogg.mp3' ,
 ')' : 'Morse_Code_-_Parenthesis_(Close).ogg.mp3' , "'" : 'Morse_Code_-_Apostrope.ogg.mp3' ,  '!' : 'Morse_Code_-_Exclamation_Point.ogg.mp3' }


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
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', "'":".----.", '!':'-.-.--'}

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
            converted += " // "
        elif letter not in MORSE_CODE_DICT.keys():
            print(f"The symbol {letter} is not in the database. Sorry!")
        else:
            converted += MORSE_CODE_DICT[letter] + " "

print(original)
mixer.init()
# mixer.music.load("music file here")
# mixer.music.play()
for word in original:
    for letter in word:
        if letter.isalpha():
            print(MORSE_CODE_DICT[letter.upper()], end=" ")
            mixer.music.load(r"C:\Users\shiva\OneDrive\Desktop\Coding\Codes and stuff\all audio files\\" + MORSE_CODE_SOUNDS_DICT[letter.upper()])
            mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        elif letter.isnumeric():
            print(MORSE_CODE_DICT[letter], end=" ")
            mixer.music.load(r"C:\Users\shiva\OneDrive\Desktop\Coding\Codes and stuff\all audio files\\" + MORSE_CODE_SOUNDS_DICT[letter])
            mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        elif letter == " ":
            print()
        elif letter not in MORSE_CODE_SOUNDS_DICT.keys():
            print(f"The symbol {letter} is not in the database. Sorry!")
        else:
            print(MORSE_CODE_DICT[letter], end=" ")
            mixer.music.load(r"C:\Users\shiva\OneDrive\Desktop\Coding\Codes and stuff\all audio files\\" + MORSE_CODE_SOUNDS_DICT[letter])
            mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
print()
print(converted)