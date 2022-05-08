from lxml import html
from datetime import datetime, date
from concurrent.futures import ThreadPoolExecutor
from scripts_py.supported_website import supported_website_xp, currency
# from supported_website import supported_website_xp, currency
# import firebase_admin
# from firebase_admin import credentials, storage, exceptions
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
        # elif key == 'item_url':
        #     continue
        else:
            missing_data[key] = value
    else:
        return missing_data


class Websites(object):
    def __init__(self, i_url, i_currency, country, html_page):
        self.item_title = ''
        self.item_image = ''
        self.item_url = i_url
        self.item_price = ''
        self.item_uid = ''
        self.product_type = ''
        self.currency = i_currency.strip()
        self.date = str(date.today().strftime("%d-%m-%Y"))
        self.time = datetime.now().strftime("%H:%M:%S")
        self.item_website = re.search(r':\/\/(.*?)\/', i_url.strip()).group(1)
        self.country = country
        self.tree = html.fromstring(html_page)
        self.item_sizes = ''
        self.brand = ''

    def noon(self):
        item_uid_ = json.loads(self.item_uid)

        # print(item_uid_['props']['pageProps']['props']['catalog']['product'])
        item_data = item_uid_['props']['pageProps']['props']['catalog']['product']['variants'][0]['offers']

        if item_data:
            self.item_price = str(item_data[0]['sale_price'])
            if self.item_price == 'None':
                self.item_price = str(item_data[0]['price'])
        else:
            try:
                self.item_price = re.search(r'(\d+\.\d+)|(\d+)', self.item_price).group(1)
            except Exception:
                self.item_price = ''
        if item_data:
            self.item_uid = dict(item_data[0])['sku_config']
            self.brand = item_uid_['props']['pageProps']['props']['catalog']['product']['brand']
            self.item_image = self.item_image.replace('r:n-t_120', 'r:n-t_400')
        else:
            self.item_uid = ''
            self.brand = ''
            self.item_image = ''
        self.tree = ''
        return self.__dict__

    def b_tech(self):
        self.tree = ''
        self.item_price = self.item_price.replace(',', '')
        return self.__dict__

    def jumia(self):
        # self.item_uid = self.item_uid.replace(':', '').strip()
        if ''.join(self.item_price).strip():
            item_price = ''.join(self.item_price).replace(r'window.__STORE__=', '')
            self.item_price = json.loads(item_price.replace(r';', '').strip())['simples'][0]['prices']['rawPrice']
        self.tree = ''

        return self.__dict__

    def souq(self):
        self.tree = ''
        return self.__dict__

    def amazon(self):
        self.item_title = self.item_title.replace('\"', "'")
        self.brand = re.sub(r'(\s+|\\n|\\t)', ' ', self.brand)
        try:
            self.item_image = re.sub(r'._(.*)_.jpg', '._AC_SL1500_.jpg', self.item_image)
            # self.item_image = re.search(r'{.(.*?)\":', item_image.strip()).group(1)
        except AttributeError:
            pass
        self.brand = self.brand.replace('Brand: ', '')
        try:
            self.item_price = re.sub(r'](.*)', ']', self.item_price)
            self.item_price = json.loads(self.item_price)[0].get('integerValue').replace(',', '')
        except Exception:
            self.item_price = re.search(r'(\d+.\d+)|(\d+)', self.item_price).group(0)

        # Check Sizes
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
        product_type_xp = supported_website_xp.get(website_check(self.item_url)).get('product_type_xp')
        brand_xp = supported_website_xp.get(website_check(self.item_url)).get('brand_xp')

        self.item_title = ''.join(list(dict.fromkeys(self.tree.xpath(title_xp)))).strip()
        self.item_image = ''.join(list(dict.fromkeys(self.tree.xpath(image_xp)))).strip()
        item_price = ''.join(list(dict.fromkeys(self.tree.xpath(price_xp)))).strip()
        self.item_uid = ''.join(list(dict.fromkeys(self.tree.xpath(uid_xp)))).strip()
        self.item_price = re.sub(r'\s+', '', item_price).strip()
        self.brand = ''.join(list(dict.fromkeys(self.tree.xpath(brand_xp)))).strip()

        product_type = list(
            dict.fromkeys(
                [re.sub(r'\n+|\s+', ' ', item).strip() for item in self.tree.xpath(product_type_xp)]
            )
        )
        self.product_type = ' @ '.join(list(filter(None, product_type)))

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
                'item_url': self.item_url,
                'currency': self.currency,
                'country': self.country
            }
            return json.dumps(validate_json(items))

        # ee = Websites.website_check('https://egypt.souq.com/eg-ar/%D8%AA%D9%8A-%D8%A8%D')


# print(ee)


def upload_image(item_obj):
    item_obj = [json.loads(item_obj)]
    item_obj = FETCH(item_obj, 'images', ['img']).start()
    return item_obj


# get item data for single item
def main(url, country):
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
        websites_ob = Websites(url, currency(url), country, html_page)
        # image upload
        # json.dumps(list(upload_image(websites_ob.extract_data()).values())[0])
        return websites_ob.extract_data()


def check_url(url, country):
    if website_check(url):
        return main(url, country)
    else:
        return "dummy_website"

#
# urll = 'https://www.noon.com/egypt-en/plus-20000mah-power-bank-wireless-charging-black/N52455107A/p/?o=a2eb16deb22d5dca'
# data = check_url(urll, "")
# print(data)

# item_data = check_url(urll)
# print(item_data)

# print(check_url(
#     'https://www.noon.com/egypt-en/playstation-5-console-extra-dualsense-wireless-controller/N45488091A/p?o=e10fe673323680ab'))
