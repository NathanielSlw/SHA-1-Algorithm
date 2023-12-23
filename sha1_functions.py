
# STEP 1: Convert the text given as input and divide it into an ascii code array
def text_to_ascii(text):
    return [ord(caractere) for caractere in text]

# STEP 2 and 3: Convert ASCII codes into binary codes
def ascii_to_binary(codes_ascii):
    binaire = []
    for code in codes_ascii:
        # Convert to binary and remove the '0b' prefix
        binaire_code = bin(code)[2:]
        # STEP 3 : Ensure that the binary length is 8 bits
        binaire_code = binaire_code.zfill(8)
        binaire.append(binaire_code)
    return binaire

# STEP 4: Join the binary in a string and add 1
def join_and_add_un(codes_binaires):
    # Join all the items in the list into a single string
    chaine_binaire = ''.join(codes_binaires)
    # Add '1' at the end
    chaine_binaire += '1'
    return chaine_binaire

# Step 5: Fill the binary message with zeros until its length is 512 mod 448
def padding_message_binary(binary_message):
    while len(binary_message) % 512 != 448:
        binary_message += '0'

    return binary_message

# STEP 6: Take the table of 8-bit binary ASCII codes from step 3 and obtain its length in binary form
def length_in_binary(binary_codes):
    # Calculate the total length in bits (each binary input represents 8 bits)
    longueur_bits = len(binary_codes) * 8

    # Convert this length into binary
    longueur_binaire = bin(longueur_bits)[2:]
    
    return longueur_binaire

# STEP 7: Add zeros at the beginning until there are 64 characters.
def complete_binary_length(binary_length):
    return binary_length.zfill(64)

# STEP 8: Add the result of step 7 to the binary message created in step 5.
def add_length_to_message(binary_message, length_binary_64_bits):
    return binary_message + length_binary_64_bits

# STEP 9: Break the message down into blocks of size 512 bits.
def divide_into_blocks(message, block_size=512):
    return [message[i:i + block_size] for i in range(0, len(message), block_size)]

# STEP 10: Divide each block into 32-bit words
def divide_in_words(bloc, word_size=32):
    return [bloc[i:i + word_size] for i in range(0, len(bloc), word_size)]

# STEP 11: Loop each array of sixteen 32-bit "words" and extend each array to 80 "words" using "bit" operations.
def extend_block(words):
    while len(words) < 80:
        # Take the words at position i-3, i-8, i-14, and i-16
        i = len(words)
        mot_a = int(words[i - 3], 2)
        mot_b = int(words[i - 8], 2)
        mot_c = int(words[i - 14], 2)
        mot_d = int(words[i - 16], 2)

        # Apply XOR between these words
        nouveau_mot = mot_a ^ mot_b ^ mot_c ^ mot_d

        # Rotate left 1 bit
        nouveau_mot = ((nouveau_mot << 1) | (nouveau_mot >> 31)) & 0xFFFFFFFF

        # Add the new word to the board
        words.append(f'{nouveau_mot:032b}')

    return words

# Useful functions for step 12 ---------------------------------------

# Adds zeros to the left of a binary string so that it reaches a specific length.
def binary_pad(bin_str, size=32):
    return bin_str.zfill(size)

# Performs a binary addition and returns the result as a binary string.
def binary_addition(a, b):
    max_length = max(len(a), len(b))
    sum = bin(int(a, 2) + int(b, 2))[2:]  # Remove '0b' prefix
    return sum.zfill(max_length)

# Performs a left rotation (circular shift to the left) on a binary string.
def left_rotate(bin_str, amount):
    return bin_str[amount:] + bin_str[:amount]

# Truncates the binary string to a specific length, removing the left-hand bits if necessary.
def truncate_front(bin_str, size=32):
    if len(bin_str) > size:
        return bin_str[-size:]
    return bin_str.zfill(size)

#  -----------------------------------------------------------------------------------------------

#   STEP 12: Loop over each part: binary operations and variable reassignment 
# + STEP 13: Convert each of the 5 resulting variables to hexadecimal (h0, h1, h2, h3, h4, h5)
# + STEP 14: Gather the 5 values (h0, h1, h2, ..) and return them (this is your hash value)
def execute_sha1_conversionhexa_join(words):
    

    # Initial Values SHA-1
    h0 = '01100111010001010010001100000001'
    h1 = '11101111110011011010101110001001'
    h2 = '10011000101110101101110011111110'
    h3 = '00010000001100100101010001110110'
    h4 = '11000011110100101110000111110000'

    # Constants for SHA-1
    K = [
        '01011010100000100111100110011001',  # (0 <= j <= 19)
        '01101110110110011110101110100001',  # (20 <= j <= 39)
        '10001111000110111011110011011100',  # (40 <= j <= 59)
        '11001010011000101100000111010110'   # (60 <= j <= 79)
    ]

    for chunk in words: 
        a, b, c, d, e = h0, h1, h2, h3, h4

        for j in range(80):
            if j < 20:
                f = binary_pad(bin((int(b, 2) & int(c, 2)) | (~int(b, 2) & 0xFFFFFFFF) & int(d, 2))[2:])
            elif j < 40:
                f = binary_pad(bin(int(b, 2) ^ int(c, 2) ^ int(d, 2))[2:])
            elif j < 60:
                f = binary_pad(bin(int(b, 2) & int(c, 2) | int(b, 2) & int(d, 2) | int(c, 2) & int(d, 2))[2:])
            else:
                f = binary_pad(bin(int(b, 2) ^ int(c, 2) ^ int(d, 2))[2:])

            temp = binary_addition(left_rotate(a, 5), f)
            temp = binary_addition(temp, e)
            temp = binary_addition(temp, K[j // 20])
            temp = binary_addition(temp, chunk[j])
            temp = truncate_front(temp, 32)

            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        h0 = truncate_front(binary_addition(h0, a), 32)
        h1 = truncate_front(binary_addition(h1, b), 32)
        h2 = truncate_front(binary_addition(h2, c), 32)
        h3 = truncate_front(binary_addition(h3, d), 32)
        h4 = truncate_front(binary_addition(h4, e), 32)

    # step 13 : Convert in hexa decimal
    result = ''.join([f'{int(binary_value, 2):08x}' for binary_value in [h0, h1, h2, h3, h4]])
    # step 14 : Gather the 5 values (h0, h1, h2, ..) and return them (this is your hash value).
    return ''.join(result)
     





