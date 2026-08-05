# Manual string length
def str_len(value):
    count = 0
    for character in value:
        count += 1
    return count

print(str_len("Maxwell"))

# Reverse string
def reverse_string(value):
    reverse_value = ""
    for ch in value:
        reverse_value = ch + reverse_value
    return reverse_value

print(reverse_string("maxwell"))

# Censor Words
def censor_words(text, banned_word):
    return text.replace(banned_word, "***")

print(censor_words("This code is bad bad", "bad"))