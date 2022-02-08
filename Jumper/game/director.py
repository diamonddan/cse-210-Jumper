#################################
# TEMPLATE CLASS
# Handles user input and the main game loop.
################################
from game.word_manager import WordManager
from game.graphic_manager import GraphicManager
from game.terminal_service import TerminalService

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
      self._graphic = GraphicManager() 
      self._is_playing = True 
      self._words= WordManager() 
      self._terminal_service = TerminalService() 

      
   

   #TEMPLATE FUNCTION
   #contains game loop--order of play
   def start_game(self):
      """The class Information Holder
      Args:
         self (Director): an instance of Director

      """
      self._words.get_word() #gets word from word manager 

      #display hypthens 

      self._graphic.print_parachute() #display graphic

      while self._is_playing: 
         self._get_inputs() 
         self._do_updates() 
         self._do_outputs() 

   def get_inputs(self): 
      """ gets the masked word from word manager

      Args: 
         self (Director): an instance of Director
      """

      #ask for letter guess 

      guess =("\nGuess a letter [A-Z]: ") 
      self._words.is_correct(guess)

   def do_updates(self): 
      """Updates letter found in word or removes portion of parachute 

      Args: 
      self (Director): An instance of Director.
      """ 

      ##looks for letter in word 

      #updates letter in word 

      #removes portion of parachute 

   def do_outputs(self): 
      """Determines game won or lost. Continues play or ends game. 
         
      Args: 
      self (Director): An instance of Director. 
      """ 

      #if word is solved - winner game over 

      if self._words.winner(): 
         self._is_playing = False 
         print("You Won") 

      #if parachute removed - lost game over 
      self._is_playing = (self._jumper == "") 
      if not self._is_playing: 
         print("Game Over") 
 
      
   