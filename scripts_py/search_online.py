from lxml import html
import re
import json
from scripts_py.extract_item_data import Websites
from scripts_py.supported_website import supported_website_xp, currency, supported_search_website_xp
from scripts_py.fetch_data_2 import FETCH
from scripts_py.upload_db import UploadDB


class SearchOnlineForItems:
    def __init__(self, search_value, country, lang):
        self.search_value = search_value
        self.country = country
        self.lang = lang
        self.items_json = []
        self.response = []

    def create_url(self):
        # added the product dirct link in order to update it in the db
        websites = {
            'eg': {
                'en': {
                    'https://www.noon.com/egypt-en/search?q={}': 'https://www.noon.com/egypt-en/{}/p',
                    'https://egypt.souq.com/eg-en/{}/s/?as=1': 'https://egypt.souq.com/eg-en/{}/s/',
                    'https://www.amazon.eg/s?k={}&ref=nb_sb_noss_2': 'https://www.amazon.eg/dp/{}/?language=en_AE',
                    'https://www.jumia.com.eg/catalog/?q={}': 'https://www.jumia.com.eg',
                    'https://btech.com/en/catalogsearch/result/?q={}': 'https://btech.com/en/'
                },
                'ar': {
                    'https://www.noon.com/egypt-ar/search?q={}': 'https://www.noon.com/egypt-ar/{}/p',
                    'https://egypt.souq.com/eg-ar/{}/s/?as=1': 'https://egypt.souq.com/eg-ar/{}/s/',
                    'https://www.amazon.eg/s?k={}&ref=nb_sb_noss_2': 'https://www.amazon.eg/dp/{}/?language=ar_AE',
                    'https://www.jumia.com.eg/ar/catalog/?q={}': 'https://www.jumia.com.eg/ar',
                    'https://btech.com/ar/catalogsearch/result/?q={}': 'https://btech.com/ar/'
                }
            },
            'ae': {
                'en': {
                    'https://www.amazon.ae/s?k={}&ref=nb_sb_noss_2': 'https://www.amazon.ae/dp/{}/?language=en_AE',
                    'https://www.noon.com/uae-en/search?q={}': 'https://www.noon.com/uae-en/{}/p'
                },
                'ar': {
                    'https://www.amazon.ae/s?k={}&language=ar_AE&ref=nb_sb_noss_2': 'https://www.amazon.ae/dp/{}/?language=ar_AE',
                    'https://www.noon.com/uae-ar/search?q={}': 'https://www.noon.com/uae-ar/{}/p'
                }
            },
            'sa': {
                'en': {
                    'https://www.amazon.sa/s?k={}&ref=nb_sb_noss_2': 'https://www.amazon.sa/dp/{}/?language=en_AE',
                    'https://www.noon.com/saudi-en/search?q={}': 'https://www.noon.com/saudi-en/{}/p'
                },
                'ar': {
                    'https://www.amazon.sa/s?k={}&language=ar_AE&ref=nb_sb_noss_2': 'https://www.amazon.sa/dp/{}/?language=ar_AE',
                    'https://www.noon.com/saudi-ar/search?q={}': 'https://www.noon.com/saudi-ar/{}/p'
                }
            }
        }
        urls = []
        for cate_url, i_url in websites.get(self.country).get(self.lang).items():
            cate_url = {
                cate_url.format(self.search_value): i_url
            }
            urls.append(cate_url)
        return urls

    def get_category_page_data(self):
        response_data = FETCH(self.create_url(), 'category_page', [self.lang]).start()
        return response_data

    def website_get_xp(self, url):
        websites = supported_search_website_xp.keys()
        for website in websites:
            if website in url:
                return website

    def extract_items_urls(self, response_data, category_url, product_url):
        uid_xp = supported_search_website_xp.get(self.website_get_xp(category_url)).get('uid_xp')
        url_xp = supported_search_website_xp.get(self.website_get_xp(category_url)).get('url_xp')

        tree = html.fromstring(response_data)
        # if self.website_get_xp(category_url) == 'noon.com':
            # json_text = re.findall(r'.hits..(.*)..searchEngine.', str(response_data))
            # json_items = json.loads(json_text[0])
            # item_uid = []
            # item_urls = []
            # for json_item in json_items:
            #     item_urls.append(product_url.format(json_item.get('sku')))
            #     item_uid.append(json_item.get('sku'))

        # else:
        item_uid = list(tree.xpath(uid_xp))
        item_urls = list(tree.xpath(url_xp))
        for uid, item_url in zip(item_uid, item_urls):

            uid = uid.split(",")
            # get url for jumia
            if self.website_get_xp(category_url) == 'jumia.com':
                item_url = ''.join([product_url, item_url])
            elif 'amazon.' in self.website_get_xp(category_url):
                item_url = product_url.format(''.join(uid))
            elif 'noon' in self.website_get_xp(category_url):
                uid_ = ''.join(uid).replace('productBox-', '')
                item_url = product_url.format(uid_)
            #  check current lang to get other lang url
            if self.lang == 'en':
                lang = 'ar'
            else:
                lang = 'en'

            uid[0] = {
                f"item_url_{self.lang}": item_url,
                f"item_url_{lang}": self.get_urls_for_en_ar(item_url),
                "item_uid": uid[0],
                "item_website": self.website_get_xp(category_url),
                "country": self.country,
                "search_value": self.search_value
            }

            self.items_json.append(uid[0])
        # print(self.items_json)

    def get_urls_for_en_ar(self, item_url):
        if self.lang == 'en':
            if self.website_get_xp(item_url) == 'jumia.com':
                item_url = item_url.replace('.eg/', '.eg/ar/')
                return item_url
            else:
                item_url = item_url.replace('en/', 'ar/')
                return item_url
        else:
            if self.website_get_xp(item_url) == 'jumia.com':
                item_url = item_url.replace('eg/ar/ar/', 'eg/')
                return item_url
            else:
                item_url = item_url.replace('ar/', 'en/')
                return item_url

    def main(self):
        self.response = self.get_category_page_data()
        for key, item_data in self.response.items():
            category_url = item_data.get('item_url')
            product_url = dict(eval(str(self.create_url()).replace('}, {', ', '))[0]).get(category_url)
            self.extract_items_urls(item_data.get('response_data'), category_url, product_url)

        return self.items_json


