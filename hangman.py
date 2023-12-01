import random
"""
    The code is a Python implementation of the Hangman game where the player has to guess a randomly
    chosen word.
    :return: The function `choose_word()` returns a randomly chosen word from the `word_list`.
"""

def choose_word():
    word_list = ["python", "java", "ruby", "javascript", "swift", "html", "css", "php","cat", "dog", "rabbit","parrot", "goldfish", "ferret", "turtle"]
    #word_list =["dog"]   
    return random.choice(word_list)

def play_hangman():
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = len(word_letters)+4

    while tries > 0 and word_letters:
        print("\nYou have {} tries left and you've used these letters: ".format(tries))
        print(' '.join(guessed_letters))

        word_list = [letter if letter in guessed_letters else '_' for letter in word]
        print('Word: ', ' '.join(word_list))

        guess = input("Guess a letter: ").lower()
        if not (guess in word_letters):
            tries-=1
        if len(guess) != 1:
            print("Please enter a single letter.")
            continue
        elif guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
       
              

    if tries == 0:
        print("\nSorry, you lost. The word was '{}'.".format(word))
    else:
        print("\nCongratulations! You guessed the word '{}'!".format(word))

if __name__ == '__main__':
    print("Welcome to Hangman!")
    play_hangman()
