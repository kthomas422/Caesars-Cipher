#-------------------------------------------------------------------------------
# Author:  Kyle Thomas
# System:  Python 3.6 on Linux
# Purpose: This program encryptes and decryptes text using Caesar's Cipher
# Format:  python caesar.py <shift amount> "input file" "output file"
# Note:    The files must be in current working dir and non printable characters
#           will be ignored.
#-------------------------------------------------------------------------------


from sys import platform, argv
from os import getcwd


#Purpose: Performs Caesar's Cipher shifting the letters in the string
#  Input: The text to encrypt (str) and the shift amount (int)
# Output: The encrypted text (str)
def caesar_cipher(string, shift):
    new_string = ""
    
    for i in range(len(string)):
        tmp_char = ord(string[i])  # convert from ascii to decimal
        if (tmp_char > 31) and (tmp_char < 127):  # printable characters
            tmp_char += shift
            if tmp_char > 126:  # loop back to beginning
                tmp_char -= 95
            if tmp_char < 32:  # loop back to end
                tmp_char += 95

        new_string += chr(tmp_char)  # convert back to ascii  

    return new_string


# Purpose: Gets the current working directory as a string
#   Input: The current working dir and platform from the os
#  Output: The current working directory (str)
def get_cwd():
    cwd = getcwd()
    current_os = platform
    if 'win32' in current_os:
        delim = '\\'  # Windows
    else:
        delim = '/'  # Linux and Mac
    cwd += delim
    return cwd


#Purpose: Opens and reads a file
#  Input: The file name
# Output: The contents of the file (str)
def open_file(filename):
    in_file = open(filename, "r")
    source = in_file.read()
    in_file.close()
    return source


# Purpose: Opens and writes to file
#   Input: The string to write and the file name
#  Output: None
def write_to_file(text, filename):
    out_file = open(filename, "w")
    print(text, file=out_file)
    out_file.close()
    return


#Purpose: To pass the arguments along to encrypt text
#  Input: Amount of letters to shift (int), the input filename (str)
#         and output filename (str)
# Output: The string shifted by the amount entered
def main():

    print(" ") #New line for prettier output
    
    cwd = get_cwd()
    
    if len(argv) < 4:  # Makes sure shift and file names were passed
        print("Error not enough arguments.")
        print("Format is: caesar.py <# to shift> <input file> <output file>")
        print("Files must be in the current working directory.")

    else:
        shift = int(argv[1])
        in_file = argv[2]
        out_file = argv[3]

        #Loops shift back into the range of the alphabet if needed       
        if shift > 95:
            while shift > 95:
                shift -= 95 
            print("Shift cannot be greater than 95...\nSetting shift to", shift)
        if shift < -95:
            while shift < -95:
                shift += 95
            print("Shift cannot be less than -95...\nSetting shift to", shift)

        source = open_file(cwd + in_file)  # Gets the input text

        shifted_text = caesar_cipher(source, shift)  # Encrypts the input text

        write_to_file(shifted_text, out_file)

        print("Success!\nResults saved to", out_file)

    return


main()

