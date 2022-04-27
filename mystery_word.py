#validates guess
def is_valid_guess(guess):
    if len(guess) == 1 & guess.isalpha():
        return True
    else:
        return False

# @see https://stackoverflow.com/a/15195942/4896064


def mask_word(word, guesses):
    state = []
    for i in range(len(word)):
        state.append("_")
    for i in range(len(word)):
        # print(word[i])
        if word[i] in guesses:
            state[i] = word[i]
    return state


def play_game(file):
    with open(file, "r") as f:
        file_string = f.read().upper()
        print(f"Word length is {len(file_string)}.")
        file_string = file_string.lower()
    # above makes uppercase letters for visibility purpose
    # below makes characters of word into list
        word_list = list(file_string)
        # print(word_list)
    chance = 8
    correct_guess = len(word_list)
    guesses = []

    while True:
        print(mask_word(word_list, guesses))
        guess = input("Please guess a letter: ").upper()
        print(guess)
        # add guess to guesses list
        guesses.append(guess)
        if guess in word_list:
            print("You guessed correctly.")
            correct_guess -= 1
            if correct_guess == 0:
                print("Congratulations, you won")
        else:
            if guess in guesses:
                print(f"You already guessed {guess}.")
            chance -= 1
            print("Sorry, try again")
        if chance == 0:
            print("You have run out of guesses, the word is:", file_string)
            break
    # then check guess against word's letters
    # tell user if guess is in word
    # user can then guess again



# if __name__ == "__main__":
play_game("test-word.txt")
