import unicodedata

def remove_diacritical_chars(text):
    """
    Removes diacritical characters from a given text.
    """
    return ''.join(c for c in unicodedata.normalize('NFD', text)
                  if unicodedata.category(c) != 'Mn')

# read text file
with open('corrupted.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# remove diacritical characters from text
text_without_diacritical_chars = remove_diacritical_chars(text)

# write text without diacritical characters to output file
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(text_without_diacritical_chars)
