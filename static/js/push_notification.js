import { getMessaging, getToken } from 'https://www.gstatic.com/firebasejs/9.1.3/firebase-messaging.js';
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.1.3/firebase-app.js";


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
    navigator.serviceWorker.register("../firebase-messaging-sw.s", {scope: '/'}).then(registration => {
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