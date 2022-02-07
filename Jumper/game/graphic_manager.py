
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
        self.parachute = {
         7: [
            " ___  ",
            "/___\ ",
            "\   / ",
            " \ /  ",
            "  O   ",
            " /|\  ",
            " / \  ",
            "      ",
            "^^^^^^"],
         6: [
            "/___\ ",
            "\   / ",
            " \ /  ",
            "  O   ",
            " /|\  ",
            " / \  ",
            "      ",
            "^^^^^^"],
         5: [
            "\   / ",
            " \ /  ",
            "  O   ",
            " /|\  ",
            " / \  ",
            "      ",
            "^^^^^^"],
         4: [
            " \ /  ",
            "  O   ",
            " /|\  ",
            " / \  ",
            "      ",
            "^^^^^^"], 
         3: [
            "AHHHH!",
            "  O   ",
            " /|\  ",
            " / \  ",
            "      ",
            "^^^^^^"], 
         2: [
            " /|\   ",
            " / \   ",
            "       ",
            "^^^^^^ "], 
         1: [
            " / \  ",
            "      ",
            "^^^^^^"],  
         0: [
            "O-\//\ ",
            "^^^^^^ "],   
        }


    def print_parachute(self):
        """This function process the words in the parachute list to print out the parachute

        Args:
            self(GraphicManager): An instance of GraphicManager
        """
  
        
        for i in self.status:
            print(self.status[i])



    def update_graphic(self, isCorrect, remainingGuesses):
        """This function updates the parachute list to print out the parachute each turn.

        Args:
            self(GraphicManager): An instance of GraphicManager
            isCorrect(Boolean): Receives an Boolean value for the guess of the user. If it's right (True) it won't change the parachute
                if it is wrong(False) it will remove the top part of the parachute.
            remainingGuesses(integer): Number of guesses left before game over.
        """
        if isCorrect == "False":
            self.status = self.parachute [remainingGuesses]
        


