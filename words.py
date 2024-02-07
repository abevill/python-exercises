def print_upper_words(words, must_start_with=None):
 
    for word in words:
        if must_start_with is None or any(word.lower().startswith(letter.lower()) for letter in must_start_with):
            print(word.upper())



