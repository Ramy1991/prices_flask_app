from aiohttp import ClientSession, TCPConnector
import asyncio
import sys
import pypeln as pl
from scripts_py.supported_website import supported_search_website_xp, currency
from lxml import html
from fake_useragent import UserAgent
import re
import json

limit = 50


# cred = credentials.Certificate(r'D:\PyChaarm\Prices\bright-lattice-260000-firebase-adminsdk.json')
# firebase_admin.initialize_app(cred, {'databaseURL': 'https://bright-lattice-260000.firebaseio.com'})


# def selenium_request(url):
#     executable_path = r"D:\PyChaarm\Prices\geckodriver.exe"
#     # executable_path = r"D:\PyChaarm\Prices\phantomjs-2.1.1-windows\bin\phantomjs.exe"
#     options = Options()
#     options.headless = True
#     driver = webdriver.Firefox(options=options, executable_path=executable_path)
#     driver.get(url)
#     tree = html.fromstring(driver.page_source)
#     driver.close()
#     return tree


def website_check(url):
    websites = supported_search_website_xp.keys()
    for website in websites:
        if website in url:
            return website


def user_agent():
    return re.search(r'(.*?)\)', UserAgent().random).group(1) + "MSIE 12;)"


def validate_json(json_values):
    missing_data = 'missing_data'
    len_data = 0
    for website in json_values:
        for value in website:
            if website[value]:
                len_data = len_data + 1
            else:
                continue
    if len_data == 0:
        return missing_data
    else:
        return json.dumps(json_values)


def main(links):
    items_json = []

    async def fetch(url, session):
        header = {
            "User-Agent": user_agent(),
            "Accept": "*/*",
            "Accept-Language": "*/*",
            "Accept-Charset": "*/*",
            "Connection": "keep-alive",
            "Keep-Alive": "300"
        }
        async with session.get(url, headers=header) as response:
            data = await response.text()
            title_xp = supported_search_website_xp.get(website_check(url)).get('title_xp')
            image_xp = supported_search_website_xp.get(website_check(url)).get('image_xp')
            price_xp = supported_search_website_xp.get(website_check(url)).get('price_xp')
            uid_xp = supported_search_website_xp.get(website_check(url)).get('uid_xp')
            url_xp = supported_search_website_xp.get(website_check(url)).get('url_xp')
            tree = html.fromstring(data)
            if website_check(url) == 'noon.com':
                data = await response.text()
                json_text = re.findall(r'.hits..(.*)..searchEngine.', data)
                json_items = json.loads(''.join(json_text))
                item_titles = []
                item_images = []
                item_uid = []
                item_prices = []
                item_urls = []

                for json_item in json_items:
                    item_urls.append(json_item.get('url'))
                    item_uid.append(json_item.get('sku'))
                    item_titles.append(json_item.get('name'))
                    if type(json_item.get('sale_price')) != int:
                        item_prices.append(json_item.get('price'))
                    else:
                        item_prices.append(json_item.get('sale_price'))
                    item_images.append(
                        'https://a.nooncdn.com/t_desktop-pdp-v1/{}.jpg'.format(json_item.get('image_key')))
            else:
                item_titles = list(tree.xpath(title_xp))
                item_images = list(tree.xpath(image_xp))
                item_uid = list(tree.xpath(uid_xp))
                item_prices = list(tree.xpath(price_xp))
                item_urls = list(tree.xpath(url_xp))

            items_dict = {
                website_check(url): {
                }
            }
            for uid, title, image, price, i_url in zip(item_uid, item_titles, item_images, item_prices, item_urls):
                uid = uid.split(",")
                item_dict = {
                    uid[0]: {
                        "item_title": title,
                        "item_image": image,
                        "item_price": price,
                        "item_url": i_url,
                        "item_uid": uid[0]
                    }
                }
                items_dict[website_check(url)].update(item_dict)

            return items_json.append(items_dict)

    pl.task.each(fetch, links, workers=limit,
                 on_start=lambda: dict(session=ClientSession(connector=TCPConnector(limit=0))),
                 on_done=lambda session: session.close(), run=True, )

    return validate_json(items_json)


def create_url(search_value, country):
    urls = []
    if country == 'Egypt':
        urls.append("https://www.noon.com/egypt-en/search?q={}".format(search_value))  # EGYPT
        urls.append("https://egypt.souq.com/eg-en/{}/s/?as=1".format(search_value))  # EGYPT
        urls.append("https://www.jumia.com.eg/catalog/?q={}".format(search_value))  # EGYPT
        urls.append("https://btech.com/en/catalogsearch/result/?cat=All&q={}".format(search_value))  # EGYPT

    elif country == 'UAE':
        if search_value == "mobiles":
            urls.append("https://www.amazon.ae/s?k=smart+phone&ref=nb_sb_noss_2")
        else:
            urls.append("https://www.amazon.ae/s?k={}&ref=nb_sb_noss_2".format(search_value))
        urls.append("https://www.noon.com/uae-en/search?q={}".format(search_value))

    return urls


# links = create_url('ramy', 'Egypt')

# print(main(create_url('sdfghjhgfdsd', 'Egypt')))

# search_value22 = sys.argv[1]
# print(search_value22)
