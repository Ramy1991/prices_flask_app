import { getMessaging, getToken, onMessage } from 'https://www.gstatic.com/firebasejs/9.6.6/firebase-messaging.js';
import { onBackgroundMessage } from 'https://www.gstatic.com/firebasejs/9.6.6/firebase-messaging-sw.js';
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.6/firebase-app.js";


const firebaseConfig = {
    apiKey: "AIzaSyCQYdl0vf8gKnayNRM18dbfMpYIQxzi0LI",
    authDomain: "bright-lattice-260000.firebaseapp.com",
    databaseURL: "https://bright-lattice-260000.firebaseio.com",
    projectId: "bright-lattice-260000",
    storageBucket: "bright-lattice-260000.appspot.com",
    messagingSenderId: "1014243229877",
    appId: "1:1014243229877:web:71f55e2379e3c05a8bfefc",
    measurementId: "G-275CEDTFV7"
};




if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register(window.location.origin + "/firebase-messaging-sw.js", {scope: '/'}).then(registration => {
        console.log("ServiceWorker running");
    }).catch(err => {
        console.log(err);
    })
  }



const app = initializeApp(firebaseConfig);
// Get registration token. Initially this makes a network call, once retrieved
// subsequent calls to getToken will return from cache.
const messaging = getMessaging();
getToken(messaging, { vapidKey: 'BCCQ90gHgbcJsHwGMOFcA7ZleVGWn8VRvvfiQ7_kXkQjKCtbVItTZ_jWclGCWdRvWiv9wVUnVEZu6dSSwt9A13s' }).then((currentToken) => {
  if (currentToken) {
    // Send the token to your server and update the UI if necessary
    console.log(currentToken);
    
    // ...
  } else {
    // Show permission request UI
    console.log('No registration token available. Request permission to generate one.');
    // ...
  }
}).catch((err) => {
  console.log('An error occurred while retrieving token. ', err);
  // ...
});

onMessage(messaging, (payload) => {
  console.log('Message received. ', payload);
  // ...
});

// onBackgroundMessage(messaging, (payload) => {
//   console.log('[firebase-messaging-sw.js] Received background message ', payload);
//   // Customize notification here
//   const notificationTitle = 'Background Message Title';
//   const notificationOptions = {
//     body: 'Background Message body.',
//     icon: '/firebase-logo.png'
//   };

//   self.registration.showNotification(notificationTitle,
//     notificationOptions);
// });

// function subscribe() {
//   // Disable the button so it can't be changed while
//   // we process the permission request
//   // var pushButton = document.querySelector('.js-push-button');
//   // pushButton.disabled = true;

//   navigator.serviceWorker.ready.then(function(serviceWorkerRegistration) {
//     // const pushSubscription = serviceWorkerRegistration.pushManager.subscribe({userVisibleOnly: true});
//     // The push subscription details needed by the application
//     // server are now available, and can be sent to it using,
//     // for example, an XMLHttpRequest.
//     // console.log(pushSubscription);
//     // console.log(pushSubscription.getKey("p256dh"));
//     // console.log(pushSubscription.getKey("auth"));
//     const subscribeOptions = {
//       userVisibleOnly: true,
//       applicationServerKey: convertDataURIToBinary('BCCQ90gHgbcJsHwGMOFcA7ZleVGWn8VRvvfiQ7_kXkQjKCtbVItTZ_jWclGCWdRvWiv9wVUnVEZu6dSSwt9A13s')
//     };
//     serviceWorkerRegistration.pushManager.subscribe(subscribeOptions).then(function(subscription) {
//         // The subscription was successful
        
//         // and save it to send a push message at a later date
//       console.log(subscription);
//     }).catch(function(e) {
//         if (Notification.permission === 'denied') {
//           // The user denied the notification permission which
//           // means we failed to subscribe and the user will need
//           // to manually change the notification permission to
//           // subscribe to push messages
//           console.warn('Permission for Notifications was denied');
//           // pushButton.disabled = true;
//         } else {
//           // A problem occurred with the subscription; common reasons
//           // include network errors, and lacking gcm_sender_id and/or
//           // gcm_user_visible_only in the manifest.
//           console.error('Unable to subscribe to push.', e);
//         }
//       });
//   });
// }


// self.addEventListener('push', function(event) {
//   console.log('Received a push message', event);
//   console.log(event);
//   console.log('Received a push message', event);
//   data = event.data.json();
//   var title = data.notification.title;
//   var body = data.notification.message;
//   var icon = data.notification.icon;
//   var notificationTag = data.notification.tag;

//   var notification = new self.Notification(title, {
//     body: body,
//     tag: notificationTag,
//     icon: icon
//   });

//   event.waitUntil(
//     self.registration.showNotification(title, {
//       body: body,
//       icon: icon,
//       tag: notificationTag
//     })
//   );
// });

// var BASE64_MARKER = ';base64,';

// function convertDataURIToBinary(dataURI) {
//   var base64Index = dataURI.indexOf(BASE64_MARKER) + BASE64_MARKER.length;
//   var base64 = dataURI.substring(base64Index);
//   var raw = window.atob(base64);
//   var rawLength = raw.length;
//   var array = new Uint8Array(new ArrayBuffer(rawLength));

//   for(i = 0; i < rawLength; i++) {
//     array[i] = raw.charCodeAt(i);
//   }
//   return array;
// }

// function urlBase64ToUint8Array(base64String) {
//   var padding = '='.repeat((4 - base64String.length % 4) % 4);
//   var base64 = (base64String + padding)
//       .replace(/\-/g, '+')
//       .replace(/_/g, '/');

//   // var rawData = b64EncodeUnicode( base64 );
//   var rawData = atob(base64);
//   var outputArray = new Uint8Array(rawData.length);

//   for (var i = 0; i < rawData.length; ++i) {
//       outputArray[i] = rawData.charCodeAt(i);
//   }
//   return outputArray;
// }