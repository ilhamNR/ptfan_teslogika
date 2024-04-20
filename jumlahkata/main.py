import re

def find_words_without_special_characters(sentence):
    # Split the sentence into words
    words = sentence.split()
    words_without_special_chars = []

    # Iterate through each word in the sentence
    for word in words:
        # Use regular expression to check if the word only consists of allowed characters
        if re.match(r'^[a-zA-Z0-9,.?!=]+$', word):
            words_without_special_chars.append(word)

    return words_without_special_chars

# Take input from the user
sentence = input()

# Call the find_words_without_special_characters function with user input
words_without_special_chars = find_words_without_special_characters(sentence)
print(len(words_without_special_chars))
