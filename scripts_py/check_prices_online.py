import firebase_admin
from firebase_admin import db
import json
from scripts_py.fetch_data import FETCH
import extract_item_data
from datetime import datetime
from collections import OrderedDict

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
        self.product_to_notify = {}

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
        # print(self.tracking_products)
        return self.tracking_products

    def get_product_prices(self):
        response = FETCH(list(self.extract_data_firebase().values()), 'firebase', 'e').start()
        now = datetime.now()
        # print(self.users_data.values())
        for sku, item in response.items():
            # extract date using extract_item_data (Xpath)
            url = item.get(f'item_url_e')
            websites_ob = extract_item_data.Websites(url, item.get('currency'), '', item.get(f'response_data_e'))
            new_product_data = json.loads(websites_ob.extract_data())

            # compare old price with new price
            sic = new_product_data.get('item_uid')
            new_price = new_product_data.get('item_price')
            currency = new_product_data.get('currency')

            # Get the recent update for the price
            old_data = db.reference(f"/p_p_data/{sic}/item_price/{currency}").get()
            print(new_price)
            # order price object based on time and date
            # ordered_data = OrderedDict(
            #     sorted(
            #         old_data.items(),
            #         key=lambda x: datetime.strptime(x[0], '%d-%m-%Y %H:%M:%S')
            #     )
            # )
            # recent_updated_price = float(list(ordered_data.values())[-1].get('price'))

            # check new price is not missing or out of stock
            # if new_price != 'missing_data':
            #     # check price change
            #     if float(new_price) != recent_updated_price:
            #         # product to be update on "p_p_data" firebase
            #         item = {
            #             f"/{str(sic)}/item_price/{currency}/{now.strftime('%d-%m-%Y %H:%M:%S')}": {
            #                 'date_time': now.strftime("%d-%m-%Y %H:%M:%S"),
            #                 'price': new_price
            #             }
            #         }
            #         self.product_to_update.update(item)
            #         item_to_notify = {
            #             sic: {
            #                 'date_time': now.strftime("%d-%m-%Y %H:%M:%S"),
            #                 'new_price': new_price,
            #                 'old_price': recent_updated_price,
            #                 'currency': currency
            #             }
            #         }
            #         self.product_to_notify.update(item_to_notify)

    def update_changes_to_firebase(self):
        # call function to export data and generate results
        self.get_product_prices()
        # select p_p_data from firebase
        if self.product_to_update:
            ref = db.reference("/p_p_data").update(self.product_to_update)
            return True
        else:
            return False

    def check_price_change_to_notify_user(self):
        for email, products in self.users_data.items():
            for sic, item in products.items():
                # check if user set a target_price
                target_price = item.get('target_price')
                new_price = float(self.product_to_notify.get(sic).get('new_price'))
                old_price = float(self.product_to_notify.get(sic).get('old_price'))
                if target_price and new_price <= float(target_price):
                    print(f'notify customer ** {new_price} {target_price}')
                elif not target_price and new_price < old_price:
                    print(f'notify customer {new_price} {old_price}')
                else:
                    print(f' {new_price} {old_price}')
                # print(email)
                # print(new_price)

    def main(self):
        self.get_product_prices()
        # self.update_changes_to_firebase()
        if self.product_to_notify:
            self.check_price_change_to_notify_user()
    # print(old_data_recent)
    # print(self.users_data)

    # need to test the last updated price if exported from db
    #  B07G88JZ8L


GetTrackedProducts().main()

# print(len(get_tracked_items))
# for i in ref:
#     print(i)
