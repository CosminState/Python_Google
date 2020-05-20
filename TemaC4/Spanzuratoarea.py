import random

wordsList = ['masina', 'bicicleta', 'python', 'spanzuratoarea']
used_letters = []
find_word = random.choice(wordsList)
guess_word = []


def start():
    print("Let's play")

    for char in find_word:
        guess_word.append('_')
    print("The word to be guessed is:\n", ' '.join(guess_word))

    tokens = 8

    while tokens > 0:
        letter = input("Pick a letter: ").lower()
        if letter == 'exit':
            break

        if letter.isalpha() and len(letter) == 1:
            if letter in used_letters:
                print("You have already chosen this letter\n", "Try again")
            else:

                used_letters.append(letter)

                if letter in find_word:
                    for x in range(0, len(find_word)):
                        if find_word[x] == letter:
                            guess_word[x] = letter
                            print(' '.join(guess_word))

                    if not '_' in guess_word:
                        print('You won!')
                        break
                else:
                    print('The word does not contain this letter')
                    tokens -= 1
                    print(f'You have {tokens} more attempts')
                    if tokens == 0:
                        print('You lost :(')
        else:
            print("Pick one letter")


if __name__ == '__main__':
    start()