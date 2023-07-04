# - scrape the website
# - user which states
#     - 7d average
#     - active cases
# - percent of new cases with respect active cases
# - decrease or increase
from user_input import UserInput
from scrape import Scrape
from display import DisplayStats

if __name__ == "__main__":
    url = 'https://covidlive.com.au/'
    option = "c"
    while option == "c":
        # clean terminal
        DisplayStats(None).clear_terminal()

        # get state from user
        state = UserInput.get_state()
        
        # scrape website and get dictionary of website
        # get a stats from scraping
        scrape = Scrape(url=(url + state))
        stats = scrape.stats()

        # display stats
        DisplayStats(stats).print()

        # option to continue for next state
        option = input("Enter 'c' to continue")
