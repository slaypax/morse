import morse as morse

def not_found():
    print("not found")

def get_letter(letter): 
    letters = {
        'a': morse.letter_a,
        'b': morse.letter_b,
        'c': morse.letter_c,
        'd': morse.letter_d,
        'e': morse.letter_e,
        'f': morse.letter_f,
        'g': morse.letter_g,
        'h': morse.letter_h,
        'i': morse.letter_i,
        'j': morse.letter_j,
        'k': morse.letter_k,
        'l': morse.letter_l,
        'm': morse.letter_m,
        'n': morse.letter_n,
        'o': morse.letter_o,
        'p': morse.letter_p,
        'q': morse.letter_q,
        'r': morse.letter_r,
        's': morse.letter_s,
        't': morse.letter_t,
        'u': morse.letter_u,
        'v': morse.letter_v,
        'w': morse.letter_w,
        'x': morse.letter_x,
        'y': morse.letter_y,
        'z': morse.letter_z
    }
    
    letters.get(letter, not_found)()

def encoder():
    my_string = input("Give me a message to translate into morse code: ")
    for c in my_string:
        if ((c) == " "):
            morse.word_space()
        else:
            get_letter(c)
            morse.letter_space() 

encoder()