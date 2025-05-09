#Day 8 - caeser cypher/ decypher


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
max_letter_indx = int(len(alphabet) - 1)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
def set_direction():
    global direction
    direction = input("Would you like to continue? If you would like to - type 'encode' to encrypt, type 'decode' to decrypt, if you wouldn't like to, simply type 'no':\n").lower()
text = input("Type your message:\n").lower()
def set_text():
    global text
    text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def set_shift():
    global shift
    shift = int(input("Type the shift number:\n"))

coded_msg = ""


def set_new_inp():
    global coded_msg
    set_direction()
    set_text()
    set_shift()
    coded_msg = ''



def encrypt(to_encode, shift_amount):
    global coded_msg
    # text_list = [lttr for lttr in to_encode]
    for idx, lttr in enumerate(to_encode): #idx is an index of the element in the list of input text
        if lttr == " ":
            coded_msg += " "
        else:
            alph_index = alphabet.index(lttr) # index of the letter in alphabet list
            new_index = alph_index + shift_amount
            if new_index <= max_letter_indx:
                coded_msg += alphabet[new_index]
            else:
                coded_msg += alphabet[new_index - max_letter_indx - 1] #beacuse the list indx starts from 0 and not 1


    print(coded_msg)
    set_new_inp()

def decrypt(to_decode, shift_amount):
    global coded_msg
    # text_list = [lttr for lttr in to_decode]
    for idx, lttr in enumerate(to_decode):
        if lttr == " ":
            coded_msg += " "
        else:
            alph_index = alphabet.index(lttr)  # index of the letter in alphabet list
            new_index = alph_index - shift_amount
            coded_msg += alphabet[new_index]
    print(coded_msg)
    set_new_inp()


if direction == "no":
    print("Okay, see you soon")
while direction != "no":
    if direction != "encode" and direction != "decode":
        print("Oops, you must have spelled it wrong")
        set_direction()
    if direction == "encode":
        encrypt(text, shift)
    if direction == "decode":
        decrypt(text,shift)


