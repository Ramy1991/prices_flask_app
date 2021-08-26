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
import urllib3

url = 'https://prices-assist.herokuapp.com/search_items_online'
myobj = {'my_data': 'somevalue'}
x = requests.post(url, data=myobj)
# for c in x.json():
print(x.text)

# from aiohttp import ClientSession, TCPConnector
# import asyncio
# import sys
# import pypeln as pl
# from scripts_py.supported_website import supported_search_website_xp, currency
# from lxml import html
# from fake_useragent import UserAgent
# import re
# import json
#
# limit = 50
#
#
# # cred = credentials.Certificate(r'D:\PyChaarm\Prices\bright-lattice-260000-firebase-adminsdk.json')
# # firebase_admin.initialize_app(cred, {'databaseURL': 'https://bright-lattice-260000.firebaseio.com'})
#
#
# # def selenium_request(url):
# #     executable_path = r"D:\PyChaarm\Prices\geckodriver.exe"
# #     # executable_path = r"D:\PyChaarm\Prices\phantomjs-2.1.1-windows\bin\phantomjs.exe"
# #     options = Options()
# #     options.headless = True
# #     driver = webdriver.Firefox(options=options, executable_path=executable_path)
# #     driver.get(url)
# #     tree = html.fromstring(driver.page_source)
# #     driver.close()
# #     return tree
#
# class SearchOnlineForItems:
#     def __init__(self, search_value, country, lang):
#         self.search_value = search_value
#         self.country = country
#         self.lang = lang
#         self.items_json = []
#         self.response = []
#
#     def create_url(self):
#         websites = {
#             'eg': {
#                 'en': {
#                     'https://www.noon.com/egypt-en/search?q={}': 'https://www.noon.com/egypt-en/{}/p',
#                     'https://egypt.souq.com/eg-en/{}/s/?as=1': 'https://egypt.souq.com/eg-en/{}/s/',
#                     'https://www.jumia.com.eg/catalog/?q={}': 'https://www.jumia.com.eg',
#                     'https://btech.com/en/catalogsearch/result/?q={}': 'https://btech.com/en/'
#                 },
#                 'ar': {
#                     'https://www.noon.com/egypt-ar/search?q={}': 'https://www.noon.com/egypt-ar/{}/p',
#                     'https://egypt.souq.com/eg-ar/{}/s/?as=1': 'https://egypt.souq.com/eg-ar/{}/s/',
#                     'https://www.jumia.com.eg/ar/catalog/?q={}': 'https://www.jumia.com.eg/ar',
#                     'https://btech.com/ar/catalogsearch/result/?q={}': 'https://btech.com/ar/'
#                 }
#             },
#             'ae': {
#                 'en': {
#                     'https://www.amazon.ae/s?k={}&ref=nb_sb_noss_2': 'https://www.amazon.ae/dp/{}/?language=en_AE',
#                     'https://www.noon.com/uae-en/search?q={}': 'https://www.noon.com/uae-en/{}/p'
#                 },
#                 'ar': {
#                     'https://www.amazon.ae/s?k={}&language=ar_AE&ref=nb_sb_noss_2': 'https://www.amazon.ae/dp/{}/?language=ar_AE',
#                     'https://www.noon.com/uae-ar/search?q={}': 'https://www.noon.com/uae-ar/{}/p'
#                 }
#             },
#             'sa': {
#                 'en': {
#                     'https://www.amazon.sa/s?k={}&ref=nb_sb_noss_2': 'https://www.amazon.sa/dp/{}/?language=en_AE',
#                     'https://www.noon.com/saudi-en/search?q={}': 'https://www.noon.com/saudi-en/{}/p'
#                 },
#                 'ar': {
#                     'https://www.amazon.sa/s?k={}&language=ar_AE&ref=nb_sb_noss_2': 'https://www.amazon.sa/dp/{}/?language=ar_AE',
#                     'https://www.noon.com/saudi-ar/search?q={}': 'https://www.noon.com/saudi-ar/{}/p'
#                 }
#             }
#         }
#         urls = []
#         for url, i_url in websites.get(self.country).get(self.lang).items():
#             urls.append({url.format(self.search_value): i_url})
#         return urls
#
#     def website_get_xp(self, url):
#         websites = supported_search_website_xp.keys()
#         for website in websites:
#             if website in url:
#                 return website
#
#     def user_agent(self):
#         return re.search(r'(.*?)\)', UserAgent().random).group(1) + "MSIE 12;)"
#
#     async def fetch(self, url, session):
#         header = {
#             "User-Agent": self.user_agent(),
#             "Accept": "*/*",
#             "Accept-Language": "*/*",
#             "Accept-Charset": "*/*",
#             "Connection": "keep-alive",
#             "Keep-Alive": "300"
#         }
#         product_url = ''.join(url.values())
#         category_url = ''.join(url.keys())
#
#         async with session.get(category_url, headers=header) as response:
#             data = await response.text()
#             self.response.append({'response_data': data, 'product_url': product_url, 'category_url': category_url})
#
#     def validate_data(self, response_data, category_url, product_url):
#         title_xp = supported_search_website_xp.get(self.website_get_xp(category_url)).get('title_xp')
#         image_xp = supported_search_website_xp.get(self.website_get_xp(category_url)).get('image_xp')
#         price_xp = supported_search_website_xp.get(self.website_get_xp(category_url)).get('price_xp')
#         uid_xp = supported_search_website_xp.get(self.website_get_xp(category_url)).get('uid_xp')
#         url_xp = supported_search_website_xp.get(self.website_get_xp(category_url)).get('url_xp')
#         cate_xp = supported_search_website_xp.get(self.website_get_xp(category_url)).get('cate_xp')
#         tree = html.fromstring(response_data)
#         if self.website_get_xp(category_url) == 'noon.com':
#             json_text = re.findall(r'.hits..(.*)..searchEngine.', response_data)
#             # print(json_text.group(1))
#
#             json_items = json.loads(json_text[0])
#
#             item_categories = []
#             item_titles = []
#             item_images = []
#             item_uid = []
#             item_prices = []
#             item_urls = []
#             item_brand = []
#
#             for json_item in json_items:
#                 item_brand.append(json_item.get('brand'))
#                 item_urls.append(product_url.format(json_item.get('sku')))
#                 item_uid.append(json_item.get('sku'))
#                 item_categories.append(''.join(list(tree.xpath(cate_xp))))
#
#                 item_titles.append(json_item.get('name'))
#                 if type(json_item.get('sale_price')) != int:
#                     item_prices.append(json_item.get('price'))
#                 else:
#                     item_prices.append(json_item.get('sale_price'))
#                 item_images.append(
#                     'https://a.nooncdn.com/t_desktop-pdp-v1/{}.jpg'.format(json_item.get('image_key')))
#         else:
#             item_titles = list(tree.xpath(title_xp))
#             item_images = list(tree.xpath(image_xp))
#             item_uid = list(tree.xpath(uid_xp))
#             item_prices = list(tree.xpath(price_xp))
#             item_urls = list(tree.xpath(url_xp))
#             item_categories = list(tree.xpath(cate_xp))
#             item_brand = list(tree.xpath(cate_xp))
#
#         if len(item_categories) != len(item_titles):
#             item_categories = list(''.join(tree.xpath(cate_xp)) for i in range(len(item_titles)))
#             item_brand = list('none' for i in range(len(item_titles)))
#
#         items_dict = {
#             self.website_get_xp(category_url): {
#             }
#         }
#         for uid, title, image, price, i_url, cate, brand in zip(item_uid, item_titles, item_images, item_prices,
#                                                                 item_urls, item_categories, item_brand):
#             uid = uid.split(",")
#             try:
#                 price = ''.join(re.findall(r'(\d+)', price))
#             except TypeError:
#                 pass
#             if self.website_get_xp(category_url) == 'jumia.com':
#                 i_url = ''.join([product_url, i_url])
#
#             item_dict = {
#                 uid[0]: {
#                     "item_title": title,
#                     "item_image": image,
#                     "item_price": int(price),
#                     "item_url": i_url,
#                     "item_uid": uid[0],
#                     "item_cate": cate,
#                     "item_brand": brand
#                 }
#             }
#             items_dict[self.website_get_xp(category_url)].update(item_dict)
#
#         self.items_json.append(items_dict)
#
#     def loop_response(self):
#         for item_data in self.response:
#             self.validate_data(item_data.get('response_data'), item_data.get('category_url'),
#                                item_data.get('product_url'))
#
#     def main(self):
#         # links = self.create_url()
#         pl.task.each(
#             self.fetch,
#             self.create_url(),
#             workers=limit,
#             on_start=lambda: dict(session=ClientSession(connector=TCPConnector(limit=None))),
#             on_done=lambda session: session.close(),
#             run=True,
#         )
#         # run loop through output to validate each data from website
#         self.loop_response()
#         return self.items_json
#
#
# d = SearchOnlineForItems('iphone', 'eg', 'en').main()
# print(d)
