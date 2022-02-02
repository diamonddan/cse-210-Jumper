
class GraphicManager:
    """This class is responsible of dealing with the strings that will print out the parachuter

    Args:
        self (GraphicManager): An instance of GraphicManager

    Stereotype:
        Service Provider / Interfacer / Information Holder
    
    Attributes:
            parachute(list): A list of strings used to print the parachute
    """
   
    def __init__(self):
        """The class constructor.

        Args:
            self(GraphicManager): An instance of GraphicManager
        """


    def print_parachute(self):
        """This function process the words in the parachute list to print out the parachute

        Args:
            self(GraphicManager): An instance of GraphicManager
        """

    def update_graphic(self, isCorrect, remainingGuesses):
        """This function updates the parachute list to print out the parachute each turn.

        Args:
            self(GraphicManager): An instance of GraphicManager
            isCorrect(Boolean): Receives an Boolean value for the guess of the user. If it's right (True) it won't change the parachute
                if it is wrong(False) it will remove the top part of the parachute.
            remainingGuesses(integer): Number of guesses left before game over.
        """