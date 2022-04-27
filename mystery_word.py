# validates guess
import random


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
    with open('words.txt') as f:
        file_string = f.read().lower()
        file_list = file_string.split()
        random_word = random.choice(file_list)
        print(random_word)
    
        print(f"Word length is {len(random_word)}.")
        file_string = file_string.lower()
    # above makes uppercase letters for visibility purpose
    # below makes characters of word into list
        # word_list = file_string.split()
        # print(word_list)
    chance = 8
    correct_guess = len(random_word)
    guesses = ' '

    while True:
        guess = input("Please guess a letter: ").lower()
        
        # print(guess)
        # add guess to guesses list  
        if guess in guesses:
            print(f"Whoops you already guessed {guess}.")
        elif guess in random_word:
            print(guess, end=" ")
            print()
            print("You guessed correctly.")

            correct_guess -= 1
            guesses += guess
            # guesses.append(guess)
            if correct_guess == 0:
                print("Congratulations, you won, the word is:", random_word)
                break
        elif guess not in random_word:
            if guess in guesses:
                print(f"Whoops you already guessed {guess}.")
            elif guess not in guesses:
                # guesses.append(guess)
                chance -= 1
                print(f"Sorry, try again, you have {chance} chances left.")
            if chance == 0:
                print("You have run out of guesses, the word is:", random_word)
                break
    # then check guess against word's letters
    # tell user if guess is in word
    # user can then guess again


if __name__ == "__main__":
    play_game('words.txt')
