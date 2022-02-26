from fake_useragent import UserAgent
from aiohttp import ClientSession, TCPConnector, client_exceptions
import asyncio
import re
import firebase_admin
from firebase_admin import credentials, storage, exceptions


class FETCH:
    def __init__(self, list_items, scape_type, *kwargs):
        self.items_list = list_items
        self.response = {}
        self.error_requests = []
        self.scape_type = scape_type
        self.languages = kwargs

    def header(self):
        try:
            user_agent = re.search(r'(.*?)\)', UserAgent().random).group(1) + "MSIE 12;)"
        except AttributeError:
            user_agent = re.search(r'(.*?)\)', UserAgent().random).group(1) + "MSIE 12;)"
        header = {
            "User-Agent": user_agent,
            "Accept": "*/*",
            "Accept-Language": "*/*",
            "Accept-Charset": "*/*",
            "Connection": "keep-alive",
            "Keep-Alive": "300"
        }

        return header

    def category_page(self, url, data):
        dict_items = {
            url.replace('https://data-pw.000webhostapp.com/?my_data=', ''): {
                "item_url": url.replace('https://data-pw.000webhostapp.com/?my_data=', ''),
                "response_data": data
            }
        }
        self.response.update(dict_items)
        # return self.response

    def product_page(self, item_object, url, lang, item_html):
        dict_item = {
            item_object.get('item_uid'): {
                "item_uid": item_object.get('item_uid'),
                f"item_url_{lang}": url.replace('https://data-pw.000webhostapp.com/?my_data=', ''),
                f"response_data_{lang}": item_html,
                "item_website": item_object.get('item_website'),
                "country": item_object.get('country'),
                "search_value": item_object.get('search_value'),
                "currency": item_object.get('currancy')
            }
        }
        if self.response.get(item_object.get('item_uid')):
            self.response[item_object.get('item_uid')].update(dict_item.get(item_object.get('item_uid')))
        else:
            self.response.update(dict_item)
        # return self.response

    def upload_image_to_cloud(self, item_object, image_data):
        item_uid = item_object.get('item_uid')

        if not firebase_admin._apps:
            # cred = credentials.Certificate('/scripts_py/bright-lattice-260000-firebase-adminsdk.json')
            try:
                cred = credentials.Certificate(r'scripts_py/bright-lattice-260000-firebase-adminsdk.json')
            except Exception:
                cred = credentials.Certificate(r'bright-lattice-260000-firebase-adminsdk.json')

            firebase_admin.initialize_app(cred, {'storageBucket': 'bright-lattice-260000.appspot.com'})

        bucket = storage.bucket()
        blob = bucket.blob("product_images/" + item_uid + '.jpg')
        blob.upload_from_string(image_data, content_type='image/jpg')
        item_object['item_image'] = blob.public_url
        self.response.update({item_uid: item_object})

    async def fetch(self, lang, item_obj, session):
        # store main data in variable
        item_object = item_obj
        if self.scape_type == 'category_page':
            url = ''.join(item_obj.keys())
        elif self.scape_type == 'images':
            # print(item_obj)
            url = item_obj.get('item_image')
            # print(url)
        elif self.scape_type == 'product_page':
        #     url = item_obj.get('item_url')
        # else:
            if lang == 'en':
                url = item_obj.get('item_url_en')
            elif lang == 'ar':
                url = item_obj.get('item_url_ar')

        # if noon website us third party host to get content 000webhost
        # if 'noon.com' in url:
        #     url = f'https://data-pw.000webhostapp.com/?my_data={url}'
        #     url = url

        try:
            response = await session.request(method='GET', url=url, headers=self.header())
            response.raise_for_status()
            # print(f"Response status {lang} ({url}): {response.status}")


            # fix json text adding quotes that replace in 000webhost "replace('noon_url', '"url"')"

            # parse data to json based on scrape type
            if self.scape_type == 'category_page':

                item_html = await response.text()
                item_html = item_html.replace('noon_url', '"url"')
                self.category_page(url, item_html)

            elif self.scape_type == 'product_page' or self.scape_type == 'firebase':

                item_html = await response.text()
                item_html = item_html.replace('noon_url', '"url"')
                self.product_page(item_object, url, lang, item_html)

            elif self.scape_type == 'images':

                image_data = await response.content.read()
                self.upload_image_to_cloud(item_object, image_data)
                # return self.response
            else:

                return 'Please Define Scrape Type'

        except Exception as err:
            self.error_requests.append(item_object)
            return f"An error ocurred in session: {err}"

    async def main(self, list_items):
        try:
            async with ClientSession() as session:
                # print(self.languages[0])
                for lang in self.languages[0]:
                    await asyncio.gather(*[self.fetch(lang, item_obj, session) for item_obj in list_items])
        except Exception as err:
            return f"An error ocurred in session: {err}"

    def start(self):
        if asyncio.get_event_loop().is_closed():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self.main(self.items_list))
        else:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.main(self.items_list))

        # check failed requests
        if self.error_requests:
            if asyncio.get_event_loop().is_closed():
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(self.main(self.error_requests))
            else:
                loop = asyncio.get_event_loop()
                loop.run_until_complete(self.main(self.error_requests))
                # print('done requests for errors')

        return self.response
        # return f"total input: {len(self.dict_urls)} - total output: {len(self.response)} - " \
        #        f"Faild: {len(self.error_requests)}"


# da = [{
#       "item_url_en":"https://www.jumia.com.eg/iphone-12-pro-max-with-facetime-256gb-pacific-blue-apple-mpg757129.html",
#       "item_url_ar":"https://www.jumia.com.eg/ar/iphone-12-pro-max-with-facetime-256gb-pacific-blue-apple-mpg757129.html",
#       "item_uid":"AP848MP0HFYPQNAFAMZ",
#       "item_website":"jumia.com",
#       "country":"eg",
#       "search_value":"iphone"
#    }]
# #
# data = FETCH(da, 'product_page', ['en', 'ar']).start()
# print(data)
