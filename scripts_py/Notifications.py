from firebase_admin import messaging
import firebase_admin

cred_obj = firebase_admin.credentials.Certificate('bright-lattice-260000-firebase-adminsdk.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://bright-lattice-260000.firebaseio.com'
})

registration_tokens = [
    'fZrwDtJVpFnJazYQtNCVhK:APA91bGEod7CzMuqZue6X3WY6WzNBWYixzqWzOnZoJW6fQvjck_j6Em9Wv79F7WP62ChiwGTazbzyEEFQez_1QcA6km1vlCt-e7JoJRngZK2YHuqIO-09_eNI6VwEUlG7uEVUjRQgWWP',
    # ...
    'fZrwDtJVpFnJazYQtNCVhK:APA91bGEod7CzMuqZue6X3WY6WzNBWYixzqWzOnZoJW6fQvjck_j6Em9Wv79F7WP62ChiwGTazbzyEEFQez_1QcA6km1vlCt-e7JoJRngZK2YHuqIO-09_eNI6VwEUlG7uEVUjRQgWW',
]

message = messaging.MulticastMessage(
    data={'score': '850', 'time': '2:45'},
    tokens=registration_tokens,
)
response = messaging.send_multicast(message)
# See the BatchResponse reference documentation
# for the contents of response.
print('{0} messages were sent successfully'.format(response.success_count))
