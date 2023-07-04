import os

class DisplayStats:
    def __init__(self, stats):
        self.stats = stats


    def print(self):
        self.clear_terminal()
        print(f"""
            Hello from Covid Live

            - 7 day average is {self.stats["average_7d"]}
            - Active cases are {self.stats["active_case"]}
            - New Cases are {self.stats["percent_new_case"]} percent
            - Cases {self.stats["case_decreased"]}
        """)

    def clear_terminal(self):
        try:
            os.system('clear')
        except:
            os.system('cls')

        
