import random

words = ['jackpot', 'jogging', 'unworthy', 'wispy', 'pneumonia', 'unitato', 'nirvana']

# Randomly choose a word from the list
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]   # create a list of underscores
attempts = 13   # number of allowed attempted
print("Welcome to Hangman")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate (chosen_word):
            if letter == guess:
                word_display[index] = guess #revel letter
    else:
        print("That letter is incorrect, idiot!!")
        attempts -= 1

# game conclusion

if '_' not in word_display:
    print("You guessed it right!")
    print(' '.join(word_display))
    print("You survived!!")
else:
    print("Yikes, you need more practice")