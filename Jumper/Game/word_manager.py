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
      working_word (list): holds the value of the masked word
      word_list (list): holds the list of possible words to choose from
      total_guessed_words (integer): holds the total number of letters guessed
   """
   def __init__(self):
      """ The class constructor

      Args: 
         self (WordManager): an instance of WordManager
      """
      self._word_list = ["hardware", "software", "memory", "program", "firewall", "network", "database", "algorithm", "backup", "binary"]
      self._correct_word = random.choice(self._word_list) #choose a random word from word_list
      self._working_word = []
      for i in range(len(self._correct_word)):  #initialize working_word with underscores the same length of correct_word
         self._working_word.append('_')
      self._total_guessed_words = 0


   """Check if the letter from the user exist in the word 
   if it exists call add_letter to replace underscores with the letter
   """
   def check_letter(self, letter):
      positions = [] #the list of positions to be replaced in working_word
      position = 0
      for i in self._correct_word:  #iterate over correct_word to check if letter is in correct_word
         if letter == i:
            positions.append(position) #keep the position in positions
         position += 1
      
      if len(positions) > 0:
         self.add_letter(letter, positions)
         return True
      else:
         return False
   
   """Recive a list with the positions in working_word to be repalced with letter"""
   def add_letter(self, letter, positions): #Daniel pls complete this method, follow the word with the assigments.
      pass
   
   def print_guessedWord(self):
      for i in self._working_word:
         print(f"{i} ", end='')
      print("")

   def user_wins(self):
      return self._total_guessed_words == len(self._correct_word)
