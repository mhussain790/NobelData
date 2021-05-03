"""
Author: Masud Hussain
Course: CS162
Assignment: 5B
"""

import json


class NobelData:

    def __init__(self):
        with open("nobels.json", "r") as infile:
            nobel_dictionary = json.load(infile)
        self._nobel_dictionary = nobel_dictionary

    def search_nobel(self, year, category):
        winner_list = []

        # Test Searches
        # print(self.nobel_dictionary["prizes"][0]["laureates"][1]["surname"])
        # print(self.nobel_dictionary["prizes"][0]["year"])

        # Loop through the keys in the prizes key from noble_dictionary
        for keys in self._nobel_dictionary["prizes"]:

            # If the year and category from the key match then proceed to the laureates key
            if year == keys["year"] and category == keys["category"]:
                for items in keys["laureates"]:

                    # Append surname of the winner to the winner_list
                    winner = items["surname"]
                    print(items["surname"])
                    winner_list.append(winner)

        # Sort the winner list then print to console
        winner_list.sort()
        print(winner_list)


# nd = NobelData()
# nd.search_nobel("2018", "chemistry")