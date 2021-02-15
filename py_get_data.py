from lxml import html
from datetime import datetime, date
from concurrent.futures import ThreadPoolExecutor
from supported_website import supported_website_xp, currency
import firebase_admin
from firebase_admin import credentials, storage
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


def upload_image(image_url, uid):
    if not firebase_admin._apps:
        cred = credentials.Certificate(r'bright-lattice-260000-firebase-adminsdk.json')
        firebase_admin.initialize_app(cred, {'storageBucket': 'bright-lattice-260000.appspot.com'})
    bucket = storage.bucket()
    image_data = requests.get(image_url).content
    blob = bucket.blob("product_images/" + uid + '.jpg')
    blob.upload_from_string(image_data, content_type='image/jpg')
    return blob.public_url


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

            #  website validation
            if website_check(url) == "noon.com":
                item_uid = re.search(r'\/(N.*?)\/p', item_uid.strip()).group(1)
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

                    print(item_title.strip() + '@' + item_image.strip() + '@' + item_price.strip() + '@')
                    item_data = validate_json(item_size_dict)
                    print(json.dumps(item_data))
                    exit()
                    return item_title.strip() + '@' + item_image.strip() + '@' + item_price.strip() + '@' + json.dumps(
                        item_data)
                # try to extract image

            elif website_check(url) == "btech.com":
                item_image = re.search(r'full.:.(.*?).,.caption', item_image).group(1).replace('\/', '/')
                domain = url
            elif website_check(url) == "jumia.com":
                item_uid = item_uid.replace(':', '').strip()
                domain = url
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
                               'item_image': upload_image(item_image, item_uid.strip()),
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


# print(check_url('https://www.jumia.com.eg/dalydress-floral-long-sleeves-blouse-with-embroidered-collar-multicolour-16066515.html'))

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
# item_price = tree.xpath(price_xp+"//text()")
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
