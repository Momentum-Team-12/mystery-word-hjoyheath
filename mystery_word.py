#validates guess
def is_valid_guess(guess):
    if len(guess) == 1 & guess.isalpha():
        return True
    else:
        return False

# @see https://stackoverflow.com/a/15195942/4896064


def mask_word(state, word, guess):
    state = list(state)
    for i in range(len(word)):
        if word[i] == guess:
            state[i] = guess
    return "".join(state)


def play_game(file):
    with open(file, "r") as f:
        file_string = f.read()
        print(f"Word length is {len(file_string)}.")
        file_string = file_string.lower()
    # above makes uppercase letters for visibility purpose
    # below makes characters of word into list
        word_list = list(file_string)
        print(word_list)

    guesses = []
    # get guess  
    guess = input("Please guess a letter: ").lower()
    print(guess)
    # add guess to guesses list
    guesses.append(guess)
    if guess in word_list:
        print("You guessed correctly")
    else:
        print("Sorry, try again")
    # then check guess against word's letters
    # tell user if guess is in word
    # user can then guess again

    # for guessesTaken in file_string:
    #     if guess == word:
    #         print("You guessed correctly")

# if __name__ == "__main__":
play_game("test-word.txt")
