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
    missing_data = ['missing_data:']
    for key in json_values:
        value = re.sub(r'\s+', '', json_values[key])
        if not value:
            missing_data.append(key)
    if len(missing_data) > 1:
        return ' '.join(missing_data)
    else:
        return json_values


class Websites(object):
    def __init__(self, _title, _image, _url, _price, _uid, _currency, tree):
        self.item_title = _title.strip()
        self.item_image = _image.strip()
        self.item_url = _url.strip()
        self.item_price = _price.strip()
        self.item_uid = _uid.strip()
        self.currency = _currency.strip()
        self.date = str(date.today().strftime("%d-%m-%Y"))
        self.time = datetime.now().strftime("%H:%M:%S")
        self.website = re.search(r':\/\/(.*?)\/', _url.strip()).group(1)
        self.tree = tree

    def upload_image(self, item_image):
        try:
            if not firebase_admin._apps:
                cred = credentials.Certificate(r'scripts_py/bright-lattice-260000-firebase-adminsdk.json')
                firebase_admin.initialize_app(cred, {'storageBucket': 'bright-lattice-260000.appspot.com'})
            bucket = storage.bucket()
            image_data = requests.get(item_image).content
            blob = bucket.blob("product_images/" + self.item_uid + '.jpg')
            blob.upload_from_string(image_data, content_type='image/jpg')
            return blob.public_url
        except exceptions:
            return exceptions

    def noon(self):
        item_uid_ = json.loads(self.item_uid)
        self.item_price = str(
            item_uid_['props']['pageProps']['catalog']['product']['variants'][0]['offers'][0]['sale_price'])
        if self.item_price == 'None':
            self.item_price = str(
                item_uid_['props']['pageProps']['catalog']['product']['variants'][0]['offers'][0]['price'])
        self.item_uid = item_uid_['props']['pageProps']['catalog']['product']['variants'][0]['offers'][0][
            'sku_config']
        self.item_image = self.upload_image(self.item_image)
        return self.__dict__

    def b_tech(self):
        self.item_image = self.upload_image(self.item_image)
        return validate_json(self.__dict__)

    def jumia(self):
        self.item_uid = self.item_uid.replace(':', '').strip()
        if self.item_price.strip():
            item_price = self.item_price.replace(r'window.__STORE__=', '')
            self.item_price = json.loads(item_price.replace(r';', '').strip())['simples'][0]['prices']['rawPrice']
        self.item_image = self.upload_image()
        return self.__dict__

    def souq(self):
        self.item_image = self.upload_image(self.item_image)
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
            item_info = {
                'item_title': self.item_title.strip(),
                'item_image': self.item_image.strip(),
                'item_price': self.item_price.strip(),
                'item_sizes': validate_json(item_size_dict)
            }
            return json.dumps(item_info)
        else:
            self.item_image = self.upload_image(self.item_image)
            self.tree = ''
            return self.__dict__


def get_data(url):
    title_xp = supported_website_xp.get(website_check(url)).get('title_xp')
    image_xp = supported_website_xp.get(website_check(url)).get('image_xp')
    price_xp = supported_website_xp.get(website_check(url)).get('price_xp')
    uid_xp = supported_website_xp.get(website_check(url)).get('uid_xp')

    def main():
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
            tree = html.fromstring(html_page)

            item_title = ''.join(list(dict.fromkeys(tree.xpath(title_xp))))
            item_image = ''.join(list(dict.fromkeys(tree.xpath(image_xp))))
            item_price = ''.join(list(dict.fromkeys(tree.xpath(price_xp))))
            item_uid = ''.join(list(dict.fromkeys(tree.xpath(uid_xp))))
            item_price = re.sub(r'\s+', ' ', item_price)

            if item_title and item_image and item_price and item_uid:
                websites_ob = Websites(item_title, item_image, url, item_price, item_uid, currency(url), '')
                #  website validation
                if website_check(url) == "noon.com":
                    return json.dumps(websites_ob.noon())
                elif "amazon." in website_check(url):
                    websites_sub = Websites(item_title, item_image, url, item_price, item_uid, currency(url), tree)
                    return json.dumps(websites_sub.amazon())
                elif website_check(url) == "btech.com":
                    return json.dumps(websites_ob.b_tech())
                elif website_check(url) == "jumia.com":
                    return json.dumps(websites_ob.jumia())
                elif website_check(url) == "souq.com":
                    return json.dumps(websites_ob.souq())
            else:
                items = {
                    'item_title': item_title,
                    'item_image': item_image,
                    'item_price': item_price,
                    'item_uid': item_uid
                }
                return json.dumps(validate_json(items))

    return main()


def check_url(url):
    if website_check(url):
        return get_data(url)
    else:
        return "dummy_website"


# print(check_url('https://www.amazon.com/Acer-Display-Graphics-Keyboard-A515-43-R19L/dp/B07RF1XD36/ref=lp_16225007011_1_2'))

