#################################
# TEMPLATE CLASS
# Handles user input and the main game loop.
################################
from Game.word_manager import WordManager
from Game.graphic_manager import GraphicManager
from Game.terminal_service import TerminalService

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
      self._guess = ''
      
   

   #TEMPLATE FUNCTION
   #contains game loop--order of play
   def start_game(self):
      """The class Information Holder
      Args:
         self (Director): an instance of Director

      """
      
      #display hypthens 


      while self._is_playing: 
         self.get_inputs() 
         self.do_updates() 
         self.do_outputs() 

   def get_inputs(self): 
      """ gets the masked word from word manager

      Args: 
         self (Director): an instance of Director
      """
      self._words.print_guessedWord() #display gueessed word from word manager 

      self._graphic.print_parachute() #display graphic
      #ask for letter guess 
      self._guess = (self._terminal_service.read_text("\nGuess a letter [A-Z]: ")).lower()
      

   def do_updates(self): 
      """Updates letter found in word or removes portion of parachute 

      Args: 
      self (Director): An instance of Director.
      """ 
      # Heidi you can also give feedback to the user with the wrong() and right() methods from terminal_service 
      # (check_letter return true if guess is in the word false in other case)

      #looks for letter in word and updates letter in word
      self._words.check_letter(self._guess)
      if self._words.check_letter(self._guess) == True:
         self._terminal_service.right()
      else:
         self._terminal_service.wrong()
         #removes portion of parachute  -> Use decrease_lives() from graphic_manager
         self._graphic.decrease_lives()


   def do_outputs(self): 
      """Determines game won or lost. Continues play or ends game. 
         
      Args: 
      self (Director): An instance of Director. 
      """ 

      #if word is solved - winner

      if self._words.user_wins() == True: 
         self._is_playing = False 
         # print("You Won") #Diego pls Change this line for the method  you_win()
         self._words.print_guessedWord()  
         self._graphic.print_parachute()
         self._terminal_service.you_win()
         exit()

      #if parachute removed -  game over 
      if self._graphic.get_lives() <= 0: 
         # print("Game Over") #Diego pls Change this line for the method game_over()
         self._words.print_guessedWord() 
         self._graphic.print_parachute()
         self._terminal_service.game_over()
         exit()
   