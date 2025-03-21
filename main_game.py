import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# Create a placeholder by word and put _
placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter: ").lower()
print(guess)

# Create a display when player select a letter
display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)