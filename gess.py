# import re
# from nltk.tokenize import word_tokenize
# from collections import defaultdict, Counter
#
#
# class MarkovChain:
#     def __init__(self):
#         self.lookup_dict = defaultdict(list)
#
#     def _preprocess(self, string):
#         cleaned = re.sub(r'\W+', ' ', string).lower()
#         tokenized = word_tokenize(cleaned)
#         return tokenized
#
#     def add_document(self, string):
#         preprocessed_list = self._preprocess(string)
#         pairs = self.__generate_tuple_keys(preprocessed_list)
#         for pair in pairs:
#             self.lookup_dict[pair[0]].append(pair[1])
#
#     def __generate_tuple_keys(self, data):
#         if len(data) < 1:
#             return
#         for i in range(len(data) - 1):
#             yield [data[i], data[i + 1]]
#
#     def generate_text(self, string):
#         if len(self.lookup_dict) > 0:
#             print("Next word suggestions:", Counter(self.lookup_dict[string]).most_common()[:3])
#         return

# from list import UserAgent
#
# print(UserAgent().random())

import requests

url = "https://d7sms.p.rapidapi.com/secure/sendbatch"

payload = {"messages": [
    {
        "content": "Bulk SMS Content",
        "from": "D7-Rapid",
        "to": ["00201005777505"]
    }
]}
headers = {
    "content-type": "application/json",
    "Authorization": "undefined",
    "X-RapidAPI-Host": "d7sms.p.rapidapi.com",
    "X-RapidAPI-Key": ""
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
