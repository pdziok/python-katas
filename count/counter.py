def count_vowels(input_text):
    counter = 0
    for i in input_text:
        if i in ['a', 'e', 'i', 'o', 'u', 'y']:
            counter += 1
    return counter
