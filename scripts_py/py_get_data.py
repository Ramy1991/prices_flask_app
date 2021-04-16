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


# def upload_image(image_url, uid):
#     try:
#         if not firebase_admin._apps:
#             cred = credentials.Certificate(r'scripts_py/bright-lattice-260000-firebase-adminsdk.json')
#             firebase_admin.initialize_app(cred, {'storageBucket': 'bright-lattice-260000.appspot.com'})
#         bucket = storage.bucket()
#         image_data = requests.get(image_url).content
#         blob = bucket.blob("product_images/" + uid + '.jpg')
#         blob.upload_from_string(image_data, content_type='image/jpg')
#         return blob.public_url
#     except exceptions:
#         return exceptions


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


# class Websites(object):
#     def __init__(self, _title, _image, _url, _price, _uid, _currency):
#         self.item_title = _title
#         self.item_image = _image
#         self.item_url = _url
#         self.item_price = _price
#         self.item_uid = _uid
#         self.currency = _currency
#         self.date = str(date.today().strftime("%d-%m-%Y"))
#         self.time = datetime.now().strftime("%H:%M:%S")
#         self.website = re.search(r':\/\/(.*?)\/', _url.strip()).group(1)
#
#     def upload_image(self):
#         try:
#             if not firebase_admin._apps:
#                 cred = credentials.Certificate(r'bright-lattice-260000-firebase-adminsdk.json')
#                 firebase_admin.initialize_app(cred, {'storageBucket': 'bright-lattice-260000.appspot.com'})
#             bucket = storage.bucket()
#             image_data = requests.get(image_url).content
#             blob = bucket.blob("product_images/" + uid + '.jpg')
#             blob.upload_from_string(image_data, content_type='image/jpg')
#             return blob.public_url
#         except exceptions:
#             return exceptions
#
#     def validate_args(self):
#         missing_data = ['missing_data:']
#         for key in json_values:
#             value = re.sub(r'\s+', '', json_values[key])
#             if not value:
#                 missing_data.append(key)
#         if len(missing_data) > 1:
#             return ' '.join(missing_data)
#         else:
#             return json_values
#
#     def noon(self):
#         item_uid_ = json.loads(self.item_uid)
#         self.item_price = str(
#             item_uid_['props']['pageProps']['catalog']['product']['variants'][0]['offers'][0]['sale_price'])
#         if self.item_price == 'None':
#             self.item_price = str(
#                 item_uid_['props']['pageProps']['catalog']['product']['variants'][0]['offers'][0]['price'])
#         self.item_uid = item_uid_['props']['pageProps']['catalog']['product']['variants'][0]['offers'][0][
#             'sku_config']
#         self.item_image = upload_image(self.item_image, self.item_uid.strip())
#         return self.__dict__
#
#     def b_tech(self):
#         self.item_image = upload_image(self.item_image, self.item_uid.strip())
#         return validate_json(self.__dict__)
#
#     def jumia(self):
#         self.item_uid = self.item_uid.replace(':', '').strip()
#         if self.item_price.strip():
#             item_price = self.item_price.replace(r'window.__STORE__=', '')
#             self.item_price = json.loads(item_price.replace(r';', '').strip())['simples'][0]['prices']['rawPrice']
#         self.item_image = upload_image(self.item_image, self.item_uid.strip())
#         return self.__dict__
#
#     def souq(self):
#         return self.__dict__


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

            # websites_ob = Websites(item_title, item_image, url, item_price, item_uid, currency(url))
            #  website validation
            if website_check(url) == "noon.com":

                # print(websites_ob.noon())

                item_uid = json.loads(item_uid)
                item_price = str(
                    item_uid['props']['pageProps']['catalog']['product']['variants'][0]['offers'][0]['sale_price'])
                if item_price == 'None':
                    item_price = str(
                        item_uid['props']['pageProps']['catalog']['product']['variants'][0]['offers'][0]['price'])
                item_uid = item_uid['props']['pageProps']['catalog']['product']['variants'][0]['offers'][0][
                    'sku_config']
                domain = re.search(r':\/\/(www\.noon.*?\/.*?)\/', url.strip()).group(1)
            elif "amazon." in website_check(url):
                # if size or color not selected
                try:
                    # image size
                    item_image = re.sub(r'._(.*?)_.jpg', '._UL1500_.jpg', item_image)
                    item_image = re.search(r'{.(.*?)\":', item_image.strip()).group(1)
                except AttributeError:
                    pass

                item_size_xp = supported_website_xp.get(website_check(url)).get('item_size')
                item_size = ''.join(tree.xpath(item_size_xp)).strip()
                if item_size:
                    item_title = item_title + ' size, ' + item_size
                domain = re.search(r':\/\/(.*?)\/', url.strip()).group(1)
                size_check = ''.join(tree.xpath('//*[@id="partialStateBuybox"]/div/div[1]/span//text()')).strip()
                if size_check:
                    item_sizes = tree.xpath(
                        "//select[@data-a-touch-header='Size']//option[@class='dropdownAvailable']/@data-a-html-content")
                    item_asins = tree.xpath(
                        "//select[@data-a-touch-header='Size']//option[@class='dropdownAvailable']/@value")
                    item_size_dict = dict(zip(item_sizes, item_asins))
                    item_info = {
                        'item_title': item_title.strip(),
                        'item_image': item_image.strip(),
                        'item_price': item_price.strip(),
                        'item_sizes': validate_json(item_size_dict)
                    }
                    # print(item_title.strip() + '@' + item_image.strip() + '@' + item_price.strip() + '@')
                    # item_data = validate_json(item_size_dict)
                    # print(json.dumps(item_info))
                    # exit()
                    return json.dumps(item_info)
                # try to extract image
            elif website_check(url) == "btech.com":
                # print(websites_ob.b_tech())
                domain = re.sub(r'(.en.*)', '', url)
            elif website_check(url) == "jumia.com":
                # print(websites_ob.jumia())
                item_uid = item_uid.replace(':', '').strip()
                domain = url
                if item_price.strip():
                    item_price = item_price.replace(r'window.__STORE__=', '')
                    item_price = json.loads(item_price.replace(r';', '').strip())['simples'][0]['prices']['rawPrice']
            else:
                domain = re.search(r':\/\/(.*?)\/', url.strip()).group(1)

            # Price Validation
            if not item_price.strip():
                item_price = "Out of Stock"
            else:
                item_price = re.search(r'(\d+.\d+|\d+|\d+.\d+.\d+)', item_price.strip()).group(1)
                item_price = re.sub(r',', '.', item_price)

            date_now = str(date.today().strftime("%d-%m-%Y"))
            time_now = datetime.now().strftime("%H:%M:%S")

            items_data_list = {'item_title': item_title.strip(),
                               # 'item_image': upload_image(item_image, item_uid.strip()),
                               'item_image': item_image,
                               'item_url': url.strip(), 'item_price': item_price, 'item_uid': item_uid.strip(),
                               'currency': currency(url), 'time': time_now, 'date': date_now,
                               'website': domain}
            item_data = validate_json(items_data_list)
            return json.dumps(item_data)
            # print(json.dumps(item_data))

    # loop = asyncio.get_event_loop()
    return main()


def check_url(url):
    if website_check(url):
        return get_data(url)
    else:
        return "dummy_website"

#
# print(check_url(
#     'https://www.amazon.com//dp/B0812K484R'))

# ua = UserAgent()
#
# header = {'User-Agent': str(ua.chrome)}
# page = requests.get(url, headers=header)
#
#
# tree = html.fromstring(page.content)
# item_title = tree.xpath(title_xp+"//text()")
# item_image = tree.xpath(image_xp)[0]
# item_url = tree.xpath(url_xp)[0]
# item_price = tree.xpath(price_xp+"//text()") https://btech.com/ar/xiaomi-redmi-note-9-pro-64gb-green-1614003650.html
# item_uid = tree.xpath(uid_xp+"//text()")
#

#
# user_id = u'9VTVXwqtV1bwx5ug9vSqywGsPgF3'
#
#
# doc_ref = db.collection(u'users').document(user_id)
#
# doc_ref.update({
#     u'name': u'Frank',
#     u'tracking_items': {
#         u'item_uid': {
#             u'item_uid': u'item_uid',
#             u'item_image': u'Blue',
#             u'item_url': u'Recess',
#             u'item_title': u'Recess',
#             u'item_price': u'Recess'
#         }
#     }
# })
