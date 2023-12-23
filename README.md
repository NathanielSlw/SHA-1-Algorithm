# SHA-1-Algorithm
This python code can be used to hash a text using the SHA-1 hashing algorithm
=> 40 characters at the end regardless of the input

<img width="1094" alt="image" src="https://github.com/NathanielSlw/SHA-1-Algorithm/assets/130759155/57c57bb7-13ea-4463-befb-6188761fde50">

Here are the different steps for the SHA-1 algorithm: 

Source for the different steps : https://www.youtube.com/watch?v=kmHojGMUn0Q 

### 1. Takes a text as input and divides it into an array of ASCII codes.

ex= "Test" => ["T", "e", "s", "t"] => **[84, 101, 115, 116]**


### 2. Convert ASCII codes into binary codes

ex: [84, 101, 115, 116] => **[1010100, 1100101, 111001, 1110100]**

### 3. Add zeros to the beginning of each until they are 8 bits long.

=> ex: [**0**1010100, **0**1100101, **0**1110011, **0**1110100]

### 4. Join and add a 1

=> 01010100011001010111001101110100**1**

### 5. Fill the binary message with zeros until its length is 512 mod 448 

010101000110010101110011011101001**0000000000000000000…0000**

### 6. Take the array of 8-bit binary ASCII codes from step 3 and obtain its length in binary form

eg: (length(array))*8 = 32 => **100000** 

### 7. Fill in with zeros at the beginning until there are 64 characters.

ex : **000000000000**..100000

### 8. Add to your binary message created earlier in step 5.

=> 0101010001100101011100110111010010000000000000000000…0000**000000000000..100000**

### 9. Break the message down into an array of 512-character "chunks".

[0101010001100101011100110111010010000000000000000000…0000000000000000..100000]

### 10. Decompose each "chunk" into a "word" sub-array of sixteen 32-bit arrays.

[ [ 01010100011001010111001101110100,10000000000000000000000000000000,…0000000000000000..100000] ]

### 11. Loop each array of sixteen 32-bit "words" and expand each array to 80 "words" using "bit" operations.

=> Each block of 16 32-bit words must be extended to 80 32-bit words. This extension is achieved using bit operations. For each word from the 17th to the 80th, the corresponding word is calculated by applying a bit-by-bit XOR between four specific words in the array (the words at position (i-3, i-8, i-14, i-16)

### 12. Loop over each part: binary operations and variable reallocation 

This stage involves complex processing in which five temporary variables (a, b, c, d, e) are used, as well as a series of defined functions and constants.

Here is an outline of how to implement this step in Python:

- **Variable initialisation**: Initial hash values (h0, h1, h2, h3, h4) are defined. These values will be updated with each block processed.

- **Definition of functions and constants** : Four functions are used to process each block: binary_pad, binary_addition, left_rotate, and truncate_front. In addition, a series of constants (K) is defined for every 20 words.

- **Processing each block**: For each block of 80 words, the temporary variables (a, b, c, d, e) are initialised with the current hash values. Then, for each word in the block, various operations are performed and the temporary variables are updated.

### 13. Converting each of the 5 resulting variables to hexadecimal (h0, h1, h2, h3, h4, h5)

### 14. Gather the 5 values (h0, h1, h2, ..) and return them (this is your hash value).
