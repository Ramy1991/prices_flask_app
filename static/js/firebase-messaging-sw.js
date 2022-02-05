// import { getMessaging, getToken } from 'https://www.gstatic.com/firebasejs/9.1.3/firebase-messaging.js';
// import { onBackgroundMessage } from 'https://www.gstatic.com/firebasejs/9.1.3/firebase-messaging-sw.js';
// import { initializeApp } from "https://www.gstatic.com/firebasejs/9.1.3/firebase-app.js";


// const firebaseConfig = {
//     apiKey: "AIzaSyCQYdl0vf8gKnayNRM18dbfMpYIQxzi0LI",
//     authDomain: "bright-lattice-260000.firebaseapp.com",
//     databaseURL: "https://bright-lattice-260000.firebaseio.com",
//     projectId: "bright-lattice-260000",
//     storageBucket: "bright-lattice-260000.appspot.com",
//     messagingSenderId: "1014243229877",
//     appId: "1:1014243229877:web:71f55e2379e3c05a8bfefc",
//     measurementId: "G-275CEDTFV7"
// };
// const app = initializeApp(firebaseConfig);
// const messaging = getMessaging();
// onBackgroundMessage(messaging, (payload) => {
//     console.log(payload);
// });

import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.6/firebase-app.js";
import { getMessaging } from'https://www.gstatic.com/firebasejs/9.6.6/firebase-messaging.js';;

// Initialize the Firebase app in the service worker by passing in
// your app's Firebase config object.
// https://firebase.google.com/docs/web/setup#config-object
const firebaseApp = initializeApp({
  apiKey: 'api-key',
  authDomain: 'project-id.firebaseapp.com',
  databaseURL: 'https://project-id.firebaseio.com',
  projectId: 'project-id',
  storageBucket: 'project-id.appspot.com',
  messagingSenderId: 'sender-id',
  appId: 'app-id',
  measurementId: 'G-measurement-id',
});

// Retrieve an instance of Firebase Messaging so that it can handle background
// messages.
const messaging = getMessaging(firebaseApp);