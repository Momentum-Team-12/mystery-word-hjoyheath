def play_game(file):
    with open(file, "r") as f:
        file_string = f.read()
        # file_string = file_string.split()
        print(f"Word length is {len(file_string)}.")
        file_string = file_string.split()
    guesses = []
    # get guess  
    guess = input("Please guess a letter ")
    print(guess)
    # add guess to guesses list
    guesses.append(guess)
    print(guesses)
    # then check guess against word's letters
    for letter in file_string:
        if letter ==
    # tell user if guess is in word
    # user can then guess again

    # for guessesTaken in file_string:
    #     if guess == word:
    #         print("You guessed correctly")

        
    

# if __name__ == "__main__":
play_game("test-word.txt")
