import random

words = ["python", "cpu", "java", "computer", "college", "books", "laptop"]

play_again = "yes"
while play_again == "yes":
    word = random.choice(words)

    guessed_letters = []
    max_attempts = 8
    wrong_guesses = 0

    print("HANGMAN GAME")
    while wrong_guesses < max_attempts:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + "_"
            else:
                display_word += "_"
        print("Word: ",display_word)
        print("Wrong attempts: ",wrong_guesses, "/", max_attempts)

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word correctly.")
            break

        guess = input("Guess a letter: ")
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter at a time.")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

    if wrong_guesses == max_attempts:
        print("You Lose the game")
        print("The word was:", word)

    play_again = input("Do you want to play again? (yes/no): ")
print("Thank you for playing Hangman!")
