# type any text, a poem or anyone
text = "Jesus is the salt of the earth and the light of the world."
# text = input("type any text, a poem or anyone: ")

# ask the user three letters
# TODO: store those letters in a list
# letters = input("type three letters, with spaces: ")
letters = "a i J".lower()
letters_list = letters.split(" ")

# 1 - how many times appears each of those letters
# TODO: pass text and letters to lowercase
text_lower = text.lower()
letters_count = {letra: text_lower.count(letra) for letra in letters_list}

print("Contagem das letras:", letters_count)

# 2 - how many words in total
words = text.split()
print("Número total de palavras:", len(words))

# 3 - first & last letter
first_letter = text[0]
last_letter = text[-1]
print("Primeira letra:", first_letter)
print("Última letra:", last_letter)

# 4 - words in inverted order
words_inverted = words[::-1]
print("Palavras em ordem invertida:", words_inverted)

# 5 - is 'python' there?
is_python = "python" in text_lower
print("A palavra 'python' está no texto?", is_python)