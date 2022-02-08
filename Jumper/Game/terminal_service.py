class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
    
    def right(self):
        """Displays the text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
        """
        print('That letter is in the word!')

    def wrong (self):
        """Displays the text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
        """
        print('That letter is not in the word!')

    def game_over(self):
        """Displays the text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
        """
        print('--GAME OVER--')
    
    def you_win(self):
        """Displays the text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
        """
        print('You WON!!')


    # def output_text (self,text):
    #     """Displays the given text on the terminal. 

    #     Args: 
    #         self (TerminalService): An instance of TerminalService.
    #         text (string): The text to display
    #     """
    #     print(text)