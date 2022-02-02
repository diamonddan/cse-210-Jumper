import random

############################
#TEMPLATE CLASS
# Manages a selected word including masking.
############################
class WordManager:
   """
   This class is responsible for getting and modifying the word being used.
   
   Sterotypes: Service provider, information holder, interfacer

   Args:
      self (WordManager): An instance of GraphicManager

   

   Attributes:
      correct_word (string): holds the value of the correct word
      working_word (string): holds the value of the masked word
      remaining_guesses (int): holds the value of the number of remaining guesses
      word_list (list): holds the list of possible words to choose from
      correct_list (list): holds the list of correct guesses
   """
   def __init__(self):
      """ The class constructor

      Args: 
         self (WordManager): an instance of WordManager
      """
      

   #TEMPLATE FUNCTION
   #gets working word from word data class
   def get_word(self):
      """ returns a random word from the word_list

      Args:
         self (WordManager): an instance of WordManager
      """
      

   #update and return the users word after a correct guess given a letter
   def update_word(self):
      """ resets masked word and constructs it again using correct guesses

      Args:
         self (WordManager): an instance of WordManager
      """
      

   def is_correct(self, letter):
      """ returns true or false based on whether guess was correct

      Args:
         self (WordManager): an instance of WordManager
         letter (string): the current user guess
      """
      

