from firebase_admin import messaging
import firebase_admin
# import base64
# message = "AAAA7CWbgLU:APA91bECBRN1NDe9l7QBa--1pd69nNOKrIJdIm6FRXo793JsOXvfcijyc_KJlOv34DggcHeS9jX4As0r278Qne4QyQ4aXh9E9EhUhLZmJYpWMGm3vMH4LweFgP0JDtauovQivzV8nk8B"
#
# # message = "Python is fun"
# message_bytes = message.encode('ascii')
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('ascii')
# print(base64_message)

cred_obj = firebase_admin.credentials.Certificate('bright-lattice-260000-firebase-adminsdk.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://bright-lattice-260000.firebaseio.com'
})

registration_tokens = [
    'fZrwDtJVpFnJazYQtNCVhK:APA91bHpifQNDRTCNA992Gt25KhpGNemzS5nZ4-TlrNfop__Q9kyYynpAH1A-UiPi1xnYgVtV5qWcfr7ok8n-8cJQD5cdssf2qu9t8n9RKTzjUYYsc1tzP-d-ZD66170somvYY6AskvR',
    # ...
    'fZrwDtJVpFnJazYQtNCVhK:APA91bHpifQNDRTCNA992Gt25KhpGNemzS5nZ4-TlrNfop__Q9kyYynpAH1A-UiPi1xnYgVtV5qWcfr7ok8n-8cJQD5cdssf2qu9t8n9RKTzjUYYsc1tzP-d-ZD66170somvYY6Askv',
]

message = messaging.MulticastMessage(
    data={'score': '850', 'time': '2:45'},
    tokens=registration_tokens,
)
response = messaging.send_multicast(message)
# See the BatchResponse reference documentation
# for the contents of response.
print('{0} messages were sent successfully'.format(response.success_count))
