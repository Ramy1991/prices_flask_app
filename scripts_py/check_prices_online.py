import firebase_admin
from firebase_admin import db
import json
from scripts_py.fetch_data import FETCH
import extract_item_data

cred_obj = firebase_admin.credentials.Certificate('bright-lattice-260000-firebase-adminsdk.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://bright-lattice-260000.firebaseio.com'
})


# default_app = firebase_admin.initialize_app()
class GetTrackedProducts:
    def __init__(self):
        self.tracking_products = {}
        self.users_data = {}
        self.product_to_update = {}

    def extract_data_firebase(self):
        ref = db.reference("/users")
        get_tracked_items = json.dumps(ref.order_by_child('num_of_t_items').start_at(1).get())
        # d = json.loads(get_tracked_items.values()
        # print(json.loads(get_tracked_items).values())
        for key, val in json.loads(get_tracked_items).items():
            product_object = val.get('tracking_items')
            self.tracking_products.update(product_object)
            users = {
                val.get('email'): val.get('tracking_items')
            }
            self.users_data.update(users)
        return self.tracking_products

    def get_product_prices(self):
        response = FETCH(list(self.extract_data_firebase().values()), 'product_page', 'e').start()
        for sku, item in response.items():
            url = item.get(f'item_url_e')
            websites_ob = extract_item_data.Websites(url, '', '', item.get(f'response_data_e'))
            new_product_data = json.loads(websites_ob.extract_data())
            # compare old price with new price
            SIC = new_product_data.get('item_uid')
            new_price = new_product_data.get('item_price')
            old_data = db.reference("/p_p_data").child(SIC).get()
            print(old_data.get('item_price').get('EGP').values())


GetTrackedProducts().get_product_prices()

# print(len(get_tracked_items))
# for i in ref:
#     print(i)
