from tkinter import *

NORMAL_FONT = ("Open Sans", 10)
MORSE_DATA = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..--', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', 
    '(':'-.--.', ')':'-.--.-', '!': '-.-.--', ' ': '/'
}
TEXT_MESSAGE = "Typing your text here."
MORSE_MESSAGE = "Typing morse code using '.' and '-', seperating spaces by '/'"


def encrypt(message):
    result = ""
    try:
        for char in message:
            result += MORSE_DATA[char] + " "
    except KeyError:
        result = "Error in input!\nCannot Translate"
    
    return result

def decrypt(message):
    result = ""
    new_morse_data = {morse: char for char, morse in MORSE_DATA.items()}
    try:
        for code in message.split(" "):
            result += new_morse_data[code] 
    except KeyError:
        result = "Error in input!\nCannot Translate"

    return result

def on_entry_click(_):
    # function that gets called whenever entry is clicked
    if entry.get('1.0', END).strip() == MORSE_MESSAGE or TEXT_MESSAGE:
       entry.delete('1.0', END) # delete all the text in the entry
       entry.insert('1.0', '') # Insert blank for user input
       entry.config(fg = 'black')

def on_focusout(_):
    # called this function when entry click other widget than entry and no text type in
    if entry.get('1.0', END).strip() == '':
        if entry_label.cget("text") == "Text: ":
            entry.insert('1.0', TEXT_MESSAGE)
        elif entry_label.cget("text") == "Morse Code: ":
            entry.insert('1.0', MORSE_MESSAGE)
        entry.config(fg = 'grey')

def add_text(text):
    # Called this function when add encrypt, decrypt result in output box
    output.config(state=NORMAL)
    output.delete('1.0', END)
    output.insert('1.0', text)
    output.config(state=DISABLED)

def swap_text_morse():
    # Called this function to swap between morse code to text and text to morse code
    print(entry_label.cget("text"))
    if entry_label.cget("text") == "Text: ":
        entry_label.config(text="Morse Code: ")
        convert_label.config(text="Text: ")
    elif entry_label.cget("text") == "Morse Code: ":
        entry_label.config(text="Text: ")
        convert_label.config(text="Morse Code: ")

def convert():
    # Called this function when convert button is pushed
    if entry_label.cget("text") == "Text: ":
        result = encrypt(entry.get('1.0', END).strip().upper())
        add_text(result)
    elif entry_label.cget("text") == "Morse Code: ":
        result = decrypt(entry.get('1.0', END).strip())
        add_text(result)


if __name__ == '__main__':
    # Setting window
    window = Tk()
    window.title("Morse code Translator")
    window.config(padx=20, pady=20)

    # Creating the widgets
    title = Label(text="Morse Code Translator", font=("Open Sans", 20, "bold"))
    entry_label = Label(text="Text: ", font=NORMAL_FONT)
    entry = Text(height=6, wrap=WORD, fg='grey', font=NORMAL_FONT)
    entry.insert(END, TEXT_MESSAGE)
    swap_btn = Button(text="Swap", width=20, font=NORMAL_FONT, command=swap_text_morse)
    convert_btn = Button(text="Convert", width=20, font=NORMAL_FONT, command=convert)
    convert_label = Label(text="Morse Code: ", font=NORMAL_FONT)
    output = Text(height=6, font=NORMAL_FONT, bg='#EEEEEE', wrap=WORD, state=DISABLED)

    # Positioning the widgets
    title.grid(row=1, column=1, columnspan=2, pady=10)
    entry_label.grid(row=2, column=1, sticky=W)
    entry.grid(row=3, column=1, columnspan=2, pady=(5,10))
    swap_btn.grid(row=4, column=2)
    convert_btn.grid(row=4, column=1)
    convert_label.grid(row=5, column=1, sticky=W, pady=(10,0))
    output.grid(row=6, column=1, columnspan=2, pady=5)

    # Bind the greyed out function for entry
    entry.bind("<FocusIn>", on_entry_click)
    entry.bind("<FocusOut>", on_focusout)

    window.mainloop()
