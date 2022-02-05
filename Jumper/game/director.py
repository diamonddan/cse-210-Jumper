#################################
# TEMPLATE CLASS
# Handles user input and the main game loop.
################################
from Game.word_manager import WordManager
from Game.graphic_manager import GraphicManager

class Director:

   """
   This class is working to call start_game, get_word_masked, get_word, and get_guessed_left. 

   Sterotypes: Structurer, Coordinator, Controller
   
   Args:
      start_game:Starts the game and calls get_word, update_word, and get_word_masked
      get_word_masked:Gets the word the user will guess on
      get_word:matches the correct word from get_word_masked
      get_guessed_left:Gives the user the remaining guesses

   
   """

   #Initialize necessary classes and attributes
   def __init__(self):
      """The class constructor
      Args:
         self.WordManager: an instance for word_Manager
      self.GraphicManager: an instance for graphic_manager
      """
   

   #TEMPLATE FUNCTION
   #contains game loop--order of play
   def start_game(self):
      """The class Information Holder
      Args:
         self (WordManager): an instance of WordManager

      """
    
   
   #TEMPLATE FUNCTION
   #returns masked/working word from word_manager
   def get_word_masked(self):
      """ gets the masked word from word manager

      Args: 
         self (WordManager): an instance of WordManager
      """

      """ gets the number of remaining guesses

      Args: 
         self (WordManager): an instance of WordManager
      """
      
   
   #TEMPLATE FUNCTION
   #returns correct word from word manager
   def get_word(self):
      """ gets the correct word from word manager

      Args: 
         self (WordManager): an instance of WordManager
      """


   def get_input(self):
      """ gets input from the user

      Args: 
         self (WordManager): an instance of WordManager
      """
      
    
   def print_remaining_guesses(self):
      """ prints the remaining guesses to the console

      Args: 
         self (WordManager): an instance of WordManager
      """
      