import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# Create a placeholder by word and put _
placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

# We create a loop to let the user guess again.
game_over = False
correct_letters = []
lives = 5

stages = [
        """
        --------
        |      |
        |      O
        |     \|/
        |      |
        |     / \
        -
        """,
        """
        --------
        |      |
        |      O
        |     \|/
        |      |
        |     /
        -
        """,
        """
        --------
        |      |
        |      O
        |     \|/
        |      |
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |     \|
        |      |
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |      |
        |      |
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |
        |
        |
        -
        """,
        """
        --------
        |      |
        |
        |
        |
        |
        -
        """
]

while not game_over:
    guess = input("Guess a letter: ").lower()
    # Create a display when player select a letter
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    # Delete lives when the word is not correct
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose")

    if "_" not in display:
        game_over = True
        print("You win")

    # Print the ASCII character to describe the lives :D
    print(stages[lives])