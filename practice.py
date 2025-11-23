
text = "The quick brown fox jumps over the lazy dog!"

# Write a list comprehension to tokenize the text and remove punctuation
tokens = [word.strip(".,!?;:").lower() for word in text.split()]

# Expected output: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
print(tokens)

def tokenize(string: str) -> list:
    cleanstring = "".join([char for char in string if char.isalnum() or char.isspace()])
    return sorted(set(cleanstring.lower().split()))

print(tokenize(text))


word_frequencies = {token: tokens.count(token) for token in enumerate(tokenize(text))}

# Expected output example: {'the': 2, 'quick': 1, ...}
print(word_frequencies)

# -----------------------------------------------
token_to_id = {token: integer for integer, token in enumerate(tokenize(text))}

# Expected output: {'dog': 0, 'quick': 1, 'fox': 2, 'the': 3, 'over': 4, 'lazy': 5, 'brown': 6, 'jumps': 7}
print(token_to_id)
# -----------------------------------------------

# Task 6: Define a dictionary that reverses the mapping in `token2int`
#
# Your code here:
# -----------------------------------------------
id_to_token = {integer: token for token, integer in token_to_id.items()}
print(id_to_token)
