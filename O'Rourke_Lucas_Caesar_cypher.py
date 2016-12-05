'''
Lucas O'Rourke   
Decodes a string with that is Ceasar cypher encrypted
'''

def main():
    input_str = input("Please enter a string to decode: ")
    shift_by = int(input("Please enter a shift: "))
    decoded_str = ceasar(input_str, shift_by)
    print(decoded_str)

def ceasar(string, shift):
    new_str = ""
    for letter in string:
        new_char = ord(letter) + shift
        if 65 <= ord(letter) <= 90:
            ord_char = (new_char - 65)%26
            new_str += str(chr(ord_char + 65))
        elif 97 <= ord(letter) <= 122:
            ord_char = (new_char - 97)%26
            new_str += str(chr(ord_char + 97))
        elif letter == " ":
            new_str += " "
    return new_str

main()       
        
