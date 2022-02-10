#Jumper
Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time.

##Rules
*The puzzle is a secret word randomly chosen from a list.
*The player guesses a letter in the puzzle.
*If the guess is correct, the letter is revealed.
*If the guess is incorrect, a line is cut on the player's parachute.
*If the puzzle is solved the game is over.
*If the player has no more parachute the game is over.
## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- Jumper             (source code for game)
  +-- game              (specific game classes)
    +-- director.py
    +-- graphic_manager.py
    +-- terminal_server.py
    +-- word_manager.py
  +-- __init__.py       (python package file)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0

## Authors

*Daniel McNary (blackanddan@byui.edu)
*Heidi Munson (mun21014@byui.edu)
*Kelly Nebeker (bnknebeker@gmail.com)
*Armando Martinez (mar21095@byui.edu)
*Diego Gomez (gom21026@byui.edu)