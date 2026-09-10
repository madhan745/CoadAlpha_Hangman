import random


words = ["python", "computer", "program"]


word = random.choice(words)


hidden_word = ["_"] * len(word)


guessed_letters = []


incorrect_guesses = 0

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")


while incorrect_guesses < 6 and "_" in hidden_word:

    print("\nWord:", " ".join(hidden_word))
    print("Incorrect guesses:", incorrect_guesses, "/ 6")

   
    guess = input("Guess a letter: ").lower()

  
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

  
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    
    guessed_letters.append(guess)

   
    if guess in word:

        print("Correct guess!")

     
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess

    else:
        incorrect_guesses += 1
        print("Wrong guess!")


if "_" not in hidden_word:
    print("\nCongratulations! You won!")
    print("The word was:", word)

else:
    print("\nGame over!")
    print("You used all 6 incorrect guesses.")
    print("The word was:", word)
