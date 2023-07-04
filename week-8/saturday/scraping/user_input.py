class UserInput:
    def get_state():
        """function gets states from the user"""
        while True:
            state = input("Enter the state for more information> ").lower()

            if state in ("vic", "nsw", "qld", "act", "nt", "tas", "sa", "wa"):
                return state
            else:
                print(f"State '{state}' does not exist in Australia")
                