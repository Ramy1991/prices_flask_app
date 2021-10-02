import firebase_admin
from firebase_admin import db
import json

cred_obj = firebase_admin.credentials.Certificate('bright-lattice-260000-firebase-adminsdk.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://bright-lattice-260000.firebaseio.com'
})


# default_app = firebase_admin.initialize_app()
class GetTrackedProducts:
    def __init__(self):
        self.tracking_products = {}
        self.users_data = {}

    def extract_data_firebase(self):
        ref = db.reference("/users")
        get_tracked_items = json.dumps(ref.order_by_child('num_of_t_items').start_at(1).get())
        # d = json.loads(get_tracked_items.values()
        print(json.loads(get_tracked_items).values())
        for key, val in json.loads(get_tracked_items).items():
            print(val.get('tracking_items'))




# print(len(get_tracked_items))
# for i in ref:
#     print(i)
