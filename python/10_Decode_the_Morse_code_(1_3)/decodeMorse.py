MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
              '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
              '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
              '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
              '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'}


def reversing_dictionary(my_map):
    return dict((my_map[k], k) for k in my_map)


def decode(code):
    # Decodes only string with one letter written in Morse
    return MORSE_CODE[code.strip()]


def decodeMorse(morse_code):
    # Accept dots, dashes and spaces, return human-readable message
    return ' '.join([''.join([MORSE_CODE[char] for char in word.split()]) for word in morse_code.strip().split('  ')])

