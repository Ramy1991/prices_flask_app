# from spellchecker import SpellChecker
#
# spell = SpellChecker()
#
# # find those words that may be misspelled
# misspelled = spell.unknown(["ubntu"])
#
# for word in misspelled:
#     # Get the one `most likely` answer
#     print(spell.correction(word))
#
#     # Get a list of `likely` options
#     print(spell.candidates(word))

# from autocorrect import Speller
#
# spell = Speller(lang='en')
#
# print(spell('episde'))

# class SearchOnlineForItems:
#     def test(self, text):
#         return text
#
#
# d = SearchOnlineForItems()
# print(d.test('sda'))

import requests

url = 'http://127.0.0.1:5000/'
myobj = {'data': 'somevalue'}

x = requests.post(url, data=myobj)

print(x.text)