# get_items_from_category = SearchOnlineForItems('iphone', 'eg', 'en').main()
#
# print(get_items_from_category)


# get items data EN and AR
class GetItemsData:
    def __init__(self, items_object, *kwargs):
        self.items_object = items_object
        self.items_data = {}
        self.languages = kwargs

    def website_get_xp(self, url: str):
        websites = supported_search_website_xp.keys()
        if url:
            for website in websites:
                if website.strip() in url:
                    return website

    def get_product_data(self):
        # print(self.items_object)
        response_data = FETCH(self.items_object, 'product_page', self.languages).start()
        # print(self.items_object)
        return response_data

    def extract_product_data(self):
        for sku, item in self.get_product_data().items():
            for lang in self.languages:
                url = item.get(f'item_url_{lang}')
                item_uid = item.get('item_uid')
                country = item.get('country')
                item_obj = ''
                if lang == 'en':
                    websites_ob = Websites(url, currency(url), country, item.get(f'response_data_{lang}'))
                    item_obj = {
                        item_uid: json.loads(websites_ob.extract_data())
                    }
                    # ADD SEARCH VALUE ITEM OBJ

                elif lang == 'ar':
                    title_xp = supported_website_xp.get(self.website_get_xp(url)).get('title_xp')
                    product_type_ar_xp = supported_website_xp.get(self.website_get_xp(url)).get('product_type_xp')
                    brand_xp = supported_website_xp.get(self.website_get_xp(url)).get('brand_xp')

                    html_page = item.get(f'response_data_{lang}')
                    tree = html.fromstring(html_page)
                    product_type = list(
                        dict.fromkeys(
                            [re.sub(r'\n+|\s+', ' ', item).strip() for item in tree.xpath(product_type_ar_xp)]
                        )
                    )
                    item_obj = {
                        item_uid: {
                            'item_title_ar': ''.join(list(dict.fromkeys(tree.xpath(title_xp)))).strip(),
                            'product_type_ar': ' @ '.join(list(filter(None, product_type))).strip(),
                            'item_url_ar': url,
                            'brand_ar': ''.join(list(dict.fromkeys(tree.xpath(brand_xp)))).replace('Brand: ',
                                                                                                   '').strip(),
                            # ADD SEARCH VALUE ITEM OBJECT
                            'search_value': self.items_object[0].get('search_value')
                        }
                    }
                if self.items_data.get(item_uid):
                    self.items_data[item_uid].update(item_obj.get(item_uid))
                else:
                    self.items_data.update(item_obj)
        #             to be active to upload images !!!! Important
        # self.items_data = FETCH(list(self.items_data.values()), 'images', ['img']).start()
        return self.items_data


# import time
#
# startTime = time.time()
# # your code here
#
# get_urls_category_page = SearchOnlineForItems('shower gel', 'eg', 'en').main()
# #
# data = GetItemsData(get_urls_category_page, 'en', 'ar').extract_product_data()
# print(data)
# #
# ex = UploadDB(data, 'eg', 'shower gel').main()
# # print(ex)
# # #
# endTime = time.time() - startTime
# print(endTime)
# # #

