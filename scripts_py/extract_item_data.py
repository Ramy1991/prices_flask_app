from lxml import html
from datetime import datetime, date
from concurrent.futures import ThreadPoolExecutor
from scripts_py.supported_website import supported_website_xp, currency
# from supported_website import supported_website_xp, currency
import firebase_admin
from firebase_admin import credentials, storage, exceptions
import requests
import re
import json
from fake_useragent import UserAgent
from scripts_py.fetch_data import FETCH


# url = r"https://www.amazon.ae/-/ar/%D8%AD%D8%B0%D8%A7%D8%A1-%D8%B1%D8%AC%D8%A7%D9%84%D9%8A-%D8%A7%D9%84%D8%A7%D8%B1%D8%AA%D8%AF%D8%A7%D8%A1-Vega-9-Bourge/dp/B07V1WJVMK?language=en_AE"


# url = sys.argv[1]

def website_check(url):
    websites = supported_website_xp.keys()
    for website in websites:
        if website in url:
            return website


def user_agent():
    return re.search(r'(.*?)\)', UserAgent().random).group(1) + "MSIE 12;)"


def validate_json(json_values):
    missing_data = json_values
    for key, value in json_values.items():
        value = re.sub(r'\s+', '', value)
        if not value:
            missing_data[key] = 'missing_data'
        elif key == 'item_url':
            continue
        else:
            missing_data[key] = 'found'
    else:
        return missing_data


class Websites(object):
    def __init__(self, _url, _currency, html_page):
        self.item_title = ''
        self.item_image = ''
        self.item_url = _url
        self.item_price = ''
        self.item_uid = ''
        self.currency = _currency.strip()
        self.date = str(date.today().strftime("%d-%m-%Y"))
        self.time = datetime.now().strftime("%H:%M:%S")
        self.item_website = re.search(r':\/\/(.*?)\/', _url.strip()).group(1)
        self.tree = html.fromstring(html_page)
        self.item_sizes = ''

    def noon(self):
        item_uid_ = json.loads(self.item_uid)
        item_data = item_uid_['props']['pageProps']['catalog']['product']['variants'][0]['offers']
        if item_data:
            self.item_price = str(
                item_uid_['props']['pageProps']['catalog']['product']['variants'][0]['offers'][0]['sale_price'])
            if self.item_price == 'None':
                self.item_price = str(
                    item_uid_['props']['pageProps']['catalog']['product']['variants'][0]['offers'][0]['price'])
        else:
            try:
                self.item_price = re.search(r'(\d+\.\d+)|(\d+)', self.item_price).group(1)
            except Exception:
                self.item_price = ''

        self.item_uid = item_uid_['props']['pageProps']['catalog']['product']['sku']

        self.tree = ''
        return self.__dict__

    def b_tech(self):
        self.tree = ''
        return self.__dict__

    def jumia(self):
        self.item_uid = self.item_uid.replace(':', '').strip()
        if self.item_price.strip():
            item_price = self.item_price.replace(r'window.__STORE__=', '')
            self.item_price = json.loads(item_price.replace(r';', '').strip())['simples'][0]['prices']['rawPrice']
        self.tree = ''
        return self.__dict__

    def souq(self):
        self.tree = ''
        return self.__dict__

    def amazon(self):
        try:
            item_image = re.sub(r'._(.*?)_.jpg', '._UL1500_.jpg', self.item_image)
            self.item_image = re.search(r'{.(.*?)\":', item_image.strip()).group(1)
        except AttributeError:
            pass

        item_size_xp = supported_website_xp.get(website_check(self.item_url)).get('item_size')
        item_size = ''.join(self.tree.xpath(item_size_xp)).strip()
        if item_size:
            self.item_title = self.item_title + ', ' + item_size
        size_check = ''.join(self.tree.xpath('//*[@id="partialStateBuybox"]/div/div[1]/span//text()')).strip()
        if size_check:
            item_sizes = self.tree.xpath(
                "//select[@data-a-touch-header='Size']//option[@class='dropdownAvailable']/@data-a-html-content")
            item_asins = self.tree.xpath(
                "//select[@data-a-touch-header='Size']//option[@class='dropdownAvailable']/@value")
            item_size_dict = dict(zip(item_sizes, item_asins))
            # item_info = {
            #     'item_title': self.item_title.strip(),
            #     'item_image': self.item_image.strip(),
            #     'item_price': self.item_price.strip(),
            #     'item_uid': self.item_uid.strip(),
            #     'item_url': self.item_url.strip(),
            #     'currency': self.currency,
            #     'date': self.date.strip(),
            #     'website': self.website.strip(),
            #     'item_sizes': validate_json(item_size_dict)
            # }
            self.item_sizes = validate_json(item_size_dict)
            self.tree = ''
            return self.__dict__
        else:
            self.tree = ''
            return self.__dict__
        # self.tree = ''
        # return self.__dict__

    def extract_data(self):
        title_xp = supported_website_xp.get(website_check(self.item_url)).get('title_xp')
        image_xp = supported_website_xp.get(website_check(self.item_url)).get('image_xp')
        price_xp = supported_website_xp.get(website_check(self.item_url)).get('price_xp')
        uid_xp = supported_website_xp.get(website_check(self.item_url)).get('uid_xp')

        self.item_title = ''.join(list(dict.fromkeys(self.tree.xpath(title_xp))))
        self.item_image = ''.join(list(dict.fromkeys(self.tree.xpath(image_xp))))
        # self.item_image = ''
        item_price = ''.join(list(dict.fromkeys(self.tree.xpath(price_xp))))
        self.item_uid = ''.join(list(dict.fromkeys(self.tree.xpath(uid_xp))))
        self.item_price = re.sub(r'\s+', ' ', item_price)

        if self.item_title and self.item_image and self.item_price and self.item_uid:
            #  website validation
            if website_check(self.item_url) == "noon.com":
                return json.dumps(self.noon())
            elif "amazon." in website_check(self.item_url):
                return json.dumps(self.amazon())
            elif website_check(self.item_url) == "btech.com":
                return json.dumps(self.b_tech())
            elif website_check(self.item_url) == "jumia.com":
                return json.dumps(self.jumia())
            elif website_check(self.item_url) == "souq.com":
                return json.dumps(self.souq())
        else:
            items = {
                'item_title': self.item_title,
                'item_image': self.item_image,
                'item_price': self.item_price,
                'item_uid': self.item_uid,
                'item_url': self.item_url
            }
            return json.dumps(validate_json(items))

        # ee = Websites.website_check('https://egypt.souq.com/eg-ar/%D8%AA%D9%8A-%D8%A8%D')


