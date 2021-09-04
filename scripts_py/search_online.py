from lxml import html
import re
import json
from scripts_py.extract_item_data import Websites
from scripts_py.supported_website import supported_website_xp, currency, supported_search_website_xp
from scripts_py.fetch_data import FETCH


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
                    'https://www.jumia.com.eg/catalog/?q={}': 'https://www.jumia.com.eg',
                    'https://btech.com/en/catalogsearch/result/?q={}': 'https://btech.com/en/'
                },
                'ar': {
                    'https://www.noon.com/egypt-ar/search?q={}': 'https://www.noon.com/egypt-ar/{}/p',
                    'https://egypt.souq.com/eg-ar/{}/s/?as=1': 'https://egypt.souq.com/eg-ar/{}/s/',
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

        if self.website_get_xp(category_url) == 'noon.com':
            # print(response_data)
            json_text = re.findall(r'.hits..(.*)..searchEngine.', response_data)
            # fix json text adding quotes that replace in 000webhost
            # json_text = json_text[0].replace('noon_url', '"url"')
            json_items = json.loads(json_text[0])
            item_uid = []
            item_urls = []
            for json_item in json_items:
                item_urls.append(product_url.format(json_item.get('sku')))
                item_uid.append(json_item.get('sku'))
        else:
            item_uid = list(tree.xpath(uid_xp))
            item_urls = list(tree.xpath(url_xp))
        for uid, item_url in zip(item_uid, item_urls):

            uid = uid.split(",")
            # get url for jumia
            if self.website_get_xp(category_url) == 'jumia.com':
                item_url = ''.join([product_url, item_url])

            #  check current lang to get other lang url
            if self.lang == 'en':
                lang = 'ar'
            else:
                lang = 'en'

            uid[0] = {
                f"item_url_{self.lang}": item_url,
                f"item_url_{lang}": self.get_urls_for_en_ar(item_url),
                "item_uid": uid[0],
                "item_website": self.website_get_xp(category_url)
            }
            self.items_json.append(uid[0])

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

    def website_get_xp(self, url):
        websites = supported_search_website_xp.keys()
        for website in websites:
            if website in url:
                return website

    def get_product_data(self):
        response_data = FETCH(self.items_object, 'product_page', self.languages).start()
        # print(self.languages)
        return response_data

    def extract_product_data(self):
        for sku, item in self.get_product_data().items():
            for lang in self.languages:
                url = item.get(f'item_url_{lang}')
                item_uid = item.get('item_uid')
                item_obj = ''
                if lang == 'en':
                    websites_ob = Websites(url, currency(url), item.get(f'response_data_{lang}'))
                    item_obj = {
                        item_uid: json.loads(websites_ob.extract_data())
                    }
                elif lang == 'ar':
                    title_xp = supported_website_xp.get(self.website_get_xp(url)).get('title_xp')
                    html_page = item.get(f'response_data_{lang}')
                    tree = html.fromstring(html_page)
                    item_obj = {
                        item_uid: {
                            'item_title_ar': ''.join(list(dict.fromkeys(tree.xpath(title_xp))))
                        }
                    }
                if self.items_data.get(item_uid):
                    self.items_data[item_uid].update(item_obj.get(item_uid))
                else:
                    self.items_data.update(item_obj)
        self.items_data = FETCH(list(self.items_data.values()), 'images', ['img']).start()
        return self.items_data


get_urls_category_page = SearchOnlineForItems('iphone', 'eg', 'en').main()

data = GetItemsData(get_urls_category_page, 'en', 'ar').extract_product_data()

print(data)

# def run_crawler(self):
#     with ThreadPoolExecutor(max_workers=30) as executor:
#         results = executor.map(self.fetch, self.items_object)
#     return self.items_data
# search_val = 'thermal paste'.replace(' ', '%20')
###
# get_urls_category_page = SearchOnlineForItems('iphone', 'eg', 'en').main()
#
# data = GetItemsData(get_urls_category_page, 'en', 'ar').extract_product_data()
# # print(len(data))
# print(data)
# d = SearchOnlineForItems('iphone', 'eg', 'ar').main()


# data = GetItemsData(d).run_crawler()
# n = 1
# for i in d:
#     n += 1
# print(n)

# print(data)

# for websites in data:
#     for website, items in websites.items():
#         print(website)
#         for sku, item in items.items():
#             item_string = f"( {item.get('item_price')}, {}, {}, )"
#             print(item.get('item_price'))
# # print(d)
#
# query = 'INSERT INTO products_eg (unique_product_code, website_name, UIC, country, price_data, sub_category_en, ' \
#         'sub_category_ar, item_type_en, item_type_ar, search_key, search_key_ar, title_en, title_ar, ' \
#         'brand_en, brand_ar, images_url, product_direct_link_en, product_direct_link_ar, sold_out, item_date)'
# d = SearchOnlineForItems('iphone', 'eg', 'en').main()
# print(d)

#
# def validate_json(self, json_values):
#     missing_data = 'missing_data'
#     len_data = 0
#     for website in json_values:
#         for value in website:
#             if website[value]:
#                 len_data = len_data + 1
#             else:
#                 continue
#     if len_data == 0:
#         return missing_data
#     else:
#         return json.dumps(json_values)


# def main(links):
#     items_json = []

# async def fetch(url, session):
#     header = {
#         "User-Agent": user_agent(),
#         "Accept": "*/*",
#         "Accept-Language": "*/*",
#         "Accept-Charset": "*/*",
#         "Connection": "keep-alive",
#         "Keep-Alive": "300"
#     }
#     main_url = ''.join(url.values())
#     url = ''.join(url.keys())
#
#     async with session.get(url, headers=header) as response:
#         data = await response.text()
#         title_xp = supported_search_website_xp.get(website_check(url)).get('title_xp')
#         image_xp = supported_search_website_xp.get(website_check(url)).get('image_xp')
#         price_xp = supported_search_website_xp.get(website_check(url)).get('price_xp')
#         uid_xp = supported_search_website_xp.get(website_check(url)).get('uid_xp')
#         url_xp = supported_search_website_xp.get(website_check(url)).get('url_xp')
#         cate_xp = supported_search_website_xp.get(website_check(url)).get('cate_xp')
#         tree = html.fromstring(data)
#         if website_check(url) == 'noon.com':
#             data = await response.text()
#             json_text = re.findall(r'.hits..(.*)..searchEngine.', data)
#             json_items = json.loads(''.join(json_text))
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
#                 item_urls.append(main_url.format(json_item.get('sku')))
#                 item_uid.append(json_item.get('sku'))
#                 item_categories.append(''.join(list(tree.xpath(cate_xp))))
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
#         items_dict = {
#             website_check(url): {
#             }
#         }
#         for uid, title, image, price, i_url, cate, brand in zip(item_uid, item_titles, item_images, item_prices,
#                                                                 item_urls, item_categories, item_brand):
#             uid = uid.split(",")
#             try:
#                 price = ''.join(re.findall(r'(\d+)', price))
#             except TypeError:
#                 pass
#             if website_check(url) == 'jumia.com':
#                 i_url = ''.join([main_url, i_url])
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
#             items_dict[website_check(url)].update(item_dict)
#
#         return items_json.append(items_dict)

#     pl.task.each(fetch, links, workers=limit,
#                  on_start=lambda: dict(session=ClientSession(connector=TCPConnector(limit=0))),
#                  on_done=lambda session: session.close(), run=True, )
#
#     return validate_json(items_json)
#
#
# def create_url(search_value, country, lang):
#     websites = {
#         'eg': {
#             'en': {
#                 'https://www.noon.com/egypt-en/search?q={}': 'https://www.noon.com/egypt-en/{}/p',
#                 'https://egypt.souq.com/eg-en/{}/s/?as=1': 'https://egypt.souq.com/eg-en/{}/s/',
#                 'https://www.jumia.com.eg/catalog/?q={}': 'https://www.jumia.com.eg',
#                 'https://btech.com/en/catalogsearch/result/?q={}': 'https://btech.com/en/'
#             },
#             'ar': {
#                 'https://www.noon.com/egypt-ar/search?q={}': 'https://www.noon.com/egypt-ar/{}/p',
#                 'https://egypt.souq.com/eg-ar/{}/s/?as=1': 'https://egypt.souq.com/eg-ar/{}/s/',
#                 'https://www.jumia.com.eg/ar/catalog/?q={}': 'https://www.jumia.com.eg/ar',
#                 'https://btech.com/ar/catalogsearch/result/?q={}': 'https://btech.com/ar/'
#             }
#         },
#         'ae': {
#             'en': {
#                 'https://www.amazon.ae/s?k={}&ref=nb_sb_noss_2': 'https://www.amazon.ae/dp/{}/?language=en_AE',
#                 'https://www.noon.com/uae-en/search?q={}': 'https://www.noon.com/uae-en/{}/p'
#             },
#             'ar': {
#                 'https://www.amazon.ae/s?k={}&language=ar_AE&ref=nb_sb_noss_2': 'https://www.amazon.ae/dp/{}/?language=ar_AE',
#                 'https://www.noon.com/uae-ar/search?q={}': 'https://www.noon.com/uae-ar/{}/p'
#             }
#         },
#         'sa': {
#             'en': {
#                 'https://www.amazon.sa/s?k={}&ref=nb_sb_noss_2': 'https://www.amazon.sa/dp/{}/?language=en_AE',
#                 'https://www.noon.com/saudi-en/search?q={}': 'https://www.noon.com/saudi-en/{}/p'
#             },
#             'ar': {
#                 'https://www.amazon.sa/s?k={}&language=ar_AE&ref=nb_sb_noss_2': 'https://www.amazon.sa/dp/{}/?language=ar_AE',
#                 'https://www.noon.com/saudi-ar/search?q={}': 'https://www.noon.com/saudi-ar/{}/p'
#             }
#         }
#     }
#     urls = []
#
#     for url, i_url in websites.get(country).get(lang).items():
#         urls.append({url.format(search_value): i_url})
#     return urls

# print(main(create_url('iphone', 'eg', 'en')))

# links = create_url('ramy', 'Egypt')

# print(main(create_url('iphone', 'Egypt')))

# search_value22 = sys.argv[1]
# print(search_value22)
