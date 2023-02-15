# Connect 4

This python program is a remake of the classic connect 4 game. It takes 6 rows and 7 columns and 2 players that take turns placing down there assigned colored chips (red 🔴 and yellow 🟡 in this case) which fall down to the lowest possible row in the selected column. The game ends when there are 4 of the same colors in a row either horizontally, vertically, or either diagonal direction and the player with that color is declared the winner. The game can also end if the board fills up with no 4 in a row achived which will result the game in a tie. This is a terminal based game.

## Features

### Existing Features

- #### Board Generation
        The board is created through the use of nested lists containg a variable for empty slots. The nested lists are itirated through and printed to the terminal, with each list taking up a whole row and the next list is printed below it. The final row of the board is a numbering system showing what the column numbers are.
- #### Pieces
        The empty slots are shown through the use of white circles (⚪) and the player pieces are red (🔴) and yellow (🟡). The empty slots and the player pieces are all tied to variables so that the pieces could easily be changed out to whatever is desired. However the spacing between the pieces at the moment is designed for these circular icons. 
- #### Players
        The game gives the option at the beginning to either play as a single player as a computer or as two players taking turns to place the chips. When you choose to play against the computer the player will always be the red pieces and the computer the yellow pieces but whoever starts is randomized. When two players is selected the player with the red pices will go first. This is all made clear through prompts in the terminal before the game begins. 
- #### Computer
        The computer is a very stupid computer that only chooses a column number between 1 and 7 randomly. Attempts to make a smarter computer were made but none of them unfortunatley worked. A slight time delay with the text "Computer is thinking..." is added before the random column number is selected to give the illusion that the computer might actually be smart. This however is just that, an illusion... The computer will then declare what column it has chosen before placing its piece.
- #### Gameplay
         Once the game actually starts the starting piece is declared and a blank board will appear either asking the player to input a column between 1 and 7 or the computer will place a piece down. Once the column is chosen a new board will be printed with the piece at the bottom of whatever column was chosen. The code takes an input from the user as an iteger between 1 and 7, which it will then convert into its corresponding index and then starts looking for an EMPTY space on the board in the selected column starting from the bottom. Once an EMPTY slot is found the computer will replace that EMPTY white piece with the colored piece of who's ever turn it was. This will then end the turn and turn over to the next color.
- #### Game End
        The game runs in a while loop that continues the game as long as the winning criterea is not met. The code will continuesly check for 4 colors in a row in any direction. This check will turn up with either a True or a False boolean value. As long as it returns False then the game will carry on. Once the 4 colors in a row are found the program will declare that color to be the winner and break out of the while loop and end the game. If the board were to fill up completely with pieces and no winner is found, the program will declare a draw and exit the while loop ending the game. The program checks this by looking for EMPTY slots on the top row of the board, if none are found and noone has won the game is a draw. 
- #### Score Keeping
        The game will ask for your name in single player and both players names in two player. These names will then be appended onto a google sheet as PLAYER 1 and PLAYER 2 (the computer will be assigned to PLAYER 2 with the name 'Computer') followed by a date and time stamp of when the game commenced. Once a player has won the winner will be appended to the sheet followed by a date and time stamp of when the game finished. If the game is exited early or if the game reaches a draw, nothing will be appended to the sheet after the names. 
- #### Inputs
        The names that are given will be treated as strings so any input allowed. 
        To pick a column a number between 1 and 7 has to be chosen. If a number outside of this range is given the program will tell the user that this column does not exist and that they should try again. If anyting other than a base 10 number is put in when choosing a column the program will tell the user that  their input is not a base 10 number and that they should try again. If a column is chosen that is already full to the top with pieces the program will let the user know that the column is full and that they should try again. This all runs on while loops so the the user can input as many incorrect options as they want without breaking the code. This also works for the computer, and the computer will keep on trying to find a column that is not full. 




### Features Left to Implement
    - A smarter ai that checks the board for potential wins and losses and makes a decision based on that using a scoring system where each potential position is given a score based on whats around it. The position with the highest score is where the ai would choose to place its piece.
    - A scoring system that keep track of how many times a certain player has won and also gives you the calculated duration of your game. Perhaps even a time given for how long people were playing before they quite and also keeps track of a ture draws(full boards as opposed to an early exit of the game).
    - A way to end the game with a written command.
    - A way to access your wins and losses through the terminal.


 ## Testing and Bugs
    The game was tested constantly while being written with loads and loads of bugs being found and fixed along the way. Getting the draw feature and the checking if a column is full were found to be particularly ticky but solutions were found in the end.
    No current bugs have been found in the end product.
    The game has been tested on muliple different devices with full funcionality. 

## Validator Testing
- PEP8
    - Only errors that were found were that lines were too long

## Deployment
- Deployed through heroku
    - https://connect4-lukasrid.herokuapp.com/

## Credits
- Code Insitute
- W3Schools
- Youtube

   


