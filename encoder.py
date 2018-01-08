import morse as morse



def get_letter(letter): 
    letters = {
        'a': morse.letter_a,
        'b': morse.letter_b,
        'c': morse.letter_c,
        'o': morse.letter_o,
        's': morse.letter_s
    }
    
    letters.get(letter, "something missing")()

def encoder():
    my_string = input("Give me a message to translate into morse code: \n")
    for c in my_string:
        if (c) == " " ):
            morse.word_space()
        else:
            get_letter(c)
            morse.letter_space() 

encoder()