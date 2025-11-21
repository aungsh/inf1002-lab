/*******************************************************************************
Task Description: 
    Write a program called guessWord that plays a two-player word-guessing game 
    using a similar procedure to the guessInteger program from C Lab1. 
    The game will proceed as follows:
    1.	Player 1 will be asked to enter a word of up 12 letters. The word should 
        contain only the lower-case English letters from ‘a’ to ‘z’, and no 
        punctuation marks or digits.
        a.	If Player 1 enters a word with upper case letters, the program 
            should change them to lower case.
        b.	If Player 1 enters a word with punctuation marks or digits, he or she 
            should be asked to enter another word.
        c.	The program does not need to check that the word is a “real” word 
            (i.e. in a dictionary).
    2.	Player 2 (who again has not been watching Player 1) will be asked to 
        guess one letter at a time.
        a.	Player 2 has maximum 7 guesses.
        b.  At the beginning of each round, the program will output a row of 
            characters containing one underscore for every letter in the word to 
            be guessed. If Player 2 has previously guessed a letter that is in 
            the word, the underscore will be replaced by that letter.
        c.	Player 2 will enter one letter. If he or she enters an upper-case 
            letter, the program will convert it to lower case. If he or she 
            enters a punctuation mark or digit, he or she will be considered 
            to have made an incorrect guess.
        d.	If the letter is not in the word, the number of incorrect guesses 
            will be incremented.
        e.	If the letter is in the word, every position in the word in which 
            that letter occurs will be revealed at the start of the next round.
    3.	The game ends when either Player 2 has guessed all the letters of the 
        word, or when Player 2 has made seven incorrect guesses.

    Note: 
        •	Use macros (#define) to represent all constants, so that it is easy 
            to change things like the number of guesses allowed, the highest number 
            allowed, and so on. 
        •	Don’t use sys.argv[] for user inputs. Use other functions such as 
            scanf(), fgets(), fgetc(), etc.,
        •	You can use the ctype.h and string.h libraries for manipulating 
            characters and strings.
        •	You may find it useful to write “helper” functions that perform tasks 
            like checking that Player 1’s string is valid, whether and where 
            Player 2 has correctly guessed a letter, and so on.
        •	There is no white space in the print after the colons (:).
        •	All print statements terminate with a new line (\n).
        •	When only one guess is remaining, use “guess” instead of “guesses”. 
        •	Include comment to your code that explains what each section of it does. 

Some sample output is shown below, with the user input shown in red:
Example – 1:
    Player 1, enter a word of no more than 12 letters:
    Topsy-turvy
    Sorry, the word must contain only English letters.
    Player 1, enter a word of no more than 12 letters:
    Cat
    Player 2 has so far guessed:
    _ _ _
    Player 2, you have 7 guesses remaining. Enter your next guess:
    e
    Player 2 has so far guessed:
    _ _ _
    Player 2, you have 6 guesses remaining. Enter your next guess:
    a
    Player 2 has so far guessed:
    _ a _
    Player 2, you have 6 guesses remaining. Enter your next guess:
    c
    Player 2 has so far guessed:
    c a _
    Player 2, you have 6 guesses remaining. Enter your next guess:
    t
    Player 2 has so far guessed:
    c a t
    Player 2 wins.

Example – 2:
    Player 1, enter a word of no more than 12 letters:
    computer
    Player 2 has so far guessed:
    _ _ _ _ _ _ _ _
    Player 2, you have 7 guesses remaining. Enter your next guess
    a
    Player 2 has so far guessed:
    _ _ _ _ _ _ _ _
    Player 2, you have 6 guesses remaining. Enter your next guess:
    b
    Player 2 has so far guessed:
    _ _ _ _ _ _ _ _
    Player 2, you have 5 guesses remaining. Enter your next guess:
    d
    Player 2 has so far guessed:
    _ _ _ _ _ _ _ _
    Player 2, you have 4 guesses remaining. Enter your next guess:
    e
    Player 2 has so far guessed:
    _ _ _ _ _ _ e _
    Player 2, you have 4 guesses remaining. Enter your next guess:
    f
    Player 2 has so far guessed:
    _ _ _ _ _ _ e _
    Player 2, you have 3 guesses remaining. Enter your next guess:
    g
    Player 2 has so far guessed:
    _ _ _ _ _ _ e _
    Player 2, you have 2 guesses remaining. Enter your next guess:
    h
    Player 2 has so far guessed:
    _ _ _ _ _ _ e _
    Player 2, you have 1 guess remaining. Enter your next guess:
    i
    Player 2 has so far guessed:
    _ _ _ _ _ _ e _
    Player 1 wins.
*******************************************************************************/
#include <stdio.h>
#include <stdbool.h>
#include <ctype.h> 
#include <string.h>

int checkLetters(char *text) {
    for (int i = 0; text[i] != '\0'; i++) {
        if (!isalpha(text[i]) && !isspace(text[i])) {
            return false;
        }
    }

    return true;
}

void lowercaseChar(char *text) {
    for (int i = 0; text[i] != '\0'; i++) {
        if (text[i] >= 'A' && text[i] <= 'Z') {
            text[i] = text[i] - 'A' + 'a';
        }
    }
}

int main() {
    char text1[13];

    while (1) {
        printf("Player 1, enter a word of no more than 12 letters:\n");
        scanf(" %[^\n]", text1);
        lowercaseChar(text1);

        if (checkLetters(text1)) {
            break;
        }

        printf("Sorry, the word must contain only English letters.\n");
        continue;
    }

    char found[strlen(text1)+1];
    int guessCount = 7;

    for (int i = 0; i < strlen(text1); i++) {
        found[i] = '_';
    }

    while (guessCount > 0) {

        printf("Player 2 has so far guessed:\n");
        int guessedAll = 1;

        for (int i = 0; i < strlen(text1); i++) {
            printf("%c ", found[i]);
            if (found[i] == '_') {
                guessedAll = 0;
            }
        }

        printf("\n");

        if (guessedAll == 1) {
            printf("Player 2 wins.");
            break;
        }

        if (guessCount == 1) {
            printf("Player 2, you have %d guess remaining. Enter your next guess:\n", guessCount);
        } else {
            printf("Player 2, you have %d guesses remaining. Enter your next guess:\n", guessCount);
        }

        char text2;
        scanf(" %c", &text2);
        text2 = tolower(text2);
        int correctGuess = 0;

        for (int i = 0; i < strlen(text1); i++) {
            if (text1[i] == text2) {
                found[i] = text2;
                correctGuess = 1;
            }
        }

        if (correctGuess == 0) {
            guessCount -= 1;
        }

    }

    if (guessCount <= 0) {
        printf("Player 2 has so far guessed:\n");
        for (int i = 0; i < strlen(text1); i++) {
            printf("%c ", found[i]);
        }
        printf("\nPlayer 1 wins.");
    }

    return 0;
}