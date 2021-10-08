import tkinter

MORSE_DATA = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..--', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', 
    '-':'-....-', '(':'-.--.', ')':'-.--.-', '!': '-.-.--', ' ': '/'
}


def encrypt(message):
    result = ""
    try:
        for char in message:
            result += MORSE_DATA[char] + " "
    except KeyError:
        result = "\nError in input!\nCannot Translate\n"
    
    return result

def decrypt(message):
    result = ""
    new_morse_data = {morse: char for char, morse in MORSE_DATA.items()}
    try:
        for code in message.split(" "):
            result += new_morse_data[code] 
    except KeyError:
        result = "\nError in input!\nCannot Translate\n"

    return result
            

def main():
    print("""
    |------------------|
    | Morse Translator |
    |------------------|
    """)
    print("Translate from\n(1): Text to Morse Code\n(2): Morse code to text")
    morse_or_text = input("(Please input 1 or 2): ")
    
    if morse_or_text == '1':
        message = input("\nType your message here: ").upper()
        return encrypt(message)
    elif morse_or_text == '2':
        message = input("\nType your morse code here (using '.' and '-', seperating letters by spaces by '/'):\n")
        return decrypt(message)
    else:
        return "\nError!\nPlease type 1 or 2\n"


if __name__ == '__main__':
    print(main())