from sha1_functions import * 

# This function first offers a test of the custom SHA-1 implementation with preset examples, 
# then allows hashing of user-inputted texts and repeating the process on demand.
def main():
    do_you_want_to_test = input("Do you want to test my custom SHA-1 hashing function against known SHA-1 hash values for the word : Test, Hello and code (y/n)")
    if do_you_want_to_test == "y":
        test_sha1()
    
    run_sha1_hashing()
    while hash_again():
        run_sha1_hashing()
    print("You quit.")  

# Function to hash a user-provided text using the SHA-1 algorithm.
def run_sha1_hashing():
    text = input("Enter a text to hash with SHA-1: ")
    hash_value = sha1_hash(text)
    print(hash_value)

# Prompts the user to decide whether to perform a hashing operation again.
def hash_again():
    verify_input = ["y", "n"]
    user_input = None
    while user_input not in verify_input:
        user_input = input("Do you want to hash again (y/n)").lower()

    if user_input == "y":
        return True
    else: 
        return False

# Implements the SHA-1 hashing algorithm on the provided text.
def sha1_hash(text):
    # STEP 1: Convert text to ASCII
    ascii_codes = text_to_ascii(text)

    # STEP 2 and 3: Convert ASCII to Binary
    binary_codes = ascii_to_binary(ascii_codes)

    # STEP 4: Join binary codes and add '1'
    joined_binary = join_and_add_un(binary_codes)

    # STEP 5: Padding the message
    padded_binary = padding_message_binary(joined_binary)

    # STEP 6: Get length in binary
    length_binary = length_in_binary(binary_codes)

    # STEP 7: Complete binary length to 64 bits
    length_64_bits = complete_binary_length(length_binary)

    # STEP 8: Add length to message
    message_with_length = add_length_to_message(padded_binary, length_64_bits)

    # STEP 9: Divide into 512-bit blocks
    blocks = divide_into_blocks(message_with_length)

    # STEP 10: Divide each block into 32-bit words
    all_words = [divide_in_words(block) for block in blocks]

    # STEP 11: Extend each block to 80 words
    extended_blocks = [extend_block(words) for words in all_words]

    # STEP 12, 13, 14: Process each block and get the final hash

    return execute_sha1_conversionhexa_join(extended_blocks)

# Tests the custom SHA-1 hashing function against known SHA-1 hash values.
def test_sha1():
    
    # Values taken from internet with true SHA1 algorithm
    test_cases = {
        "Test": "640ab2bae07bedc4c163f679a746f7ab7fb5d1fa",
        "Hello": "f7ff9e8b7bb2e09b70935a5d785e0cc5d9d0abf0",
        "code": "e6fb06210fafc02fd7479ddbed2d042cc3a5155e"
    }

    print("RESULTS -----------------------------------------------------")
    for text, expected_hash in test_cases.items():
        hash_value = sha1_hash(text)

        print(f"Testing '{text}': ", "Success (Find the same with my algorithm)" if hash_value == expected_hash else "Fail (don't find the same)")
    print("-------------------------------------------------------------")

if __name__ == "__main__":
    main()