# print(ee)


def upload_image(item_obj):
    item_obj = [json.loads(item_obj)]
    item_obj = FETCH(item_obj, 'images', ['img']).start()
    return item_obj


# get item data for single item
def main(url):
    header = {
        "User-Agent": user_agent(),
        "Accept": "*/*",
        "Accept-Language": "*/*",
        "Accept-Charset": "*/*",
        "Connection": "keep-alive",
        "Keep-Alive": "300"
    }
    with ThreadPoolExecutor(max_workers=20) as executor:
        request_1 = executor.submit(lambda: requests.get(url, headers=header))
        html_page = request_1.result().content
        websites_ob = Websites(url, currency(url), html_page)
        return upload_image(websites_ob.extract_data())


def check_url(url):
    if website_check(url):
        return main(url)
    else:
        return "dummy_website"


urll = 'https://egypt.souq.com/eg-ar/%D8%AA%D9%8A-%D8%A8%D9%8A-%D9%84%D9%8A%D9%86%D9%83-%D8%B1%D8%A7%D9%88%D8%AA%D8%B1-%D9%84%D8%A7%D8%B3%D9%84%D9%83%D9%8A-archer-c7-%D8%A8%D9%86%D8%B7%D8%A7%D9%82-%D8%AC%D9%8A%D8%AC%D8%A7%D8%A8%D8%AA-%D8%AB%D9%86%D8%A7%D8%A6%D9%8A-ac1750-6987615/i/'
# print(check_url(urll))

# item_data = check_url(urll)
# print(item_data)

# print(check_url(
#     'https://www.noon.com/egypt-en/playstation-5-console-extra-dualsense-wireless-controller/N45488091A/p?o=e10fe673323680ab'))
