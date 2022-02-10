
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
        self._lives = 7
        self._parachute = {
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
        key = self._lives
        print('')
        for i in self._parachute[key]:
            print(i)

    def get_lives(self):
        return self._lives
        
    #Kelly pls add a method decrease_lives() to decrease the number of lives here so Heidi can use it in director.py
    def decrease_lives(self):
        self._lives -= 1