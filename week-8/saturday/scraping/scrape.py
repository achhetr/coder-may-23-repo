import requests
from bs4 import BeautifulSoup

class Scrape:
    def __init__(self, url):
        self.__soup = self.__html_soup(url)

    def stats(self):
        return {
            'average_7d': self.__average_7d(),
            'active_case': self.__active_case(),
            'percent_new_case': self.__percent_new_case(),
            'case_decreased': self.__case_decreased(),
        }

    # private

    def __html_soup(self, url):
        """function gets states from the user"""
        response = requests.get(url)
        return BeautifulSoup(response.content, 'html.parser')

    def __average_7d(self):
        node = self.__soup.find(string="7d Average")
        parent = node.find_parent('tr')
        average = parent.css.select(".TOTAL")[0].text
        return self.__convert_str_into_number(average)


    def __active_case(self):
        node = self.__soup.find(string="7d Average")
        parent = node.find_parent('tr')
        cases = parent.css.select(".TOTAL")[0].text
        return self.__convert_str_into_number(cases)

    def __percent_new_case(self):
        main_node = self.__soup.find_all("table", class_="DAILY-SUMMARY")[0]
        node = main_node.find(string="Cases")
        parent = node.find_parent('tr')
        total_case = parent.css.select(".TOTAL")[0].text
        total_case = self.__convert_str_into_number(total_case)
        new_cases = self.__active_case()

        return str(round(float(new_cases) / total_case, 3) * 100) + '%'

    def __case_decreased(self):
        if self.__case_decreased_or_not():
            return "decreased"
        else:
            return "increased"

    def __case_decreased_or_not(self):
        node = self.__soup.find(string="7d Average")
        parent = node.find_parent('tr')
        cases = parent.css.select(".NET")[0].text
        cases = self.__convert_str_into_number(cases)

        return cases < 0

    def __convert_str_into_number(self, snum):
        return int(snum.replace(",", ""))

# - user which states
#     - 7d average
#     - active cases
# - percent of new cases with respect active cases
# - decrease or increase
